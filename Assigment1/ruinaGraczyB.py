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
a = 90
b = 10

for j in range(100):
  pA = pa[j]
  pB = 1 - pA
  A = Player(a, pA)
  B = Player(b, pB)

  # symulacja
  B_win = 0
  for game in range(N):
    A.capital = a
    B.capital = b
    while(A.capital != 0 and B.capital != 0):
      pGame = random.uniform(0, 1)
      if(A.p >= pGame):
        # print('a win')
        A.capital += 1
        B.capital -= 1
      if(A.p < pGame):
        # print ("b win")
        A.capital -= 1
        B.capital += 1

    if(A.capital == 0):
      B_win += 1

  # print(B_win)
  r_pa.append(B_win/N)
  # koniec symulacji

  del A
  del B


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