import numpy as np
import cv2

blackbox=np.zeros([500,500])
print(blackbox)

blackbox[200:300,200:300]=255

cv2.imshow("display",blackbox)
cv2.waitKey(0)