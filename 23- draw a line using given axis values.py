import matplotlib.pyplot as plt
x = [1, 2, 3, 4, 5]
y = [2, 4, 1, 3, 5]
plt.plot(x, y, marker='o', color='green', label='Data Line')
plt.xlabel('X Axis Label')
plt.ylabel('Y Axis Label')
plt.title('Line Plot from Direct Data')
#plt.legend()
plt.show()
