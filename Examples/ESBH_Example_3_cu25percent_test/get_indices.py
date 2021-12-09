from ase import io
from ase.io import read
from ase.visualize import view


#cu_surface = []
#pd_surface = []

#layer_total = 196

#equil_comp=[]

#num_steps = 250000

facet_indices = []
edge_indices = []
vertex_indices = []
bulk_indices = []

surface = read('labelled_cluster.xyz')
     
for atom in surface:
   if atom.symbol == 'Cu':
         facet_indices.append(atom.index)
   elif atom.symbol == 'Au':
         edge_indices.append(atom.index)
   elif atom.symbol == 'Ag':
         vertex_indices.append(atom.index)
   elif atom.symbol == 'Pd':
         bulk_indices.append(atom.index)

print(f"facet_indices =  {facet_indices}")
print(f"edge_indices =  {edge_indices}")
print(f"vertex_indices =  {vertex_indices}")
print(f"bulk_indices =  {bulk_indices}")

#import matplotlib.pyplot as plt

#plt.plot(equil_comp,'k',label="equil")
#plt.plot(pd_surface,'b',label="pd_surface")
#plt.plot(cu_surface,'r',label="cu_surface")
#plt.plot(pd_subsurface,'tab:blue',label="subsurface")
#plt.ylabel('# Pd atoms in layer')
#plt.ylim([0,100])
#plt.legend()
#plt.show()
