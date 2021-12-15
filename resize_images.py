'''from PIL import Image
import glob
import os

# new folder path (may need to alter for Windows OS)
# change path to your path
path = '/home/aman17/resize' #the path where to save resized images
# create new folder
if not os.path.exists(path):
    os.makedirs(path)

# loop over existing images and resize
# change path to your path
for filename in glob.glob('/home/aman17/Object-Detector/t-shirts/IMG-20201102-WA0053.jpg'): #path of raw images
    img = Image.open(filename).resize((512,512))
    # save resized images to new folder with existing filename
    img.save('{}{}{}'.format(path,'/',os.path.split(filename)[1]))

print('yes')

from PIL import Image
import glob
import os

# new folder path (may need to alter for Windows OS)
# change path to your path
ORI_PATH = '/home/aman17/Programs/AppyHub/tsh/0.jpg'
NEW_SIZE = 1024

PATH = '/home/aman17/Programs/AppyHub/1024_tsh' #the path where to save resized images
count=0
# create new folder
#if not os.path.exists(PATH):
#    os.makedirs(PATH)

# loop over existing images and resize
# change path to your path
for filename in glob.glob(ORI_PATH+'**/*.jpg'): #path of raw images with is subdirectory
    img = Image.open(filename).resize((NEW_SIZE,NEW_SIZE))
    
    # get the original location and find its subdir
    loc = os.path.split(filename)[0]
    #subdir = loc.split('\\')[1]
    
    # assembly with its full new directory
    fullnew_subdir = PATH+"/"
    name = os.path.split(filename)[1]
    
    # check if the subdir is already created or not
    if not os.path.exists(fullnew_subdir):
        os.makedirs(fullnew_subdir)
    
    # save resized images to new folder with existing filename
    img.save('{}{}{}'.format(fullnew_subdir,'/',name))
    count=count+1
    print(count)
#print('yes')
'''
from PIL import Image
import glob
import os

# new folder path (may need to alter for Windows OS)
# change path to your path
path = '/home/aman17/Programs/AppyHub/1024_tsh' #the path where to save resized images
# create new folder
if not os.path.exists(path):
    os.makedirs(path)

# loop over existing images and resize
# change path to your path
for filename in glob.glob('/home/aman17/Programs/AppyHub/tsh/*.jpg'): #path of raw images
    img = Image.open(filename).resize((1024,1024))
    # save resized images to new folder with existing filename
    img.save('{}{}{}'.format(path,'/',os.path.split(filename)[1]))
