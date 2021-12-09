import ase.cluster
import ase.cluster.icosahedron
import ase.cluster.octahedron
import ase.cluster.decahedron
from ase.visualize import view

cluster = ase.cluster.octahedron.Octahedron('Pd',6,1)
print(len(cluster))
view(cluster)
