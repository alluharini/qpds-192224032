import matplotlib.pyplot as plt
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
plt.plot(x, y, label='Line Plot', color='blue')
plt.xlabel('X Axis Label')
plt.ylabel('Y Axis Label')
plt.title('Simple Line Plot')
plt.legend()
plt.show()
