
from asap3.Internal.BuiltinPotentials import Gupta
from ESBH_Program.ElementSwapBasinHopping_Main import ElementSwapBasinHopping_Main

input_name = 'example.xyz'
output_name = 'output_example.xyz'
max_no_to_steps = 5000
fmax = 0.1

start_recording_step = 1
step_recording_interval = 1

verbose=True
print_interval=1000

#Gupta_parameters = {'Pd': [10.867, 3.742, 0.1746, 1.718, 2.7485], 'Au': [10.229, 4.036, 0.2061, 1.79, 2.884], ('Au','Pd'): [10.54, 3.89, 0.19, 1.75, 2.816]}
#calculator = Gupta(Gupta_parameters, cutoff=1000, debug=True)

##
# error in gp above, trying rando versions
r0 = 4.07/(2.0**0.5)
Gupta_parameters = {'Au': [10.53, 4.30, 0.2197, 1.855, r0]}
Gupta_parameters = {'Au': [10.53, 4.30, 0.2197, 1.855, r0], 'Pd': [10.53, 4.30, 0.2197, 1.855, r0], ('Au','Pd'): [10.53, 4.30, 0.2197, 1.855, r0]}
calculator = Gupta(Gupta_parameters, cutoff=1000, debug=True)
##

ElementSwapBasinHopping_Main(input_name,output_name,calculator,max_no_to_steps,fmax=fmax,start_recording_step=start_recording_step,step_recording_interval=step_recording_interval,verbose=verbose,print_interval=print_interval)
