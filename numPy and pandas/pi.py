from numpy import pi
import numpy as np

# (9 Numbers from 0 to 2)
test = np.linspace(0, 2, 9)
print(test)

# useful to evaluate function at lots of points
x = np.linspace(0, 2*pi, 100) 
f = np.sin(x)

print(x)
print(f)