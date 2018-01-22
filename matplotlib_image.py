import numpy as np
from scipy.misc import imread, imresize
import matplotlib.pyplot as plt

img = imread('/u01/images/white_cat.jpeg')
img_tinted = img * [1, 0.95, 0.9]

print 'image shape is '
print img.shape

# Show the original image
plt.subplot(1, 2, 1)
plt.imshow(img)

# Show the tinted image
plt.subplot(1, 2, 2)

# A slight gotcha with imshow is that it might give strange results
# if presented with data that is not uint8. To work around this, we
# explicitly cast the image to uint8 before displaying it.
plt.imshow(np.uint8(img_tinted))
plt.show()
