import matplotlib.pyplot as plt
import numpy as np

x = np.random.rand(50)
y = np.random.rand(50)

plt.scatter(x, y, color='b')
plt.title('Scatter graph with Random Distribution')
plt.show()
