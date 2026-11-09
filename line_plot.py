import matplotlib.pyplot as plt

x = [10, 20, 30, 40, 50]
y1 = [2, 4, 6, 8, 10]
y2 = [1, 3, 5, 7, 9]

plt.plot(x, y1, color='blue', linestyle='-', marker='o', label='Line 1')
plt.plot(x, y2, color='red', linestyle='--', marker='s', label='Line 2')

plt.title('2D Line Plot Basics')
plt.xlabel('X Axis - Values')
plt.ylabel('Y Axis - Measurements')
plt.legend()
plt.grid(True)
plt.show()