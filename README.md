# ElementSwapBasinHopping: A Basin Hopping program for element swapping

[![PyPI - Python Version](https://img.shields.io/badge/Python-3.6%20%7C%203.7%20%7C%203.8%20%7C%203.9-blue)](https://docs.python.org/3/)
<!-- [![Citation](https://img.shields.io/badge/Citation-click%20here-green.svg)](https://dx.doi.org/10.1021/acs.jcim.0c01128) -->
[![GitHub release (latest by date)](https://img.shields.io/github/v/release/GardenGroupUO/ElementSwapBasinHopping)](https://github.com/GardenGroupUO/ElementSwapBasinHopping)
[![Licence](https://img.shields.io/github/license/GardenGroupUO/ElementSwapBasinHopping)](https://www.gnu.org/licenses/agpl-3.0.en.html)
[![LGTM Grade](https://img.shields.io/lgtm/grade/python/github/GardenGroupUO/ElementSwapBasinHopping)](https://lgtm.com/projects/g/GardenGroupUO/ElementSwapBasinHopping/context:python)

Authors: Geoffrey R. Weal, Caitlin A. Casey-Stevens and Dr. Anna L. Garden (University of Otago, Dunedin, New Zealand)

Group page: https://blogs.otago.ac.nz/annagarden/

Page to cite with work from: *XXX*; XXX; 

## What is this Program?

ElementSwapBasinHopping is a program that performs a element swapping basin hopping algorithm. This program utilises modules from the Atomic Simulation Environment (ASE) and As Soon As Possible (ASAP3) packages. 

## Pre-Requisite Programs

ElementSwapBasinHopping requires the following programs before it can be used:

* Atomic Simulation Environment (ASE): https://wiki.fysik.dtu.dk/ase/
* ASAP3: https://wiki.fysik.dtu.dk/asap
* Packaging

The easiest way to install these is through pip. Type the following two lines into the terminal: 

.. code-block:: bash

	pip3 install --upgrade --user ase packaging
	pip3 install --upgrade --user asap3==3.11.10

See https://pip.pypa.io/en/stable/installation/ if you do not have pip installed on your computer. 

## Installation

To install this program on your computer, pop open your terminal, ``cd`` to where you want to place this program on your computer, and clone the program to your computer by typing the following into your terminal:

```
git clone https://github.com/GardenGroupUO/ElementSwapBasinHopping
```

If you do not have ``git`` installed on your computer, see https://www.atlassian.com/git/tutorials/install-git

Once you have done this, type ``pwd`` into the terminal and copy this path into your ``~\.bashrc`` in the following format:

```bash
#####################################################################################
# These lines will allow python to locate this program on your computer.
export PATH_TO_ElementSwapBasinHopping='/PATH_GIVEN_BY_THE_PWD_COMMAND/ElementSwapBasinHopping'
export PYTHONPATH="$PATH_TO_ElementSwapBasinHopping":$PYTHONPATH
#####################################################################################
```

This will allow your computer to run this program through your terminal on python3.

## How to Run ElementSwapBasinHopping

An example of the script used to run this program is given below, called ``Run_ESBH.py``.

As well as this script, you also need the cluster that you wish to perform the element swapping basin hopping algorithm, and give it's name to the ``input_name`` variable. For example, in th escript below, this file is called ``cluster.xyz``, and ``input_name = 'cluster.xyz'`` in the script,

```python
from asap3.Internal.BuiltinPotentials import Gupta
from ElementSwapBasinHopping_Program import ElementSwapBasinHopping_Main
import ase.units as units

input_name = 'cluster.xyz'
output_name = 'output_cluster.xyz'
max_no_to_steps = 30000
fmax = 0.1

start_recording_step = 15000
step_recording_interval = 100

verbose=True
print_interval=1000

#Cleri Parameters
Gupta_parameters = {'Cu': [10.960,2.278,0.0855,1.224,2.556],'Pd': [10.867,3.742,0.1746,1.718,2.7485],('Cu','Pd'): [10.9135,3.01,0.13005,1.471,2.65225]} ##Cleri
calculator = Gupta(Gupta_parameters, cutoff=2.236, debug=True) ##Cleri

ElementSwapBasinHopping_Main(input_name,output_name,calculator,max_no_to_steps,temperature=500*units.kB,fmax=fmax,start_recording_step=start_recording_step,step_recording_interval=step_recording_interval,verbose=verbose,print_interval=print_interval)
```

## What will ElementSwapBasinHopping do when you run the ``Run_ESBH.py`` script?

When you execute this program by running ``python3 Run_ESBH.py`` in the terminal, ElementSwapBasinHopping will perform the basin hopping algorithm based on swapping elements in the cluster. 

## Output files that are created by ElementSwapBasinHopping

``output_cluster.xyz``: The lowest energy cluster located using the element swapping basin hopping algorithm
``lowest.traj``: All the lowest energy clusters that were obtained as the element swapping basin hopping algorithm was performed. 

``recorded_local_minima.traj``: The lowest cluster that were obtained during the ESBH, based on the values given for ``start_recording_step`` and ``step_recording_interval``. All local minima obtained by the ESBH will be recorded into this ``traj`` file if ``start_recording_step=1`` and ``step_recording_interval=1``.
``steps_recorded_into_recorded_local_minima_traj.txt``: These are the local minima of steps that are recorded into the ``recorded_local_minima.traj`` file. 

``global_optimisation_output.txt``: Output text file from the basin hopping algorithm, including minimised energy.
``local_optimisation_output.txt``: Output text file of the local minimisations during each basin hopping step.

## About

<div align="center">

| Python        | [![PyPI - Python Version](https://img.shields.io/badge/Python-3.6%20%7C%203.7%20%7C%203.8%20%7C%203.9-blue)](https://docs.python.org/3/) | 
|:-------------:|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------:|
| Repositories  | [![GitHub release (latest by date)](https://img.shields.io/github/v/release/GardenGroupUO/ElementSwapBasinHopping)](https://github.com/GardenGroupUO/ElementSwapBasinHopping) |
| Documentation | [![GitHub release (latest by date)](https://img.shields.io/github/v/release/GardenGroupUO/ElementSwapBasinHopping)](https://github.com/GardenGroupUO/ElementSwapBasinHopping) | 
| Citation      | [![Citation](https://img.shields.io/badge/Citation-click%20here-green.svg)](https://dx.doi.org/10.1021/acs.jcim.0c01128) | 
| Tests         | [![LGTM Grade](https://img.shields.io/lgtm/grade/python/github/GardenGroupUO/ElementSwapBasinHopping)](https://lgtm.com/projects/g/GardenGroupUO/ElementSwapBasinHopping/context:python)
| License       | [![Licence](https://img.shields.io/github/license/GardenGroupUO/ElementSwapBasinHopping)](https://www.gnu.org/licenses/agpl-3.0.en.html) |
| Authors       | Geoffrey R. Weal, Caitlin A. Casey-Stevens, and Dr. Anna L. Garden |
| Group Website | https://blogs.otago.ac.nz/annagarden/ |

</div>
