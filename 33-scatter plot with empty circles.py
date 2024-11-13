import matplotlib.pyplot as plt
import numpy as np

x = np.random.rand(50)
y = np.random.rand(50)

plt.scatter(x, y, facecolors='none', edgecolors='b')
plt.title('Scatter Plot with Empty Circles')
plt.show()
