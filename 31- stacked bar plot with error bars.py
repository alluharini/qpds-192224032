import matplotlib.pyplot as plt
import numpy as np

x = np.arange(5)
men_means = [22, 30, 35, 35, 26]
women_means = [25, 32, 30, 35, 29]
men_std = [4, 3, 4, 1, 5]
women_std = [3, 5, 2, 3, 3]

plt.bar(x, men_means, yerr=men_std, label='Men')
plt.bar(x, women_means, yerr=women_std, bottom=men_means, label='Women')
plt.legend()
plt.show()
