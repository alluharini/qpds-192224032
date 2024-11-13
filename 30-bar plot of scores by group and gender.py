import matplotlib.pyplot as plt
import numpy as np

men = [22, 30, 35, 35, 26]
women = [25, 32, 30, 35, 29]
labels = ['A', 'B', 'C', 'D', 'E']

x = np.arange(len(labels))
width = 0.35

fig, ax = plt.subplots()
ax.bar(x - width/2, men, width, label='Men')
ax.bar(x + width/2, women, width, label='Women')

ax.set_xlabel('Category')
ax.set_ylabel('Scores')
ax.set_title('Scores by category and gender')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()

plt.show()
