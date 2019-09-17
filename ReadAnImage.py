import cv2
img = cv2.imread('IMG_20171018_134443.jpg')#normal windows path D:\OpenCV  python path should be D:/OpenCV/IMG_20171018_134443.jpg
resize = cv2.resize(img,(480,520),interpolation = cv2.INTER_AREA)#resize the image.
cv2.imshow('Output Image',resize)
cv2.waitKey(0)
cv2.destroyAllWindows()