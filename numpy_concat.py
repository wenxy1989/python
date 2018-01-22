import numpy as np
from time import clock as now

a = np.arange(999990)
b = np.arange(999990)

time1 = now()
print 'now is : %d' % time1
c = np.append(a, b)
print 'c len is %d ' % len(c)
time2 = now()
print 'now is : %d' % time2
c = np.append(a, b)
print 'c len is %d ' % len(c)
print c
print 'numpy.append use time is  %d ' % (time2 - time1)

time3 = now()
print 'now is : %d' % time3
c = np.append(a, b)
d = np.concatenate((a, b), axis=0)
print 'd len is %d ' % len(d)
time4 = now()
print 'now is : %d' % time4
c = np.append(a, b)
print 'd len is %d ' % len(d)
print d
print 'numpy.concatenate use time is  %d ' % (time4 - time3)
