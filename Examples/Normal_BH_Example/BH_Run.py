from ase.io import read as ase_read
from ase.io import write as ase_write
from asap3.Internal.BuiltinPotentials import Gupta
from ase.units import kB
from ase.optimize.fire import FIRE
from ase.optimize.basin import BasinHopping

max_no_to_steps = 50
cluster = ase_read('example.xyz')
Gupta_parameters = {'Pd': [10.867, 3.742, 0.1746, 1.718, 2.7485], 'Au': [10.229, 4.036, 0.2061, 1.79, 2.884], ('Au','Pd'): [10.54, 3.89, 0.19, 1.75, 2.816]}
cluster.set_calculator(Gupta(Gupta_parameters, cutoff=1000, debug=True))

fmax = 0.1
bh = BasinHopping(atoms=cluster,         # the system to optimize
                  temperature=100 * kB, # 'temperature' to overcome barriers
                  dr=1.0,               # maximal stepwidth
                  optimizer=FIRE,      # optimizer to find local minima
                  fmax=fmax,             # maximal force for the optimizer
                  optimizer_logfile='output.txt', # output for local optimisations
                  )
bh.run(max_no_to_steps)

from ase.visualize import view
view(cluster)
