from ase import io
from ase.io import read
from ase.visualize import view


cu_facet = []
cu_edge = []
cu_vertex = []
cu_bulk = []


facet_total = 48 
edge_total = 24 
vertex_total = 24
bulk_total = 44  


#equil_composition=(1470/(196+1470))*100
equil_composition = 35/140*100
equil_comp =[]

num_steps = 33000  

facet_indices =  [6, 7, 9, 11, 15, 17, 20, 21, 24, 25, 26, 27, 32, 35, 39, 40, 46, 58, 63, 64, 72, 75, 79, 83, 87, 88, 91, 92, 93, 94, 96, 98, 106, 108, 111, 112, 113, 117, 119, 120, 121, 122, 123, 126, 129, 133, 136, 139]
edge_indices =  [4, 5, 8, 10, 16, 19, 22, 28, 33, 34, 41, 43, 66, 77, 78, 84, 90, 99, 110, 125, 127, 128, 134, 137]
vertex_indices =  [0, 1, 2, 3, 29, 30, 31, 44, 45, 59, 60, 62, 76, 80, 82, 85, 86, 95, 109, 124, 131, 132, 135, 138]
bulk_indices =  [12, 13, 14, 18, 23, 36, 37, 38, 42, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 61, 65, 67, 68, 69, 70, 71, 73, 74, 81, 89, 97, 100, 101, 102, 103, 104, 105, 107, 114, 115, 116, 118, 130]


for n in range(0,num_steps,100):

     slab=read('local_minima.traj',index=n)

     ##### Surfaces  #####

     cu_count_facet =0
     cu_count_edge = 0
     cu_count_vertex = 0
     cu_count_bulk = 0
#     pd_count_surface=0
     
     for index in facet_indices:
          if slab[index].symbol == 'Cu':
#               surface_indices.append(atom.index)
                cu_count_facet=cu_count_facet+1
#          elif slab[index].symbol == 'Pd':
#                pd_count_facet=pd_count_facet+1
     for index in edge_indices:
          if slab[index].symbol == 'Cu':
                cu_count_edge=cu_count_edge+1

     for index in vertex_indices:
          if slab[index].symbol == 'Cu':
                cu_count_vertex=cu_count_vertex+1

     for index in bulk_indices:
          if slab[index].symbol == 'Cu':
                cu_count_bulk=cu_count_bulk+1


     cu_facet.append(cu_count_facet/facet_total*100)
     cu_edge.append(cu_count_edge/edge_total*100)
     cu_vertex.append(cu_count_vertex/vertex_total*100)
     cu_bulk.append(cu_count_bulk/bulk_total*100)
#     cu_subsurface.append(cu_count_subsurface)
     equil_comp.append(equil_composition)

#print(cu_count_surface)
#print(pd_count_surface)


##print(surface_indices)
import matplotlib.pyplot as plt

plt.plot(equil_comp,'k',label="equil")
#plt.plot(pd_surface,'b',label="pd_surface")
plt.plot(cu_facet,'r',label="cu_facet")
plt.plot(cu_edge,'b',label="cu_edge")
plt.plot(cu_vertex,'g',label="cu_vertex")
plt.plot(cu_bulk,'m',label="cu_bulk")

#plt.plot(pd_subsurface,'tab:blue',label="subsurface")
plt.ylabel('% Cu composition')
plt.ylim([-10,110])
plt.legend()
plt.savefig('cu_25percent.png')
plt.show()
