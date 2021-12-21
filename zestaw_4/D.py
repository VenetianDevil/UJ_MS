import cmath as math
import random as random
import matplotlib.pyplot as plt
import numpy as np

N = 100

lamA = []
avgNodA = []
waitingA = []

lamD=[]
avgNodD = []
waitingD = []

r=[]
avgNodR = []
waitingR = []

def countAvgNWKolejce(kolejka):
    sum = kolejka[0]*A_i[0]
    time_sum = Ai
    for i in range(1, N):
        sum += kolejka[i]*(A_i[i]-A_i[i-1])

    return sum/time_sum

for lambda_A in range(2, 30):
    lambda_D = 15

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

    avg_n_w_kolejce = countAvgNWKolejce(w_kolejce)

    lamA.append(lambda_A)
    avgNodA.append(avg_n_w_kolejce)
    waitingA.append(np.average(R_i))

for lambda_D in range(2, 30):
    lambda_A = 15

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

    avg_n_w_kolejce = countAvgNWKolejce(w_kolejce)

    lamD.append(lambda_D)
    avgNodD.append(avg_n_w_kolejce)
    waitingD.append(np.average(R_i))

for i in range(0, 30):
    lambda_A = random.uniform(2, 30)
    lambda_D = random.uniform(2, 30)
    r_i = lambda_A/lambda_D

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

    avg_n_w_kolejce = countAvgNWKolejce(w_kolejce)

    r.append(r_i)
    avgNodR.append(avg_n_w_kolejce)
    waitingR.append(np.average(R_i))

fig, ((ax1, ax2), (ax3, ax4), (ax5, ax6)) = plt.subplots(3, 2)

ax1.scatter(lamA, avgNodA, label="liczba zadań w zależności od λA")
ax2.scatter(lamA, waitingA, label="czas oczekiwania w zależności od λA")

ax3.scatter(lamD, avgNodD, label="liczba zadań w zależności od λD")
ax4.scatter(lamD, waitingD, label="czas oczekiwania w zależności od λD")

ax5.scatter(r, avgNodR, label="liczba zadań w zależności od λA/λD")
ax6.scatter(r, waitingR, label="czas oczekiwania w zależności od λA/λD")

# plt.legend()
plt.show()