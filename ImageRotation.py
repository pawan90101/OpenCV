import cv2
import  numpy as np
img = cv2.imread('Imagewrite.png')

rotate_img = cv2.rotate(img,cv2.ROTATE_90_CLOCKWISE)

cv2.imshow('After Rotate Image',rotate_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
