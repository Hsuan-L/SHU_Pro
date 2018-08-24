# PicEdit_forModule

# resize

from PIL import Image # Read image
from resizeimage import resizeimage # Resize image
import os # Using relative path

os.chdir(r'C:\Users\spect\OneDrive\桌面\School\SHU\2018_2\2018_1.5_GraduationPro\PicProcess')
# the direction of 0529_PicEdit.py, for the relative path


# image_resize.show();# show the image


# ========================================================================= #

# filter background

# references of Background Removal(33 - 58) =>https://pythonprogramming.net/grabcut-foreground-extraction-python-opencv-tutorial/ 

import cv2 # Read image, Grabcut, cvtColor, Canny, Bitwise_and
import numpy as np # Zeros, Where, Astype, Newaxis
import matplotlib.pyplot as plt # Show image

img = cv2.imread('./Images/Recycle/F3/IMG_1_1.png') # using opencv to read the image cause we need to use the Canny later

# cv2.imwrite('./Image/DoDoRo1.png', img) # save the image


mask = np.zeros(img.shape[:2],np.uint8)
# zeros => https://docs.scipy.org/doc/numpy/reference/generated/numpy.zeros.html

bgdModel = np.zeros((1,65),np.float64)
fgdModel = np.zeros((1,65),np.float64)

rect = (70, 30, 130, 340)# rect = (start_x, start_y, width, height).

cv2.grabCut(img,mask,rect,bgdModel,fgdModel,5,cv2.GC_INIT_WITH_RECT)
# Grabcut => https://docs.opencv.org/trunk/d8/d83/tutorial_py_grabcut.html
mask = np.where((mask==1)|(mask==2),0,1).astype('uint8') 
# where => https://docs.scipy.org/doc/numpy/reference/generated/numpy.where.html

img = img*mask[:,:,np.newaxis]
# newaxis => https://docs.scipy.org/doc/numpy-1.13.0/reference/arrays.indexing.html

plt.imshow(img),plt.colorbar(),plt.show() # show the image


# Reference of Canny(01 - 79) =>  https://pythonprogramming.net/canny-edge-detection-gradients-python-opencv-tutorial/


hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
# cvtColor => https://docs.opencv.org/3.0-beta/modules/imgproc/doc/miscellaneous_transformations.html


img = Image.fromarray(img, 'RGB')
img.save('./Images/final.png')


# image_import = Image.open('./Image/final.png')# import image using relative path

# width, height = image_import.width, image_import.height # get the width and height of the image


# image_resize = resizeimage.resize_cover(image_import, [width/40, height/40])# resize the image

# img = image_resize.convert('P') # convert the image to 8 bit('P'); convert to grayscale('LA')

# img.save('./Images/Result.png')# save the image