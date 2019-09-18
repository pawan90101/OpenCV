#HSV stands for Hue Saturation Value
# Hue: 0-180, Saturation: 0-255, Value: 0-255 as same as RGB(all are 0-255)
import cv2
img = cv2.imread('Imagewrite.png')
img_HSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
cv2.imshow("HSV Imge",img_HSV)
cv2.imshow('Hue Channel',img_HSV[:,:,0])
cv2.imshow('Saturation Channel',img_HSV[:,:,1])
cv2.imshow('Value Channel',img_HSV[:,:,2])
cv2.waitKey(0)
cv2.destroyAllWindows()
