import cv2
img = cv2.imread("IMG_20171018_134443.jpg")
resize = cv2.resize(img,(480,520),interpolation = cv2.INTER_AREA)#resize the image.
cv2.imshow('Output Image',resize)
print(resize.shape)
print("Height pixel values ",resize.shape[0])
print("Width pixel values ",resize.shape[1])
print("Layer is ",resize.shape[2])#this is RGB
cv2.waitKey(0)& 0xFF # if you are using 32 bit system then it should be cv2.waitKey(0)
cv2.destroyAllWindows()
