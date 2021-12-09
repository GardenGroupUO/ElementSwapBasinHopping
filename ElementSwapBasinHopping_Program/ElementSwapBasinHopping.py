import os
import numpy as np
from ase.units import kB
from ase.optimize.fire import FIRE
from ase.optimize.basin import BasinHopping
from random import randint
from copy import deepcopy

# Copied originally from https://gitlab.com/ase/ase/-/blob/master/ase/optimize/basin.py

class ElementSwapBasinHopping(BasinHopping):

	def __init__(self, atoms, temperature=100 * kB, optimizer=FIRE, fmax=0.1, dr=0.1, logfile='-',  trajectory='lowest.traj', optimizer_logfile='-', local_minima_trajectory='recorded_local_minima.traj', adjust_cm=True, start_recording_step=1, step_recording_interval=1, verbose=False, print_interval=1):
		"""
		Parameters:

		atoms: Atoms object
			The Atoms object to operate on.

		trajectory: string
			Pickle file used to store trajectory of atomic movement.

		logfile: file object or str
			If *logfile* is a string, a file with that name will be opened.
			Use '-' for stdout.
		"""

		if isinstance(start_recording_step,int) and (start_recording_step >= 1):
			self.start_recording_step = start_recording_step
		else:
			print('Error: start_recording_step must be an int and must be greater than or equal to 1.')
			print('start_recording_step = '+str(start_recording_step))
			exit('This program will finish without beginning')

		if isinstance(step_recording_interval,int) and (step_recording_interval >= 1):
			self.step_recording_interval = step_recording_interval
		else:
			print('Error: step_recording_interval must be an int and must be greater than or equal to 1.')
			print('step_recording_interval = '+str(step_recording_interval))
			exit('This program will finish without beginning')

		self.verbose = verbose
		self.print_interval = print_interval

		self.recorded_steps_data_filename = 'steps_recorded_into_'+local_minima_trajectory.replace('.','_')+'.txt'
		if os.path.exists(self.recorded_steps_data_filename):
			os.remove(self.recorded_steps_data_filename)
		self.recorded_steps_counter = 1
		with open(self.recorded_steps_data_filename,'w') as step_recorded_dataTXT:
			step_recorded_dataTXT.write('Image no in traj file starting at 1 (starting at 0): Step\n')

		'''
		self.kT = temperature
		self.optimizer = optimizer
		self.fmax = fmax
		self.dr = dr
		if adjust_cm:
			self.cm = atoms.get_center_of_mass()
		else:
			self.cm = None

		self.optimizer_logfile = optimizer_logfile
		self.lm_trajectory = local_minima_trajectory
		if isinstance(local_minima_trajectory, str):
			self.lm_trajectory = self.closelater(
				Trajectory(local_minima_trajectory, 'w', atoms))

		Dynamics.__init__(self, atoms, logfile, trajectory)
		self.initialize()
		'''

		BasinHopping.__init__(self,atoms,temperature,optimizer,fmax,dr,logfile,trajectory,optimizer_logfile,local_minima_trajectory,adjust_cm)

	def initialize(self):
		self.positions = 0.0 * self.atoms.get_positions()
		self.symbols = [''] * len(self.atoms.get_chemical_symbols())
		self.Emin = self.get_energy(self.atoms.get_positions(),self.atoms.get_chemical_symbols(),0) or 1.e32
		self.rmin = self.atoms.get_positions()
		self.positions = self.atoms.get_positions()
		self.symbols = self.atoms.get_chemical_symbols()
		self.call_observers()
		self.log(-1, self.Emin, self.Emin)

	def run(self, steps):
		"""
		OVERRIDDEN METHOD: This method is designed to override the original method in BasinHopping in ASE.

		Hop the basins for defined number of steps.
		"""

		ro = self.positions
		symbolso = self.symbols
		Eo = self.get_energy(ro,symbolso,0)

		for step in range(1,steps+1):
			if self.verbose and (step % self.print_interval == 0):
				print('step = '+str(step))
			En = None
			while En is None:
				rn, symbolsn = self.move(ro, symbolso)
				#import pdb; pdb.set_trace()
				En = self.get_energy(rn, symbolsn, step)

			if En < self.Emin:
				# new minimum found
				self.Emin = En
				self.symbolsmin = self.atoms.get_chemical_symbols()
				self.rmin = self.atoms.get_positions()
				self.call_observers()
			self.log(step, En, self.Emin)

			accept = np.exp((Eo - En) / self.kT) > np.random.uniform()
			if accept:
				ro = rn.copy()
				symbolso = symbolsn.copy()
				Eo = En

	def move(self, ro, symbolso):
		"""
		OVERRIDDEN METHOD: This method is designed to override the original method in BasinHopping in ASE.

		To keep in line with how BasinHopping works in ASE, you MUST have and return the following:
			* You must input ro which are the original positions of atoms in the cluster.
			* You must output the positions of atoms in the cluster.

		Therefore, to implement the element swap into the move method that swaps two of the positions of atoms in the cluster.

		"""
		return self.element_swap(ro, symbolso)

	def element_swap(self, ro, symbolso):
		"""
		This method is designed swap two atoms in the ASE basin hopping algorithm.

		To keep in line with how BasinHopping works in ASE, you MUST have and return the following:
			* You must input ro which are the original positions of atoms in the cluster.
			* You must output the positions of atoms in the cluster.

		Therefore, to implement the element swap into the move method that swaps two of the positions of atoms in the cluster.

		"""
		# Copy ro so that the original is kept by the algorthim. This is required in the coding for the ASE Basin Hopping algotithm
		rn = deepcopy(ro)
		symbolsn = list(symbolso)
		# Get a random atom and set it as the first atoms to wap
		atom_1_index = randint(0,len(self.atoms)-1)
		atom_1_symbol = symbolsn[atom_1_index]
		# Get all other indices in the cluster that have an element that is different to atom_1
		possible_atom_2_indices = [index for index in range(len(symbolsn)) if not symbolsn[index] == atom_1_symbol]
		atom_2_index = possible_atom_2_indices[randint(0,len(possible_atom_2_indices)-1)]
		atom_2_symbol = symbolsn[atom_2_index]
		if atom_1_symbol == atom_2_symbol:
			exit('Error')
		# Swap the positions of these two in ro (the original position of atoms in the cluster).
		#temp_position_swap_holder = deepcopy(rn[atom_1_index])
		#rn[atom_1_index] = deepcopy(rn[atom_2_index])
		#rn[atom_2_index] = temp_position_swap_holder
		# Swap the positions of these two in symbols (the original position of atoms in the cluster).
		#temp_position_swap_holder = symbolsn[atom_1_index]
		symbolsn[atom_1_index] = atom_2_symbol
		symbolsn[atom_2_index] = atom_1_symbol
		# return the new position of atoms (where two which correspeond to atoms with different elements have been swapped)
		#import pdb; pdb.set_trace()
		return rn, symbolsn
	
	def get_minimum(self):
		"""Return minimal energy and configuration."""
		atoms = self.atoms.copy()
		atoms.set_positions(self.rmin)
		atoms.set_chemical_symbols(self.symbolsmin)
		return self.Emin, atoms

	def get_energy(self, positions, symbols, step):
		"""Return the energy of the nearest local minimum."""
		#import pdb; pdb.set_trace()
		if np.sometrue(self.positions != positions) or np.sometrue(self.symbols != symbols):
			self.positions = positions
			self.symbols = symbols
			self.atoms.set_positions(positions)
			self.atoms.set_chemical_symbols(symbols)
			with self.optimizer(self.atoms,logfile=self.optimizer_logfile) as opt:
				opt.run(fmax=self.fmax)
			if self.lm_trajectory is not None:
				# This code has been added for Anna
				if (step >= self.start_recording_step) and ((step - self.start_recording_step) % self.step_recording_interval == 0):
					self.lm_trajectory.write(self.atoms)
					with open(self.recorded_steps_data_filename,'a') as step_recorded_dataTXT:
						step_recorded_dataTXT.write(str(self.recorded_steps_counter)+' ('+str(self.recorded_steps_counter-1)+') : '+str(step)+'\n')
						self.recorded_steps_counter += 1
					if self.verbose:
						if step == self.start_recording_step:
							print('Starting to record')
						print('recording step = '+str(step))
			self.energy = self.atoms.get_potential_energy()
		return self.energy