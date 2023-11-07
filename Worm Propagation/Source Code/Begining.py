import networkx as nx
import matplotlib.pyplot as plt
import random
from networkx.algorithms.distance_measures import center

G = nx.gnm_random_graph(5000,0)

nodePos = nx.random_layout(G,None,2,5000)
print("nodePos : \n" , nodePos)


scale_pos = {}
for n in nodePos:
  arr = nodePos[n]
  x = arr[0]
  y = arr[1]
  scale_pos.update({n:(x*100,y*200)})
scale_pos

plt.figure(figsize=(50, 50))
nx.draw_networkx(G,scale_pos)
plt.grid()
plt.show()


plt.figure(figsize=(50, 50))
G1 = nx.random_geometric_graph(5000, 5, dim=2, pos=scale_pos)
nx.draw_networkx(G1)