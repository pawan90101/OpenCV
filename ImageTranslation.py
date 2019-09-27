import cv2
import  numpy as np
img = cv2.imread('IMG_20171018_134443.jpg')
resize = cv2.resize(img,(480,520),interpolation = cv2.INTER_AREA)#resize the image.

height,width = resize.shape[:2]
print(width)
print(height)

quarter_height,quarter_width = height/4,width/4
print(quarter_height)
print(quarter_width)
'''
trancelate matrix = |1 0 tx|
                    |0 1 ty|
'''
t = np.float32([[1,0,quarter_width],[0,1 , quarter_height]])
print(t)
img_tansformation = cv2.warpAffine(resize,t,(width,height))

cv2.imshow('Orignal Image',resize)
cv2.imshow('After transformation Image',img_tansformation)
cv2.waitKey(0)
cv2.destroyAllWindows()