import cmath as math
import random as random
import matplotlib.pyplot as plt
import numpy as np
from collections import Counter

N = 10000
lambd = 1
t = 10 #1 10 20 90
lambd_t = lambd * t
X = []
N_t = []
n_i = []
Poisson = []

for i in range(0, N):
    X.append(i)
    tV = 0
    count = 0
    while True:
        n = random.uniform(0,1)
        t_i = (-(math.log(n))/lambd)
        tV += t_i
        if np.greater_equal(tV, t):
            break
        count += 1
    
    n_i.append(count)
    
N_t = sorted(Counter(n_i).items())
N_t = list(zip(*N_t))
Ntx, Nty = N_t[0], np.array(N_t[1])/N

for k in Ntx:
    Poisson.append(((lambd_t**k)/(np.math.factorial(k))) * math.exp(-lambd_t))

print("lambda t = ", lambd_t)
print("avg dyst = ", np.average(n_i))

# plt.step(X, n_i, label="ni")
# fig, (ax0, ax1) = plt.subplots(2)

plt.plot(Ntx, Nty, label="t 10")
plt.plot(Ntx, Poisson, label="Poisson")

plt.legend()
plt.show()