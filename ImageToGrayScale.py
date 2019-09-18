import cv2
import numpy as np
def Image2GrayScale1(img):
    grayScale_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow("GrayScaleFirstMethod", grayScale_img)


img = cv2.imread('Imagewrite.png',0)#method two is is option 0
cv2.imshow('Orignal',img)
cv2.waitKey(0) &  0xFF
#Image2GrayScale1(img)
#cv2.waitKey(0) &  0xFF
cv2.destroyAllWindows()
