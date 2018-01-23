import numpy as np
from NearestNeighbor import NearestNeighbor
from load_CIFAR import load_CIFAR10

Xtr, Ytr, Xte, Yte = load_CIFAR10('/u01/package/cifar-10-batches-py')
# print 'load_CIFAR10 result type and shape'
# print 'train type x is %s y is %s , test type x is %s y is %s' % (type(Xtr), type(Ytr), type(Xte), type(Yte))
# print 'train shape x is %s y is %s , test shape x is %s y is %s' % (Xtr.shape, Ytr.shape, Xte.shape, Yte.shape)

Xtr = np.asarray(Xtr)
Ytr = np.asarray(Ytr)
Xte = np.asarray(Xte)
Yte = np.asarray(Yte)
Xtr_rows = Xtr.reshape(Xtr.shape[0], 32 * 32 * 3)
Xte_rows = Xte.reshape(Xte.shape[0], 32 * 32 * 3)
# print 'train x shape is %s' % (Xtr_rows.shape)
# print Xtr_rows.shape
# print 'test x shape is %s' % (Xte_rows.shape)
# print Xte_rows.shape

dis_row = Xtr_rows - Xtr_rows[0, :]
distance = np.sum(np.abs(dis_row), axis=1)
print distance

nn = NearestNeighbor()
nn.train(Xtr_rows, Ytr)
Yte_predict = nn.predict(Xte_rows)

print 'accuracy : %f' % np.mean(Yte_predict == Yte)
