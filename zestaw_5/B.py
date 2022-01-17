import cmath as math
import random as random
import matplotlib.pyplot as plt
import numpy as np

N = 100
lambda_A = 10
lambda_D = 10
lambda_D2 = 6

idx=[]
A_i = []
D_i = []
A2_i = []
D2_i = []
Ai = 0
R_i = [] # czas oczekiwania oczekiwanie

w_kolejce = []
w_kolejce2 = []

tD2_i = 1/lambda_D2
for i in range(N):
    idx.append(i)
    n = random.uniform(0, 1)
    tA_i = -math.log(n)/lambda_A
    tD_i = -math.log(n)/lambda_D
    Ai += tA_i

    tA2_i = tD_i

    if(i==0):
        A_i.append(tA_i)
        D_i.append(tA_i + tD_i)
        A2_i.append(tA2_i)
        D2_i.append(tA2_i + tD2_i)
    else:
        A_i.append(A_i[i-1] + tA_i)
        D_i.append(np.maximum(D_i[i-1], Ai) + tD_i)
        A2_i.append(A2_i[i-1] + tA2_i)
        D2_i.append(np.maximum(D2_i[i-1], Ai) + tD2_i)

    #czas oczekiwania do 1 serwera + czas oczekiwania do 2 serwera
    R_i.append(D_i[i] - A_i[i] + D2_i[i] - A2_i[i])

# zliczanie zadan w kolejce do serwera 1 w zależności od czasu
d=0
t_D = D_i[d]
wyk=0
w_kolejce.append(0)
for i in range(1, N):
    while np.greater_equal(A_i[i],t_D):
        wyk+=1
        d+=1
        t_D=D_i[d]
        # print(i, " ", d)

    w_kolejce.append(i-wyk)

rest = N-wyk
time = A_i.copy()
for i in range(rest):
    print(i, rest)
    time.append(D_i[wyk+i])
    w_kolejce.append(rest-i-1)

# zliczanie zadan w kolejce do serwera 2 w zależności od czasu
d=0
t_D = D2_i[d]
wyk=0
w_kolejce2.append(0)
for i in range(1, N):
    print(i)
    while np.greater_equal(A2_i[i],t_D):
        wyk+=1
        d+=1
        t_D=D2_i[d]

    w_kolejce2.append(i-wyk)

rest = N-wyk
time2 = A2_i.copy()
for i in range(rest):
    print(i, rest)
    time2.append(D2_i[wyk+i])
    w_kolejce2.append(rest-i-1)

fig, (ax1, ax2, ax3) = plt.subplots(3)

ax1.scatter(A_i, idx, label="A_i")
ax1.scatter(D2_i, idx, label="D_i")

ax2.step(time, w_kolejce, label="kol 1")
ax2.step(time2, w_kolejce2, label="kol 2")

ax3.scatter(A_i, R_i, label="oczekiwanie")

# plt.legend()
plt.show()