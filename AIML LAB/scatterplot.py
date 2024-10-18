import numpy as np
import matplotlib.pyplot as plt
x = np.random.random(1000)
y = np.random.random(1000)
plt.scatter(x, y, s=5, c='b', marker='o', alpha=0.5)
plt.scatter(x, y)