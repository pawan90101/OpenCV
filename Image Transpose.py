import cv2
import  numpy as np
img = cv2.imread('Imagewrite.png')
rotated_img = cv2.transpose(img)

cv2.imshow('Normal Image',img)
cv2.imshow('After Rotate Image',rotated_img)
cv2.waitKey(0)
cv2.destroyAllWindows()