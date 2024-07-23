import random
import numpy as np

random.seed(0)

x1: list = [random.uniform(-4, 0) for i in range(10)]
y1: list = [random.uniform(0, 6) for i in range(10)]

x2: list = [random.uniform(0, 6) for i in range(10)]
y2: list = [random.uniform(-4, 0) for i in range(10)]

print(min(x1), max(y1))
print()
print(min(x2), max(y2))


np.random.seed(0)

x3 = np.random.uniform(-4, 0)
y3 = np.random.uniform(0, 6)

print(x3)
print(y3)