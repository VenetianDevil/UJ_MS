#!/usr/bin/python3
# -*- coding: utf-8 -*-

import cmath as math
import random as random
import matplotlib.pyplot as plt
import numpy as np

u=0
s2=1
N = 5000
result = []
density = []

def f(y):
    return (1/(math.sqrt(2*math.pi*s2)))*math.exp(-((y-u)**2)/(2*s2))

def warSum(N, result, u):
    value = 0
    for i in range(1, N):
        value += (result[i]-u)**2
    return value

while len(result) < N:
    v1=random.uniform(-1, 1)
    v2=random.uniform(-1, 1)
    R2=(v1**2)+(v2**2)

    while 1<R2:
        v1=random.uniform(-1, 1)
        v2=random.uniform(-1, 1)    
        R2=(v1**2)+(v2**2)

    # print(v1, v2, R2)

    R = math.sqrt(R2)
    y1 = math.sqrt(-2*math.log(R2))*(v1/R)
    y2 = math.sqrt(-2*math.log(R2))*(v2/R)
    result.append(y1)
    if len(result) < N:
        result.append(y2)


# print(result)
result = np.sort_complex(result)

for y in result:
    density.append(f(y))

# plt.hist(result, normed=True, bins=20)
# plt.plot(result, density)
# plt.show()

avg = sum(result)/N
wariancja = 1/N * warSum(N, result, u)
# avg = math.avg(result)
print("avg = ", avg)
print("wariancja = ", wariancja)