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
r_pa = []
analitic = []

for i in range(100):
  pa.append(random.uniform(0, 1))

pa.sort()
a = 20
b = 20
c = 20
d = 20
e = 20

for j in range(100):
  pA = pa[j]
  pB = 1 - pA - random.uniform(0, (1 - pA))
  pC = 1 - pA - pB - random.uniform(0, (1 - pA - pB))
  pD = 1 - pA - pB - pC - random.uniform(0, (1 - pA - pB - pC))
  pE = 1 - pA - pB - pC - pD
  A = Player(a, pA)
  B = Player(b, pB)
  C = Player(c, pC)
  D = Player(d, pD)
  E = Player(e, pE)

  # symulacja
  A_lose = 0
  for game in range(N):
    A.capital = a
    B.capital = b
    C.capital = c
    D.capital = d
    E.capital = e
    while(A.capital != 0 and B.capital != 0 and C.capital != 0):
      pGame = random.uniform(0, 1)
      if(A.p >= pGame):
        # print('a win')
        A.capital += 4
        B.capital -= 1
        C.capital -= 1
        D.capital -= 1
        E.capital -= 1
      if(A.p < pGame):
        # print ("b win")
        A.capital -= 4
        B.capital += 1
        C.capital += 1
        D.capital += 1
        E.capital += 1

    if(A.capital == 0):
      A_lose += 1

  # print(A_lose)
  r_pa.append(A_lose/N)
  # koniec symulacji

  del A
  del B
  del C


# analityczny
N_a = 100
pa_analitic = []
step = 1/(N_a)
print(step)
for i in range(1, N_a+1):
  pa_analitic.append(0 + i*step)

print(pa_analitic)
pa_analitic.sort()
z = a + b
for i in range(N_a):
  p = pa_analitic[i]
  q = 1 - p
  if (p != 0.5 and q != 0.5):
    analitic.append((((q / p)**a)-((q/p)**z))/(1 - ((q/p)**z)))
  if (p == 0.5 and q == 0.5):
    analitic.append(1 - (a/z))


# print(pa)
# print(r_pa)
plt.scatter(pa, r_pa)
plt.plot(pa_analitic, analitic, color="red")
# plt.xlim([.4, .6])
plt.show()