import cmath as math
import random as random
import matplotlib.pyplot as plt
import numpy as np

class Player:
  def __init__(self, c, p):
    self.capital = c # a, b
    self.p = p

N = 100 #ilość rozgrywek
pa = []
L_max = []

for i in range(50):
  pa.append(random.uniform(0, 1))

pa.sort()

for j in range(50):
  pA = pa[j]
  pB = 1 - pA
  a = 50
  b = 50
  A = Player(a, pA)
  B = Player(b, pB)
  L_all=[]

  # symulacja
  for game in range(N):
    A.capital = a
    B.capital = b
    L = 0
    while(A.capital != 0 and B.capital != 0):
      L = L+1
      pGame = random.uniform(0, 1)
      if(A.p >= pGame):
        # print('a win')
        A.capital += 1
        B.capital -= 1
      if(A.p < pGame):
        # print ("b win")
        A.capital -= 1
        B.capital += 1

    L_all.append(L)

  L_max.append(max(L_all))

  # koniec symulacji

  del A
  del B


# print(pa)
# print(r_pa)
plt.plot(pa, L_max, color="red")
plt.show()