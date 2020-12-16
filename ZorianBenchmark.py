# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 08:33:09 2020

@author: zorian
"""

 # Import numpy to handle matrices
import numpy as np

# Generates random 2 by 3 matrix
matrix = np.random.rand(2,3)
matrix

import pandas as pd
df = pd.DataFrame(matrix)
df

df.iloc[1, 2]
matrix[1, 2]

# 1D random number between 0 and 1
matrix = np.random.randint(0, 2)

matrix = np.random.randint(0, 2, size=(2,3))

matrix = np.random.randint(0, 2, size= (20,30))

# Computes average times




import time
time.time()




repeats = 5

#---------------------------
def benchmatrixrand():
    start1 = time.time()
    matrix = np.random.randint(0, 2, size=(10000,100000))
    end1 = time.time()
    time1 = end1-start1
    return time1


def benchmatrix():
    start1 = time.time()
    matrix = np.full( shape=(30500,100000), fill_value = 110706)
    end1 = time.time()
    time1 = end1-start1
    return time1

def benchpicalc():
    start1 = time.time()
    pi = 0
    for n in range(10000000):
      pi += ((-1)**n) / (2*n + 1)
    print(4 * pi)
    end1 = time.time()
    time1 = end1-start1
    return time1




def runbenchmark(benchmark, repeats, label):
    times = []
    for n in range(repeats) :
        times.append(benchmark())
        print(f'Time {len(times)} = {times[-1]}')
        
    #make average time and award points.
    AvgTime = (sum(times)/len(times))
    print(AvgTime)
    points = (100 - (AvgTime*AvgTime))
    print(f'You got {points} points on {label}! (Higher is better)')

runbenchmark(benchmatrixrand, repeats, "Random Matrix Benchmark")
runbenchmark(benchmatrix, repeats, "Set Matrix Benchmark")
runbenchmark(benchpicalc, repeats, "Pi Calculation Benchmark")



