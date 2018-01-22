import numpy as np

a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
b = a[:2, 1:3]

print a
print b
print a[0, 1]
b[0, 0] = 77
print a[0, 1]
row_r1 = a[1, :]
row_r2 = a[1:2, :]
print row_r1, row_r1.shape
print row_r2, row_r2.shape

cos_r1 = a[:, 1]
cos_r2 = a[:, 1:2]

print cos_r1, cos_r1.shape
print cos_r2, cos_r2.shape
