from ase.cluster.decahedron import Decahedron
from ase.io import write as ase_write

atoms = Decahedron('Au',p=5,q=2,r=0)
atoms[0].symbol = 'Pd'

ase_write('example.xyz',atoms)