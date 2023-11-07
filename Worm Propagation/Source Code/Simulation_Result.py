import math,random
import numpy
import networkx as nx

import matplotlib.pyplot as plt
from networkx.algorithms.distance_measures import center
m = 50
m_time_slot_len ={}
time_slot_len = []
max_i = 0
for x in range(1,m+1):
  print(f"round {x} expriment")
  infected = []
  g2 = nx.gnm_random_graph(5000,0)
  nodePos = nx.random_layout(g2,None,2,5000)
  
  scale_pos = {}
  for n in nodePos:
    arr = nodePos[n]
    x = arr[0]
    y = arr[1]
    scale_pos.update({n:(x*100,y*200)})

  G1 = nx.random_geometric_graph(5000, 5, dim=2, pos=scale_pos)

   
  first_node = random.choice(center(G1)) 
  infected.append(first_node)
  nbr = list(nx.neighbors(G1,first_node))

  color_map = []
  coin_d = {}
  t_data = {}
  t_coin =[]
  time_infected = {}
  beta = 0.5
  for n in G1:
        coin = random.uniform(0,1)
        coin_d.update({n:coin})
        if n in nbr: 
          if coin <= beta:
             color_map.append("red")
             infected.append(n)
            
          else:
             color_map.append("green")  
        else : 
             color_map.append("green") 
  color_map[first_node] = "red"

  t_coin.append(coin_d)
  time_infected.update({1:[f"time slot{1} infected:",infected[:],len(infected[:])]})


  i = 2
  while len(infected) < len(G1):
    t_infected = infected[:]
    coin_d = {}
    for j in t_infected:
      nbr = list(nx.neighbors(G1,j))
      for n in nbr:
        if n not in t_infected and n not in infected:
          coin = random.uniform(0,1)
          coin_d.update({n:coin})
          if coin <= beta:
            color_map[n] = "red"
            infected.append(n)
    t_coin.append(coin_d)
    time_infected.update({i:[f"time slot{i} infected:",t_infected,len(t_infected[:])]})
    i += 1 
  time_infected.update({i:[f"final time slot infected:",infected,len(infected[:])]})
  if max_i < i:
    max_i = i
    print(max_i)
  for key in time_infected:
    time_slot_len.append(time_infected[key][2])
  m_time_slot_len.update({x:time_slot_len})
  time_slot_len = []  

new_m_time_slot = []

for key in m_time_slot_len:
  balance_list = [5000] * max_i
  for i,j in zip(range(0,max_i),range(0,len(m_time_slot_len[key]))):
    balance_list[i] = m_time_slot_len[key][j]
  new_m_time_slot.append(balance_list)  
print("bigest time slot:",max_i)
Beta1_mean = numpy.mean(new_m_time_slot,axis=0)
print(Beta1_mean)

import math,random
import numpy
import networkx as nx
import matplotlib.pyplot as plt
from networkx.algorithms.distance_measures import center
m = 50
m_time_slot_len ={}
time_slot_len = []
max_i = 0
for x in range(1,m+1):
  print(f"round {x} expriment")
  infected = []
  g2 = nx.gnm_random_graph(5000,0)
  nodePos = nx.random_layout(g2,None,2,5000)
  
  scale_pos = {}
  for n in nodePos:
    arr = nodePos[n]
    x = arr[0]
    y = arr[1]
    scale_pos.update({n:(x*100,y*200)})

  G1 = nx.random_geometric_graph(5000, 5, dim=2, pos=scale_pos)
 
  first_node = random.choice(center(G1))
  infected.append(first_node)
  nbr = list(nx.neighbors(G1,first_node))

  color_map = []
  coin_d = {}
  t_data = {}
  t_coin =[]
  time_infected = {}
  beta = 0.5
  for n in G1:
        coin = random.uniform(0,1)
        coin_d.update({n:coin})
        if n in nbr: 
          if coin <= beta:
             color_map.append("red")
             infected.append(n)

          else:
             color_map.append("green")  
        else : 
             color_map.append("green") 
  color_map[first_node] = "red"
  t_coin.append(coin_d)
  time_infected.update({1:[f"time slot{1} infected:",infected[:],len(infected[:])]})


  i = 2
  while len(infected) < len(G1):
    t_infected = infected[:]
    coin_d = {}
    for j in t_infected:
      nbr = list(nx.neighbors(G1,j))
      for n in nbr:
        if n not in t_infected and n not in infected:
          coin = random.uniform(0,1)
          coin_d.update({n:coin})
          if coin <= beta:
            color_map[n] = "red"
            infected.append(n)
    t_coin.append(coin_d)
    time_infected.update({i:[f"time slot{i} infected:",t_infected,len(t_infected[:])]})
    i += 1

  time_infected.update({i:[f"final time slot infected:",infected,len(infected[:])]})
  if max_i < i:
    max_i = i
    print(max_i)
  for key in time_infected:
    time_slot_len.append(time_infected[key][2])
  m_time_slot_len.update({x:time_slot_len})
  time_slot_len = []  

new_m_time_slot = []

