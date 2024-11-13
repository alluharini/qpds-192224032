import matplotlib.pyplot as plt

math_marks = [88, 92, 80, 89, 100, 80, 60, 100, 80, 34]
science_marks = [35, 79, 79, 48, 100, 88, 32, 45, 20, 30]
marks_range = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

plt.scatter(marks_range, math_marks, color='r', label='Math Marks')
plt.scatter(marks_range, science_marks, color='g', label='Science Marks')

plt.xlabel('Marks Range')
plt.ylabel('Marks')
plt.title('Math vs Science Marks')
plt.legend()
plt.show()
