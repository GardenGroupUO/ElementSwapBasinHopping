from ase.io import read as ase_read
from ase.io import write as ase_write
from ase.optimize.fire import FIRE
from ElementSwapBasinHopping_Program.ElementSwapBasinHopping import ElementSwapBasinHopping

class ElementSwapBasinHopping_Main:

	def __init__(self,input_name,output_name,calculator,max_no_to_steps,temperature=float('inf'),optimizer=FIRE,fmax=0.1,dr=0.0,logfile='global_optimisation_output.txt',trajectory='lowest.traj',optimizer_logfile='local_optimisation_output.txt',local_minima_trajectory='recorded_local_minima.traj',adjust_cm=True,start_recording_step=1,step_recording_interval=1,verbose=False,print_interval=1):
		self.input_name = input_name
		self.output_name = output_name
		self.calculator = calculator
		self.max_no_to_steps = max_no_to_steps
		self.temperature = temperature
		self.optimizer = optimizer
		self.fmax = fmax
		self.dr = dr
		self.logfile = logfile
		self.trajectory = trajectory
		self.optimizer_logfile = optimizer_logfile
		self.local_minima_trajectory = local_minima_trajectory
		self.adjust_cm = adjust_cm
		self.start_recording_step = start_recording_step
		self.step_recording_interval = step_recording_interval
		self.verbose = verbose
		self.print_interval = print_interval
		self.run()

	def run(self):
		self.import_cluster()
		self.run_ESBH()
		self.save_lowest_energetic_cluster()
		print('The Basin Hopping Algorithm will end.')

	def import_cluster(self):
		print('Importing '+str(self.input_name))
		self.cluster = ase_read(self.input_name)
		self.cluster.set_calculator(self.calculator)

	def run_ESBH(self):
		print('Running the Basin Hopping Algorithm')
		self.bh = ElementSwapBasinHopping(atoms=self.cluster,temperature=self.temperature,optimizer=self.optimizer,fmax=self.fmax,dr=self.dr,logfile=self.logfile,trajectory=self.trajectory,optimizer_logfile=self.optimizer_logfile,local_minima_trajectory=self.local_minima_trajectory,adjust_cm=self.adjust_cm,start_recording_step=self.start_recording_step,step_recording_interval=self.step_recording_interval,verbose=self.verbose,print_interval=self.print_interval)
		self.bh.run(self.max_no_to_steps)
		print('The Basin Hopping Algorithm has finished')

	def save_lowest_energetic_cluster(self):
		print('Writing the lowest energetic cluster as '+str(self.output_name))
		global_LES = ase_read(self.trajectory,index=-1)
		ase_write(self.output_name,global_LES)
