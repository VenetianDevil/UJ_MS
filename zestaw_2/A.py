import cmath as math
import random as random
import matplotlib.pyplot as plt
import numpy as np

P = np.matrix('0.64 0.32 0.04;0.4 0.5 0.1;0.25 0.5 0.25')
# print (P)

P_00 = [P[0, 0]]
P_01 = [P[0, 1]]
P_02 = [P[0, 2]]
P_10 = [P[1, 0]]
P_11 = [P[1, 1]]
P_12 = [P[1, 2]]
P_20 = [P[2, 0]]
P_21 = [P[2, 1]]
P_22 = [P[2, 2]]

N = 2
eps_exp = .0001
eps = np.matrix('1')

while (eps > eps_exp).all(1).all():
# while N <= 10:
    N = N + 1
    P_prev = P
    P = P@P
    P_00.append(P[0, 0])
    P_01.append(P[0, 1])
    P_02.append(P[0, 2])
    P_10.append(P[1, 0])
    P_11.append(P[1, 1])
    P_12.append(P[1, 2])
    P_20.append(P[2, 0])
    P_21.append(P[2, 1])
    P_22.append(P[2, 2])

    eps = np.absolute(np.subtract(P, P_prev))

print ("ε = ", eps)
X = list(range(1, N))
plt.plot(X, P_00, label="00")
plt.plot(X, P_01, label="01")
plt.plot(X, P_02, label="02")
plt.plot(X, P_10, label="10")
plt.plot(X, P_11, label="11")
plt.plot(X, P_12, label="12")
plt.plot(X, P_20, label="20")
plt.plot(X, P_21, label="21")
plt.plot(X, P_22, label="22")

print("P[j=0]: ", P_00[-1] )
print("P[j=1]: ", P_01[-1] )
print("P[j=2]: ", P_02[-1] )

plt.xlabel("N")
plt.ylabel("P_ij")
plt.legend()
plt.show()