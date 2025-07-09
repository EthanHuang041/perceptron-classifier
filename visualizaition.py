import matplotlib.pyplot as plt
import load_data 

data, labels = load_data.load_data_from_txt()

with open("parameter.txt", "r") as f:
    line = f.readline().strip().split()
    w = [float(line[0]), float(line[1])]
    b = float(line[2])

pos_x = [x[0] for x, y in zip(data, labels) if y == 1]
pos_y = [x[1] for x, y in zip(data, labels) if y == 1]
neg_x = [x[0] for x, y in zip(data, labels) if y == -1]
neg_y = [x[1] for x, y in zip(data, labels) if y == -1]

plt.scatter(pos_x, pos_y, c='blue', label='Positive (1)')
plt.scatter(neg_x, neg_y, c='red', label='Negative (-1)')

import numpy as np
x_vals = np.linspace(min(pos_x + neg_x), max(pos_x + neg_x), 100)
y_vals = -(w[0] * x_vals + b) / w[1]
plt.plot(x_vals, y_vals, 'g-', label='Model Boundary')


plt.xlabel("x1")
plt.ylabel("x2")
plt.title("Perceptron Classification Boundary")
plt.legend()
plt.grid()
plt.show()
