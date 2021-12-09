from ase.cluster.decahedron import Decahedron
from ase.io import write as ase_write

atoms = Decahedron('Au',p=5,q=2,r=0)
for index in range(30):
	atoms[index].symbol = 'Pd'

atoms.set_cell((100,100,100))
atoms.center()

ase_write('example.xyz',atoms)