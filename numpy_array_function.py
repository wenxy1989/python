import numpy as np

x = np.array([[1, 2], [3, 4]])
y = np.array([[5, 6], [7, 8]])

v = np.array([9, 10])
w = np.array([11, 12])

print 'x : '
print x
print 'x.T : '
print x.T


print 'v : '
print v
print 'v.T : '
print v.T

print 'w : '
print w

print 'v * w'
print v.dot(w)
print np.dot(v, w)

print 'x * y'
print x.dot(v)
print np.dot(x, v)

print 'x * y'
print x.dot(y)
print np.dot(x, y)

print 'sum x : '
print np.sum(x)
print np.sum(x, axis=0)
print np.sum(x, axis=1)
