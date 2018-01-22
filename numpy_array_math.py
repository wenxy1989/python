import numpy as np

x = np.array([[1, 2], [3, 4]], dtype=np.float64)
y = np.array([[5, 6], [7, 8]], dtype=np.float64)

print 'x + y : '
print x + y
print np.add(x, y)

print 'x - y : '
print x - y
print np.subtract(x, y)

print 'x * y : '
print x * y
print np.multiply(x, y)
print np.dot(x, y)

print 'x / y : '
print x / y
print np.divide(x, y)

print 'sqrt x : '
print np.sqrt(x)
