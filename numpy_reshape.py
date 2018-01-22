import numpy as np

count = 30

arr = np.arange(count)

print 'arr.shape : '
print arr.shape

print 'numpy reshape (3,5,2) start'
print '------------order is \'C\' : -----------'
print np.reshape(arr, (3, 5, 2), 'C')
print '------------order is \'F\' : -----------'
print np.reshape(arr, (3, 5, 2), 'F')
print '------------order is \'A\' : -----------'
print np.reshape(arr, (3, 5, 2), 'A')
a = arr.reshape(2, 3, 5)
print 'a is : '
print a
print 'a.reshape(a.shape[0],3 * 5)'
print a.shape[0]
print 'up is a.shape[0]'
print a.reshape(a.shape[0], 3 * 5)

print 'transpose (1,0,2) a is : '
print a.transpose(1, 0, 2)
