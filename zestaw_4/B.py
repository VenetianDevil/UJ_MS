import cmath as math
import random as random
import matplotlib.pyplot as plt
import numpy as np

N = 1000
lambda_A = 2
lambda_D = 3

idx = []
A_i = []
D_i = []
Ai = 0
R_i = [] # czas oczekiwania oczekiwanie

w_kolejce = []
wykonane = []

for i in range(N):
    idx.append(i)
    n = random.uniform(0, 1)
    tA_i = -math.log(n)/lambda_A
    tD_i = -math.log(n)/lambda_D
    Ai += tA_i

    if(i==0):
        A_i.append(tA_i)
        D_i.append(tA_i + tD_i)
    else:
        A_i.append(A_i[i-1] + tA_i)
        D_i.append(np.maximum(D_i[i-1], Ai) + tD_i)

    R_i.append(D_i[i] - A_i[i])

# zliczanie zadan w kolejce w zależności od czasu
d=0
t_D = D_i[d]
wyk=0
w_kolejce.append(1)
for i in range(1, N):
    while np.greater(A_i[i],t_D):
        wyk+=1
        d+=1
        t_D=D_i[d]
        # print(i, " ", d)

    w_kolejce.append(i+1-wyk)

def countAvgNWKolejce(kolejka):
    sum = kolejka[0]*A_i[0]
    time_sum = Ai
    for i in range(1, N):
        sum += kolejka[i]*(A_i[i]-A_i[i-1])

    return sum/time_sum

avg_n_w_kolejce = countAvgNWKolejce(w_kolejce)

print("E(R)λA = ",  np.average(R_i)*lambda_A)
print("E(n) = ", avg_n_w_kolejce)

fig, (ax1, ax2, ax3) = plt.subplots(3)

ax1.scatter(A_i, idx, label="A_i")
ax1.scatter(D_i, idx, label="D_i")

ax2.scatter(A_i, w_kolejce, label="kol")

ax3.scatter(A_i, R_i, label="oczekiwanie")

# plt.legend()
plt.show()