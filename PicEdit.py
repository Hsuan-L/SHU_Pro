import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('./Images/Recycle/F3/IMG_12_1.JPG')
mask = np.zeros(img.shape[:2],np.uint8)

bgdModel = np.zeros((1,65),np.float64)
fgdModel = np.zeros((1,65),np.float64)

rect = (1000, 300, 1000, 3500)

cv2.grabCut(img,mask,rect,bgdModel,fgdModel,5,cv2.GC_INIT_WITH_RECT)
mask2 = np.where((mask==0)|(mask==1),0,1).astype('uint8')
img = img*mask2[:,:,np.newaxis]

mask2 = np.where((mask==1)|(mask==2),0,1).astype('uint8')
img = img*mask2[:,:,np.newaxis]

plt.imshow(img)
plt.colorbar()
plt.show()