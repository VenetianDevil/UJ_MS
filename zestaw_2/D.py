import cmath as math
import random as random
import matplotlib.pyplot as plt
import numpy as np
from collections import Counter

N = 1000
users = 100
x = 0 #wybrany węzeł startowy
X = [x]
x_0 = []
x_1 = []
x_2 = []
x_3 = []
x_4 = []

for n in range(1, N):
    cout_logged_in = x
    cout_logged_out = 0
    # dla zalogowanych P wylogowania
    for i in range (0, x):
        P_move = random.uniform(0, 1)
        if(P_move < 1 - (.008*x + .1)):
            cout_logged_in = cout_logged_in - 1
    
    # dla niezalogowanch prawdopodobienstwo zalogowania
    for i in (range (0, users-x)):
        P_move = random.uniform(0, 1)
        if(P_move < .2):
            cout_logged_in = cout_logged_in + 1
    
    x = cout_logged_in
    # print("x = ", x)
    X.append(x)

    N_x = Counter(X)
    # print ("N_x =", N_x )
    x_0.append(N_x[18]/n)
    x_1.append(N_x[20]/n)
    x_2.append(N_x[25]/n)
    x_3.append(N_x[28]/n)
    x_4.append(N_x[30]/n)

N_x = Counter(X)
pi_i = []
for u_id in (range (0, users)):
    pi_i.append(N_x[u_id]/N)

print ("π_18 = ", x_0[-1])
print ("π_20 = ", x_1[-1])
print ("π_25 = ", x_2[-1])
print ("π_28 = ", x_3[-1])
print ("π_30 = ", x_4[-1])

fig, (ax0, ax1, ax2, ax3, ax4, ax5) = plt.subplots(6)
N_arr = list(range(1, N))
ax0.plot(N_arr, x_0)
ax1.plot(N_arr, x_1)
ax2.plot(N_arr, x_2)
ax3.plot(N_arr, x_3)
ax4.plot(N_arr, x_4)
N_arr = list(range(0, users))
ax5.plot(N_arr, pi_i)
plt.show()


# los < P_0  to do P_0
# jak los > P_0 ale los < P_0+P_1 to do P_1
# jak nie to do P_2