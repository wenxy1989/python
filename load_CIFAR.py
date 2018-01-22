# -*- coding: utf-8 -*-
"""
Created on Tue Dec 20 13:37:50 2016

@author: HDU
"""

import numpy as np
'''
输入训练集及测试集
'''


def unpickle(file):
    import cPickle
    fo = open(file, 'rb')
    dict = cPickle.load(fo)
    fo.close()
    return dict


def load_CIFAR10(file):
    # get the training data
    dataTrain = []
    labelTrain = []
    for i in range(1, 6):
        dic = unpickle(file + "/data_batch_" + str(i))
        for item in dic["data"]:
            dataTrain.append(item)
        for item in dic["labels"]:
            labelTrain.append(item)

# get test data
    dataTest = []
    labelTest = []
    dic = unpickle(file + "/test_batch")
    for item in dic["data"]:
        dataTest.append(item)
    for item in dic["labels"]:
        labelTest.append(item)
    return (dataTrain, labelTrain, dataTest, labelTest)


datatr, labeltr, datate, labelte = load_CIFAR10(
    "/u01/package/cifar-10-batches-py")

# print "Xte:%d" %(len(dataTest))
# print "Yte:%d" %(len(labelTest))
Xtr = np.asarray(datatr)
Xte = np.asarray(datate)
Ytr = np.asarray(labeltr)
Yte = np.asarray(labelte)
# Xtr_rows becomes 50000 x 3072
Xtr_rows = Xtr.reshape(Xtr.shape[0], 32 * 32 * 3)
# Xte_rows becomes 10000 x 3072
Xte_rows = Xte.reshape(Xte.shape[0], 32 * 32 * 3)
print Xtr.shape
print Xte.shape
print Ytr.shape
print Yte.shape
print type(Xtr)


class NearestNeighbor(object):
    def __init__(self):
        pass

    def train(self, X, y):
        """ X is N x D where each row is an example. Y is 1-dimension of size N """
        # the nearest neighbor classifier simply remembers all the training data
        self.Xtr = X
        self.ytr = y

    def predict(self, X):
        """ X is N x D where each row is an example we wish to predict label for """
        num_test = X.shape[0]
        # lets make sure that the output type matches the input type
        Ypred = np.zeros(num_test, dtype=self.ytr.dtype)
        num = 0

        # loop over all test rows
        for i in xrange(num_test):
            # find the nearest training image to the i'th test image
            # using the L1 distance (sum of absolute value differences)
            distances = np.sum(np.abs(self.Xtr - X[i, :]), axis=1)
            # get the index with smallest distance
            min_index = np.argmin(distances)
            # predict the label of the nearest example
            Ypred[i] = self.ytr[min_index]
            num = num + 1
            if num % 10 == 0:
                print "num=", num / 10

        return Ypred


nn = NearestNeighbor()  # create a Nearest Neighbor classifier class
# train the classifier on the training images and labels
nn.train(Xtr_rows, Ytr)
Yte_predict = nn.predict(Xte_rows)  # predict labels on the test images
# and now print the classification accuracy, which is the average number
# of examples that are correctly predicted (i.e. label matches)
print 'accuracy: %f' % (np.mean(Yte_predict == Yte))
