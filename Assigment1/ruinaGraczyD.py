import cmath as math
import random as random
import matplotlib.pyplot as plt
import numpy as np

class Player:
  def __init__(self, c, p):
    self.capital = c # a, b
    self.p = p

N = 1000 #ilość gier
a_capital = []
r_pa = []
analitic = []
L_all = [] #ilosci rozgrywek

for i in range(N):
  a_capital.append(random.randint(1, 99))

a_capital.sort()

for j in range(N):
  pA = .2
  pB = 1 - pA
  a = 50
  b = 50
  A = Player(a, pA)
  B = Player(b, pB)

  # symulacja
  # for game in range(N):
  L = 0
  while(A.capital != 0 and B.capital != 0):
    L= L+1
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
  # koniec symulacji

  del A
  del B

print("avg = ", sum(L_all)/N)
# print(pa)
# print(r_pa)
plt.hist(L_all)
plt.show()