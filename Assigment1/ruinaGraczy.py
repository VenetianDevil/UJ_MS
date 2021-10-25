import cmath as math
import random as random
import matplotlib.pyplot as plt
import numpy as np

class Player:
  def __init__(self, c, p):
    self.capital = c # a, b
    self.p = p

N = 10 #ilość kolejek
pa = []
r_pa = []

for i in range(100):
  pa.append(random.uniform(0, 1))

pa.sort()

for j in range(100):
  pA = pa[j]
  pB = 1 - pA

  A = Player(50, pA)
  B = Player(50, pB)

  r_pa.append((B.p - 1) * ((1 - ((B.p / A.p)**N))/(1-(B.p/A.p))))

  del A
  del B

print(pa)
print(r_pa)
plt.plot(pa, r_pa)
plt.show()