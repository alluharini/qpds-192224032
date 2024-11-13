import matplotlib.pyplot as plt
import numpy as np

x = np.random.rand(50)
y = np.random.rand(50)
sizes = np.random.rand(50) * 1000  # Random sizes for the balls

plt.scatter(x, y, s=sizes, color='b', alpha=0.5)
plt.title('Scatter Plot with Random Ball Sizes')
plt.show()