for key in m_time_slot_len:
  balance_list = [5000] * max_i
  for i,j in zip(range(0,max_i),range(0,len(m_time_slot_len[key]))):
    balance_list[i] = m_time_slot_len[key][j]
  new_m_time_slot.append(balance_list)  

print("bigest time slot:",max_i)
Beta2_mean = numpy.mean(new_m_time_slot,axis=0)
print(Beta2_mean)

time_slot = list(range(0,33))
plt.plot(time_slot,Beta2_mean)
plt.show()

import math,random
import numpy
import networkx as nx
import matplotlib.pyplot as plt
from networkx.algorithms.distance_measures import center
m = 50
m_time_slot_len ={}
time_slot_len = []
max_i = 0
for x in range(1,m+1):
  print(f"round {x} expriment")
  infected = []
  g2 = nx.gnm_random_graph(5000,0)
  nodePos = nx.random_layout(g2,None,2,5000)
  
  scale_pos = {}
  for n in nodePos:
    arr = nodePos[n]
    x = arr[0]
    y = arr[1]
    scale_pos.update({n:(x*100,y*200)})

  
  G1 = nx.random_geometric_graph(5000, 5, dim=2, pos=scale_pos)

   
  first_node = random.choice(center(G1))
  infected.append(first_node)
  nbr = list(nx.neighbors(G1,first_node))

  color_map = []
  coin_d = {}
  t_data = {}
  t_coin =[]
  time_infected = {}
  beta = 0.8
  for n in G1:
        coin = random.uniform(0,1)
        coin_d.update({n:coin})
        if n in nbr: 
          if coin <= beta:
             color_map.append("red")
             infected.append(n)
            
            
          else:
             color_map.append("green")  
        else : 
             color_map.append("green") 
  color_map[first_node] = "red"

  t_coin.append(coin_d)
  time_infected.update({1:[f"time slot{1} infected:",infected[:],len(infected[:])]})


  i = 2
  while len(infected) < len(G1):
    t_infected = infected[:]
  
    coin_d = {}
  
    for j in t_infected:
      nbr = list(nx.neighbors(G1,j))
    
      for n in nbr:
        if n not in t_infected and n not in infected:
          coin = random.uniform(0,1)
          coin_d.update({n:coin})
          if coin <= beta:
            color_map[n] = "red"
          
            infected.append(n)
  
    t_coin.append(coin_d)
  
    time_infected.update({i:[f"time slot{i} infected:",t_infected,len(t_infected[:])]})
    i += 1
  
  time_infected.update({i:[f"final time slot infected:",infected,len(infected[:])]})
  if max_i < i:
    max_i = i
    print(max_i)
  for key in time_infected:
    time_slot_len.append(time_infected[key][2])
  m_time_slot_len.update({x:time_slot_len})
  time_slot_len = []  

new_m_time_slot = []

for key in m_time_slot_len:
  balance_list = [5000] * max_i
  for i,j in zip(range(0,max_i),range(0,len(m_time_slot_len[key]))):
    balance_list[i] = m_time_slot_len[key][j]
  new_m_time_slot.append(balance_list)  

print("bigest time slot:",max_i)
Beta3_mean = numpy.mean(new_m_time_slot,axis=0)
print(Beta3_mean)



Beta1_mean = [4.000e+00,4.000e+00,9.000e+00,2.900e+01,5.500e+01,1.020e+02,1.370e+02,
 1.740e+02,2.190e+02,2.610e+02,3.390e+02,4.140e+02,5.000e+02,5.780e+02,
 6.800e+02,7.880e+02,9.100e+02,1.028e+03,1.140e+03,1.287e+03,1.439e+03,
 1.597e+03,1.738e+03,1.886e+03,2.025e+03,2.176e+03,2.347e+03,2.531e+03,
 2.724e+03,2.905e+03,3.042e+03,3.179e+03,3.323e+03,3.454e+03,3.583e+03,
 3.721e+03,3.865e+03,4.015e+03,4.180e+03,4.343e+03,4.488e+03,4.610e+03,
 4.712e+03,4.804e+03,4.857e+03,4.903e+03,4.932e+03,4.957e+03,4.969e+03,
 4.983e+03,4.994e+03,4.998e+03,4.999e+03,4.999e+03,4.999e+03,4.999e+03,
 4.999e+03,4.999e+03,5.000e+03,5.000e+03,5.000e+03,5.000e+03,5.000e+03]

Beta2_mean = [8,8,45,108,176,282,395,530,714,916,1143,1410,
 1656,1895,2130,2372,2615,2841,3054,3258,3460,3683,3900,4118,
 4339,4577,4779,4896,4956,4987,5000,5000,5000]



Beta3_mean = [12,12,56,138,224,332,460,642,837,1087,1376,1639,1931,2224,
              2447,2677,2921,3133,3345,3566,3794,4021,4231,4442,4663,4853,4950,4990,5000,5000]

plt.grid(True)
plt.xlabel("Time")
plt.ylabel("Average number of infected nodes")
plt.title("Q3 simulation")

