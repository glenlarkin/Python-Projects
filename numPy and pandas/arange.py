import numpy as np

# 1D Array
a = np.arange(6)
print(a)

# 2D Array
b = np.arange(12).reshape(4,3)
print(b)

# 3D Array
c = np.arange(24).reshape(2,3,4)
print(c)

print(np.arange(10000))

print(np.arange(10000).reshape(100,100))


rg = np.random.default_rng(1)
d = rg.random((2,3))
print(d)
print(d.sum())
print(d.min())
print(d.max())