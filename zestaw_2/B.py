import cmath as math
import random as random
import matplotlib.pyplot as plt
import numpy as np
from collections import Counter

P = np.matrix('0.64 0.32 0.04;0.4 0.5 0.1;0.25 0.5 0.25')
# print (P)

N = 1000
x = 2 #wybrany węzeł startowy
X = [x]
x_0 = []
x_1 = []
x_2 = []

for n in range(2, N):
    P_move = random.uniform(0, 1)
    if(P_move < P[x, 0]):
        x = 0
    elif(P_move < P[x, 0] + P[x, 1]):
        x = 1
    else:
        x = 2

    X.append(x)
    N_x = Counter(X)
    # print ("N_x =", N_x )
    x_0.append(N_x[0]/n)
    x_1.append(N_x[1]/n)
    x_2.append(N_x[2]/n)

print ("π_0 = ", x_0[-1])
print ("π_1 = ", x_1[-1])
print ("π_2 = ", x_2[-1])
print ("P^N = ", np.power(P, N))

N_arr = list(range(2, N))
fig, (ax0, ax1, ax2) = plt.subplots(3)
plt.xlabel("N")
plt.ylabel("x")
ax0.plot(N_arr, x_0)
ax1.plot(N_arr, x_1)
ax2.plot(N_arr, x_2)
plt.show()
