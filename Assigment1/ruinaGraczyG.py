import cmath as math
import random as random
import matplotlib.pyplot as plt
import numpy as np

class Player:
  def __init__(self, c, p):
    self.capital = c # a, b
    self.p = p

fig, (ax1, ax2) = plt.subplots(2)
N = 5 #ilość rozgrywek
pa = []
L_max = []

for j in range(N):
  pA = .8
  pB = 1 - pA
  a = 50
  b = 50
  A = Player(a, pA)
  B = Player(b, pB)

  # symulacja
  L = 0
  aCapital =[]
  aWin = []
  win = 0
  while(A.capital != 0 and B.capital != 0):
    pGame = random.uniform(0, 1)
    if(A.p >= pGame):
      win = win + 1
      # print('a win')
      A.capital += 1
      B.capital -= 1
    if(A.p < pGame):
      win = win -1
      # print ("b win")
      A.capital -= 1
      B.capital += 1
    aCapital.append(A.capital)
    aWin.append(win)
    L = L+1

  ax1.step(list(range(0, L)), aCapital, color=np.random.rand(3,))
  ax2.plot(list(range(0, L)), aWin, color=np.random.rand(3,))

  # koniec symulacji

  del A
  del B


plt.show()
