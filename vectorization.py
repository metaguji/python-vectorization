import numpy as np
import time

sample_size = 1000000

a = np.random.rand(sample_size)
b = np.random.rand(sample_size)

tic = time.time()
c = np.dot(a,b)
toc = time.time()

print(c)
print("Vectorized version: " +  str(1000*(toc-tic)) + "ms")


c = 0
tic = time.time()

for i in range(sample_size):
    c += a[i]*b[i]

toc = time.time()

print(c)
print("For loop version: " +  str(1000*(toc-tic)) + "ms")
