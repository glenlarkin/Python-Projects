#import matplotlib
import numpy as np

a = np.arange(15).reshape(3, 5)
print(a)
print(a.shape)

b = np.array([6, 7, 8])
print(b)

# Array Creation

c = np.array([2, 3, 4])
print(c)
print(c.dtype)

d = np.array([1.2, 3.5, 5.1])
print(d.dtype)

zero = np.zeros((3, 4))
print(zero)

one = np.ones((2,3,4), dtype=np.int16)
print(one)

empty = np.empty((2,3))
print(empty)

np.arange(10, 30, 5)