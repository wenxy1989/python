import cPickle
import numpy as np
import matplotlib.pyplot as plt


def unpickle(file):
    with open(file, 'rb') as fo:
        dict = cPickle.load(fo)
    return dict


def decodeImage(array):
    if len(array) != 3072:
        return null
    red_channel = array[:1024]
    green_channel = array[1024:2048]
    blue_channel = array[2048:]
    #print 'channel length red is %s , green is %s ,blue is %s' % (len(red_channel), len(green_channel), len(blue_channel))
    point_arr = np.array([red_channel, green_channel, blue_channel]).T
    image_arr = np.zeros((32, 32, 3))
    for i in range(32):
        image_row = point_arr[i * 32:i * 32 + 32]
        image_arr[i] = image_row
    return image_arr


source = unpickle('/u01/package/cifar-10-batches-py/data_batch_1')
print type(source)
for i in source:
    print '%s is %s length is : %f' % (i, type(source[i]), len(source[i]))

print source['data'].shape
print len(source['labels'])
print source['batch_label']
print len(source['filenames'])

plots = [5, 20]
for rownum in range(plots[0]):
    for colnum in range(plots[1]):
        index = colnum + (rownum) * plots[1]
        #plt.subplot(plots[0], plots[1], rownum + 1,colnum + 1)
        plt.subplot(plots[0], plots[1], index +1)
        print 'row %d clumn %d index %d ' % (rownum+1, colnum+1, index)
        img = decodeImage(source['data'][index])
        plt.imshow(np.uint8(img))

plt.show()
