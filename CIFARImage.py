import os
import cPickle as pickle
import numpy as np


def unpickle(filename):
    fo = open(filename, 'rb')
    dict = pickle.load(fo)
    fo.close()
    return dict


def load_CIFAR_batch(filename):
    """ load single batch of cifar """
    datadict = unpickle(filename)
    X = datadict['data']
    Y = datadict['labels']
    X = X.reshape(10000, 3, 32, 32).transpose(0, 2, 3, 1).astype("float")
    Y = np.array(Y)
    return X, Y


def load_CIFAR10(ROOT):
    """ load all of cifar """
    xs = []
    ys = []
    for b in range(1, 6):
        f = os.path.join(ROOT, 'data_batch_%d' % (b, ))
        X, Y = load_CIFAR_batch(f)
        xs.append(X)
        ys.append(Y)
    Xtr = np.concatenate(xs)
    Ytr = np.concatenate(ys)
    del X, Y
    Xte, Yte = load_CIFAR_batch(os.path.join(ROOT, 'test_batch'))
    return Xtr, Ytr, Xte, Yte


#load_CIFAR10('/u01/package/cifar-10-batches-py')