plt.plot(time_slot,Beta1_mean,"o",label="beta = 0.1 exp")
plt.plot(time_slot2,temp2,"^",label="beta = 0.5 exp")
plt.plot(time_slot3,temp3,"r*",label="beta = 0.8 exp")

plt.legend()
plt.show()



import math
import matplotlib.pyplot as plt

infected_q4_beta1 = []
infected_q4_beta2 = []
infected_q4_beta3 = []

N=5000
beta=0.1
density=0.25
r=5

time_slots_q4 = list(range(0, 62))


for t in time_slots_q4:
  
  e = - (2*beta*((math.sqrt(density*math.pi)*r)**3)*t)/math.sqrt(N)
  f2 = ((math.sqrt(N)-1)/(math.sqrt(N)+1))
  f = 2 / (1+f2*math.exp(e))
  p = (f - 1)**2
  result = N * p
  infected_q4_beta1.append(result)
  
beta=0.5
for t in time_slots_q4:
  e = - (2*beta*((math.sqrt(density*math.pi)*r)**3)*t)/math.sqrt(N)
  f2 = ((math.sqrt(N)-1)/(math.sqrt(N)+1))
  f = 2 / (1+f2*math.exp(e))
  p = (f - 1)**2
  result = N * p
  infected_q4_beta2.append(result)

beta=0.8
for t in time_slots_q4:
  e = - (2*beta*((math.sqrt(density*math.pi)*r)**3)*t)/math.sqrt(N)
  f2 = ((math.sqrt(N)-1)/(math.sqrt(N)+1))
  f = 2 / (1+f2*math.exp(e))
  p = (f - 1)**2
  result = N * p
  infected_q4_beta3.append(result)


plt.grid(True)

plt.xlabel('Time')
plt.ylabel('Number of infected nodes')
plt.title('Q4 model')



plt.plot(time_slots_q4, infected_q4_beta1, "c", label='beta=0.1 q4')
plt.plot(time_slots_q4, infected_q4_beta2, "m", label='beta=0.5 q4')
plt.plot(time_slots_q4, infected_q4_beta3, "k", label='beta=0.8 q4')

plt.legend()

plt.show()



import math
import matplotlib.pyplot as plt

infected_q5_beta1=[]
infected_q5_beta2=[]
infected_q5_beta3=[]

N=5000
beta=0.1
density=0.25
r=5

time_slots_q5 = list(range(1,63))
eta = 7.065 
for t in time_slots_q5:
  c = 2*math.sqrt(density*math.pi)*r
  e = -((beta*c*eta)/math.sqrt(N))
  d = 1+ ((math.sqrt(N)-1)/(math.sqrt(N)+1))*math.exp(e)*t
  f = 2/d
  result = N * (f-1)**2
  infected_q5_beta1.append(result)

beta=0.5
for t in time_slots_q5:
  c = 2*math.sqrt(density*math.pi)*r
  e = -((beta*c*eta)/math.sqrt(N))
  d = 1+ ((math.sqrt(N)-1)/(math.sqrt(N)+1))*math.exp(e)*t
  f = 2/d
  result = N * (f-1)**2
  infected_q5_beta2.append(result)

beta=0.8
for t in time_slots_q5:
  c = 2*math.sqrt(density*math.pi)*r
  e = -((beta*c*eta)/math.sqrt(N))
  d = 1+ ((math.sqrt(N)-1)/(math.sqrt(N)+1))*math.exp(e)*t
  f = 2/d
  result = N * (f-1)**2
  infected_q5_beta3.append(result)


plt.grid(True)

plt.xlabel('Time')
plt.ylabel('Number of infected nodes')
plt.title('Q5 model')

plt.plot(time_slots_q5, infected_q5_beta1, "b", label='beta=0.1')
plt.plot(time_slots_q5, infected_q5_beta2, "y", label='beta=0.5')
plt.plot(time_slots_q5, infected_q5_beta3, "g", label='beta=0.8')
plt.legend()
plt.show()

time_slot = list(range(0,63))
time_slot2 = list(range(0,63))
time_slot3 = list(range(0,63))

plt.grid(True)
plt.xlabel("Time")
plt.ylabel("Average number of infected nodes")
plt.title("All models and their related curves")

plt.plot(time_slot,Beta1_mean,"o",label="beta = 0.1 exp")
plt.plot(time_slot2,temp2,"^",label="beta = 0.5 exp")
plt.plot(time_slot3,temp3,"r*",label="beta = 0.8 exp")

plt.plot(time_slots_q4, infected_q4_beta1, "c", label='beta=0.1 q4')
plt.plot(time_slots_q4, infected_q4_beta2, "m", label='beta=0.5 q4')
plt.plot(time_slots_q4, infected_q4_beta3, "k", label='beta=0.8 q4')

plt.plot(time_slots_q5, infected_q5_beta1, "b", label='beta=0.1 q5')
plt.plot(time_slots_q5, infected_q5_beta2, "y", label='beta=0.5 q5')
plt.plot(time_slots_q5, infected_q5_beta3, "g", label='beta=0.8 q5')

plt.legend()
plt.show()

