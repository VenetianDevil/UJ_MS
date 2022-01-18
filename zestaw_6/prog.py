import cmath as math
import random as random
from re import A
import matplotlib.pyplot as plt
import numpy as np

N = 100
lambda_A = 6
lambda_D = 5

idx=[]
A_i = []
TD_i = []
D_i = []
D2_i = []
n_i = []
Ai = 0
R_i = [] # czas oczekiwania oczekiwanie

w_kolejce = []
wykonane = []

# przygotowanie kolejki
for i in range(N):
    idx.append(i)
    n = random.uniform(0, 1)
    tA_i = -math.log(n)/lambda_A
    tD_i = -math.log(n)/lambda_D
    Ai += tA_i

    TD_i.append(tD_i)
    n_i.append(n)

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
w_kolejce.append(0)
for i in range(1, N):
    while np.greater_equal(A_i[i], t_D):
        wyk += 1
        d += 1
        t_D = D_i[d]
        # print(i, " ", d)

    w_kolejce.append(i-wyk)

rest = N-wyk
q1_time = A_i.copy()
for i in range(rest):
    print(i, rest)
    q1_time.append(D_i[wyk+i])
    w_kolejce.append(rest-i-1)

D2_i = A_i.copy()
R2_i = []

print(A_i)
time = 0
time_unit = 0.01
q2_time = []
q2_tasks = []
while len([tD_i for tD_i in TD_i if np.greater(tD_i, 0)]) > 0:
    q2_time.append(time)
    tasks_in_server = 0
    tasks_we_care_about_idx = []

    for i in range(N):
        if np.greater_equal(time, A_i[i]) and np.greater(TD_i[i], 0):
            tasks_in_server = tasks_in_server + 1
            tasks_we_care_about_idx.append(i)

    q2_tasks.append(tasks_in_server)
    for task_id in tasks_we_care_about_idx:
        D2_i[task_id] = D2_i[task_id] + time_unit
        TD_i[task_id] = TD_i[task_id] - (time_unit / tasks_in_server)

    time = time + time_unit

finished_at_time_D = []
for task_id in range(N):
    finished_at_time_D.append(len([tD_i for tD_i in D2_i if np.greater_equal(D2_i[task_id], tD_i)]))
    R2_i.append(D2_i[task_id] - A_i[task_id])



fig, (ax1, ax2, ax3) = plt.subplots(3)

print(finished_at_time_D)
# print(len(idx)

ax1.plot(q1_time, w_kolejce, label="kol")
ax1.plot(q2_time, q2_tasks, label="kol")

ax2.bar(idx, R_i, label="oczekiwanie")
ax2.bar(idx, R2_i, label="oczekiwanie")

# ax1.scatter(A_i, idx, label="A_i")
# ax3.scatter(A_i, idx, label="A_i")
ax3.scatter(D_i, idx, label="D_i")
ax3.scatter(D2_i, finished_at_time_D, label="D_i")
# ax3.scatter(D2_i, idx, label="D_i")

# plt.legend()
plt.show()