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
