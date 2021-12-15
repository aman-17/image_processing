'''
from skimage import io
import numpy as np
from numpy import asarray
from PIL import Image
from skimage.io import imread
#from scipy.misc import imread

img = io.imread('result.jpeg', as_gray=True)

arr = np.array(img)
arr = np.arange(150).reshape(5, 10, 3)
x, y, z = arr.shape
indices = np.vstack(np.unravel_index(np.arange(x*y), (y, x))).T
x1=np.hstack((arr.reshape(x*y, z), indices))
print(x1)

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def rgb2gray(rgb):
    return np.dot(rgb[...,:3], [0.2989, 0.5870, 0.1140])

img = mpimg.imread('result.jpeg')     
gray = rgb2gray(img)    
plt.imshow(gray, cmap=plt.get_cmap('gray'), vmin=0, vmax=1)
plt.show()
'''
from PIL import Image
img = Image.open('T11.jpeg').convert('LA')
img.save('greyscale.png')
