#image resize using image pyramid
import cv2
import  numpy as np
img = cv2.imread('Imagewrite.png')
smaller = cv2.pyrDown(img)
bigger =  cv2.pyrUp(img)

cv2.imshow('Normal Image',img)
cv2.imshow('Smller Image',smaller)
cv2.imshow('Larger Image',bigger)
cv2.waitKey(0)
cv2.destroyAllWindows()