# The information about the Organisms program

__name__    = 'ElementSwapBasinHopping'
__version__ = '1.5'
__author__  = 'Dr. Geoffrey Weal and Dr. Anna Garden'

import sys
if sys.version_info[0] == 2:
	toString = ''
	toString += '\n'
	toString += '================================================'+'\n'
	toString += 'This is the ElementSwapBasinHopping'+'\n'
	toString += 'Version: '+str(__version__)+'\n'
	toString += '\n'
	toString += 'The ElementSwapBasinHopping program requires Python3. You are attempting to execute this program in Python2.'+'\n'
	toString += 'Make sure you are running the ElementSwapBasinHopping program in Python3 and try again'+'\n'
	toString += 'This program will exit before beginning'+'\n'
	toString += '================================================'+'\n'
	raise ImportError(toString)
if sys.version_info[1] < 4:
	toString = ''
	toString += '\n'
	toString += '================================================'+'\n'
	toString += 'This is the ElementSwapBasinHopping'+'\n'
	toString += 'Version: '+str(__version__)+'\n'
	toString += '\n'
	toString += 'The ElementSwapBasinHopping program requires Python 3.4 or greater.'+'\n'
	toString += 'You are using Python '+str('.'.join(sys.version_info))
	toString += '\n'
	toString += 'Use a version of Python 3 that is greater or equal to Python 3.4.\n'
	toString += 'This program will exit before beginning'+'\n'
	toString += '================================================'+'\n'
	raise ImportError(toString)

# ------------------------------------------------------------------------------------------------------------------------

# A check for ASE
import importlib
python_version = 3.4

ase_spec = importlib.util.find_spec("ase")
found = ase_spec is not None

if not found:
	toString = ''
	toString += '\n'
	toString += '================================================'+'\n'
	toString += 'This is the ElementSwapBasinHopping'+'\n'
	toString += 'Version: '+str(__version__)+'\n'
	toString += '\n'
	toString += 'The ElementSwapBasinHopping program requires ASE.'+'\n'
	toString += '\n'
	toString += 'Install ase by typing the following into your terminal\n'
	toString += 'pip3 install --user --upgrade ase\n'
	toString += '\n'
	toString += 'This program will exit before beginning'+'\n'
	toString += '================================================'+'\n'
	raise ImportError(toString)	

packaging_spec = importlib.util.find_spec("packaging")
found = packaging_spec is not None

if not found:
	toString = ''
	toString += '\n'
	toString += '================================================'+'\n'
	toString += 'This is the ElementSwapBasinHopping Program'+'\n'
	toString += 'Version: '+str(__version__)+'\n'
	toString += '\n'
	toString += 'The ElementSwapBasinHopping requires the "packaging" program.'+'\n'
	toString += '\n'
	toString += ''+'\n'
	toString += 'Install packaging by typing the following into your terminal\n'
	toString += 'pip3 install --user --upgrade packaging\n'
	toString += '\n'
	toString += 'This program will exit before beginning'+'\n'
	toString += '================================================'+'\n'
	raise ImportError(toString)	

import ase
ase_version_minimum = '3.19.0'
from packaging import version
#from distutils.version import StrictVersion
#if StrictVersion(ase.__version__) < StrictVersion(ase_version_minimum):
if version.parse(ase.__version__) < version.parse(ase_version_minimum):
	toString = ''
	toString += '\n'
	toString += '================================================'+'\n'
	toString += 'This is the ElementSwapBasinHopping Program'+'\n'
	toString += 'Version: '+str(__version__)+'\n'
	toString += '\n'
	toString += 'The ElementSwapBasinHopping program requires ASE greater than or equal to '+str(ase_version_minimum)+'.'+'\n'
	toString += 'The current version of ASE you are using is '+str(ase.__version__)+'.'+'\n'
	toString += '\n'
	toString += 'Install ase by typing the following into your terminal\n'
	toString += 'pip3 install --user --upgrade ase\n'
	toString += '\n'
	toString += 'This program will exit before beginning'+'\n'
	toString += '================================================'+'\n'
	raise ImportError(toString)

# ------------------------------------------------------------------------------------------------------------------------

# A check for ASAP3

ase_spec = importlib.util.find_spec("asap3")
found = ase_spec is not None

if not found:
	toString = ''
	toString += '\n'
	toString += '================================================'+'\n'
	toString += 'This is the ElementSwapBasinHopping'+'\n'
	toString += 'Version: '+str(__version__)+'\n'
	toString += '\n'
	toString += 'The ElementSwapBasinHopping program requires ASAP3.'+'\n'
	toString += '\n'
	toString += 'Install asap3 by typing the following into your terminal\n'
	toString += 'pip3 install --user --upgrade asap3\n'
	toString += '\n'
	toString += 'This program will exit before beginning'+'\n'
	toString += '================================================'+'\n'
	raise ImportError(toString)	

import asap3
asap3_version_minimum = '3.11.10'
if not version.parse(asap3.__version__) == version.parse(asap3_version_minimum):
	toString = ''
	toString += '\n'
	toString += '================================================'+'\n'
	toString += 'This is the ElementSwapBasinHopping Program'+'\n'
	toString += 'Version: '+str(__version__)+'\n'
	toString += '\n'
	toString += 'The ElementSwapBasinHopping program requires ASAP3 equal to '+str(asap3_version_minimum)+'.'+'\n'
	toString += 'The current version of ASAP3 you are using is '+str(asap3.__version__)+'.'+'\n'
	toString += '\n'
	toString += 'Install ase by typing the following into your terminal\n'
	toString += 'pip3 install --user --upgrade asap3==3.11.10\n'
	toString += '\n'
	toString += 'This program will exit before beginning'+'\n'
	toString += '================================================'+'\n'
	raise ImportError(toString)

# ------------------------------------------------------------------------------------------------------------------------

__author_email__ = 'anna.garden@otago.ac.nz'
__license__ = 'GNU AFFERO GENERAL PUBLIC LICENSE'
__url__ = 'https://github.com/GardenGroupUO'
__doc__ = 'None'

from ElementSwapBasinHopping_Program.ElementSwapBasinHopping_Main import ElementSwapBasinHopping_Main
__all__ = ['ElementSwapBasinHopping_Main']

# ------------------------------------------------------------------------------------------------------------------------