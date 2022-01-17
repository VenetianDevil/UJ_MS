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
Ai = 0

A2_i = []
D2_i = []
Ai2 = 0

queue_A = []
queue_n = []
R_i = [] # czas oczekiwania oczekiwanie

w_kolejce = []

A = 0
for i in range(N):
    idx.append(i)
    n = random.uniform(0, 1)
    tA_i = -math.log(n)/lambda_A
    A += tA_i
    queue_A.append(A)
    queue_n.append(n)

wyk_s1=0
wyk_s2=0
s1_free = True
s2_free = True

D_total = []
i1 = 0
idx1 = []
idx2 = []
i2 = 0
for i in range(0, N):
    tA_i = queue_A[i]
    n = queue_n[i]

    if s1_free == False and np.greater(tA_i,D_i[wyk_s1]): #zwalniam 1 serwer jesli zadanie w nim ma czas zakocznenia wczesniejszy niz to zadanie co teraz przyszło
        s1_free = True
        wyk_s1 += 1

    if s2_free == False and np.greater(tA_i,D2_i[wyk_s2]): #zwalniam 2 serwer jesli zadanie w nim ma czas zakocznenia wczesniejszy niz to zadanie co teraz przyszło
        s2_free = True
        wyk_s2 += 1

    if s1_free == False and s2_free == False: #jesli nadal oba sa zajete
        if np.greater(D_i[wyk_s1],D2_i[wyk_s2]): #zwalniam ten serwer ktory wczesniej skonczy zadanie
            s2_free = True
            wyk_s2 += 1
        else:
            s1_free = True
            wyk_s1 += 1

    if s1_free == True:
        idx1.append(i)
        i1+=1
        tD_i = -math.log(n)/lambda_D
        s1_free = False
        A_i.append(tA_i)
        if(wyk_s1==0):
            D_i.append(tA_i + tD_i)
            D_total.append(tA_i + tD_i)
        else:
            D_i.append(np.maximum(D_i[wyk_s1-1], tA_i) + tD_i)
            D_total.append(np.maximum(D_i[wyk_s1-1], tA_i) + tD_i)
        #czas oczekiwania do 1 serwera + czas oczekiwania do 2 serwera
        R_i.append(D_i[wyk_s1] - A_i[wyk_s1])
    elif s2_free == True:
        idx2.append(i)
        i2+=1
        s2_free = False
        tD2_i = -math.log(n)/lambda_D2
        A2_i.append(tA_i)
        if(wyk_s2==0):
            D2_i.append(tA_i + tD2_i)
            D_total.append(tA_i + tD2_i)
        else:
            D2_i.append(np.maximum(D2_i[wyk_s2-1], tA_i) + tD2_i)
            D_total.append(np.maximum(D2_i[wyk_s2-1], tA_i) + tD2_i)

        #czas oczekiwania do 1 serwera + czas oczekiwania do 2 serwera
        R_i.append(D2_i[wyk_s2] - A2_i[wyk_s2])

# zliczanie zadan w kolejce w zależności od czasu
d=0
t_D = D_total[d]
wyk=0
w_kolejce.append(0)
for i in range(1, N):
    while np.greater_equal(queue_A[i],t_D):
        wyk+=1
        d+=1
        t_D=D_total[d]
        # print(i, " ", d)

    w_kolejce.append(i-wyk)

rest = N-wyk
time = queue_A.copy()
for i in range(rest):
    print(i, rest)
    time.append(D_total[wyk+i])
    w_kolejce.append(rest-i-1)

fig, (ax1, ax2, ax3) = plt.subplots(3)

# ax1.scatter(A_i, idx1, label="A_i")
# ax1.scatter(D_i, idx1, label="D_i")

# ax1.scatter(A2_i, idx2, label="A_i")
# ax1.scatter(D2_i, idx2, label="D2_i")

ax1.scatter(queue_A, idx, label="A_i")
ax1.scatter(D_total, idx, label="D1_i")

ax2.step(time, w_kolejce, label="kol 1")

ax3.bar(queue_A, R_i, label="oczekiwanie")

# plt.legend()
plt.show()