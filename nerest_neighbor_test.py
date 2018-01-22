import NearestNeighbor
from CIFARImage import load_CIFAR10

Xtr, Ytr, Xte, Yte = load_CIFAR10('/u01/package/cifar-10-batches-py')
Xtr_rows = Xtr.reshape(Xtr.shape[0], 32 * 32 * 3)
Xte_rows = Xte.reshape(Xte.shape[0], 32 * 32 * 3)

nn = NearestNeighbor()
nn.train(Xtr_rows, Ytr)
Yte_predict = nn.predict(Xte_rows)

print 'accuracy : %f' % np.mean(Yte_predict == Yte)
