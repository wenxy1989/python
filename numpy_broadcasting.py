import numpy as np

x = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
v = np.array([1, 0, 1])
y = np.empty_like(x)

for i in range(4):
    y[i, :] = x[i, :] + v

print y
vv = np.tile(v, (4, 1))
print vv
y = x + vv
print y

print 'x + v : '
print x + v
