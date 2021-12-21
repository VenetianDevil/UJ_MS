import cmath as math
import random as random
import matplotlib.pyplot as plt
import numpy as np
from collections import Counter

N = 10000
lambd = 1
t = 90 #1 10 20 90
lambd_t = lambd * t
X = []
N_t = []
n_i = []
Poisson1 = []
Poisson2 = []
Poisson3 = []
group = []
P = [0.2, .5, .3]
groupIdx = [1, 2, 3]
gr1 = []
gr2 = []
gr3 = []

for i in range(0, N):
    tV = 0
    count = 0
    gr1.append(0)
    gr2.append(0)
    gr3.append(0)
    while True:
        n = random.uniform(0,1)
        t_i = (-(math.log(n))/lambd)
        tV += t_i
        if np.greater_equal(tV, t):
            break
        count += 1
    #     prawdopodobieństwo
        p_rand = random.uniform(0, 1)
        if p_rand < P[0]:
            gr1[i] += 1 # p1=0.2
        elif p_rand < P[0] + P[1]:
            gr2[i] += 1 # p2=0.5
        else:
            gr3[i] += 1 # p3=0.3


lambd_t_p1 = lambd_t * P[0]
lambd_t_p2 = lambd_t * P[1]
lambd_t_p3 = lambd_t * P[2]

gr1C = sorted(Counter(gr1).items())
gr1C = list(zip(*gr1C))
gr1Cx, gr1Cy = gr1C[0], np.array(gr1C[1])/N

gr2C = sorted(Counter(gr2).items())
gr2C = list(zip(*gr2C))
gr2Cx, gr2Cy = gr2C[0], np.array(gr2C[1])/N

gr3C = sorted(Counter(gr3).items())
gr3C = list(zip(*gr3C))
gr3Cx, gr3Cy = gr3C[0], np.array(gr3C[1])/N

for k1 in gr1Cx:
    Poisson1.append(((lambd_t_p1**k1)/(np.math.factorial(k1))) * math.exp(-lambd_t_p1))

for k2 in gr2Cx:
    Poisson2.append(((lambd_t_p2**k2)/(np.math.factorial(k2))) * math.exp(-lambd_t_p2))

for k3 in gr3Cx:
    Poisson3.append(((lambd_t_p3**k3)/(np.math.factorial(k3))) * math.exp(-lambd_t_p3))

print("lambda t p1 = ", lambd_t_p1)
print("avg dyst 1 = ", np.average(gr1))

print("lambda t p2 = ", lambd_t_p2)
print("avg dyst 2 = ", np.average(gr2))

print("lambda t p3 = ", lambd_t_p3)
print("avg dyst 3 = ", np.average(gr3))

fig, (ax0, ax1, ax2) = plt.subplots(3)
ax0.plot(gr1Cx, gr1Cy, label="group 1")
ax0.plot(gr1Cx, Poisson1, label="group 1 Poisson")
ax1.plot(gr2Cx, gr2Cy, label="group 2")
ax1.plot(gr2Cx, Poisson2, label="group 2 Poisson")
ax2.plot(gr3Cx, gr3Cy, label="group 3")
ax2.plot(gr3Cx, Poisson3, label="group 3 Poisson")

plt.legend()
plt.show()