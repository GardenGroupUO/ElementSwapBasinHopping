
from asap3.Internal.BuiltinPotentials import Gupta
from ESBH_Program.ElementSwapBasinHopping_Main import ElementSwapBasinHopping_Main
import ase.units as units
#import os
#os.remove('global_optimisation_output.txt')
#os.remove('local_minima.traj')
#os.remove('local_optimisation_output.txt')
#os.remove('lowest.traj')

input_name = 'cluster.xyz'
output_name = 'output_cluster.xyz'
max_no_to_steps = 30000
fmax = 0.1

start_recording_step = 15000 
step_recording_interval = 100

verbose=True
print_interval=1000

#Mottet Parameters		
#Gupta_parameters = {'Cu': [9.184, 1.880, 0.115, 1.802, 2.55],'Pd': [7.352, 2.384, 0.358, 3.722, 2.7506],('Cu','Pd'): [7.200, 2.867, 0.208, 2.600, 2.65]} ##Mottet
#calculator = Gupta(Gupta_parameters, cutoff=(2.0)**(0.5), debug=True) 
#Cleri Parameters
Gupta_parameters = {'Cu': [10.960,2.278,0.0855,1.224,2.556],'Pd': [10.867,3.742,0.1746,1.718,2.7485],('Cu','Pd'): [10.9135,3.01,0.13005,1.471,2.65225]} ##Cleri
calculator = Gupta(Gupta_parameters, cutoff=2.236, debug=True) ##Cleri
#Panizon Negreiros Parameters
#Gupta_parameters = {'Cu': [10.653,2.49,0.092585,1.2437,2.556],'Pd': [17, 2.09, 0.0501, 1.1924, 2.7506],('Cu','Pd'): [13.8265,2.29,0.0713425,1.21805,2.6533]} ##Panizon + Negreiros
#calculator = Gupta(Gupta_parameters, cutoff=(3.0)**(0.5), debug=True) 

ElementSwapBasinHopping_Main(input_name,output_name,calculator,max_no_to_steps,temperature=500*units.kB,fmax=fmax,start_recording_step=start_recording_step,step_recording_interval=step_recording_interval,verbose=verbose,print_interval=print_interval)
