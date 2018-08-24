# Date:07.14.2018
# Editer:Y.H
# This PYTHON file is used to ADD noise

import cv2 # opencv
import numpy as np # math method
from matplotlib import pyplot as plt # 2D plotting library
import os # operating system

os.chdir(r'C:\Users\spect\OneDrive\桌面\School\SHU\2018_2\2018_1.5_GraduationPro\PicProcess') # set main directory

# read images
Recycle = cv2.imread('./Images/Recycle/F1/IMG_1_1.jpg')
Recycle = cv2.cvtColor(Recycle, cv2.COLOR_BGR2RGB)
Noise = cv2.imread('./Images/Noise/noise1.png')

# add noise
New = cv2.addWeighted(Recycle, 1, Noise, 0.5, 0)
# New = Recycle + (Noise*0.3)

# debug
plt.imshow(New)
plt.title('New recycle image'), plt.xticks([]), plt.yticks([])
plt.show()

cv2.imwrite('./Images/Recycle/F4/IMG_1_1.jpg', New)



