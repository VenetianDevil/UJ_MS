import cmath as math
import random as random
import matplotlib.pyplot as plt
import numpy as np

class Player:
  def __init__(self, c, p):
    self.capital = c # a, b
    self.p = p

N = 100 #ilość rozgrywek
a_capital = []
r_pa = []
analitic = []

for i in range(50):
  a_capital.append(random.randint(1, 99))

a_capital.sort()

for j in range(50):
  pA = .5
  pB = 1 - pA
  a = a_capital[j]
  b = 100 - a
  A = Player(a, pA)
  B = Player(b, pB)
  C = Player(b, pB)
  D = Player(b, pB)

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

  # analityczny
  z = 100
  if (A.p != 0.5 and B.p != 0.5):
    analitic.append((((B.p / A.p)**a)-((B.p/A.p)**z))/(1 - ((B.p/A.p)**z)))
  if (A.p == 0.5 and B.p == 0.5):
    analitic.append(1 - (a/z) )
  # analitic.append(1-analize(A.p, B.p, B.capital))

  del A
  del B


# print(pa)
# print(r_pa)
plt.scatter(a_capital, r_pa)
plt.plot(a_capital, analitic, color="red")
plt.show()