import numpy as np

a = np.array([[1, 2],
              [3, 4]])

b = np.array([[5, 6],
              [7, 8]])

print("Matrix A:")
print(a)

print("Matrix B:")
print(b)

print("Addition:")
print(a + b)

print("Multiplication:")
print(np.dot(a, b))
