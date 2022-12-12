import numpy as np
import cv2 as cv

img1 = cv.imread('messi.jpg')

another_img1 = cv.cvtColor(img1, cv.COLOR_BGR2HSV)

cv.imwrite("HSV_CONVERTED_IMAGE.jpg",another_img1)

lower_blue = np.array([110,50,50])
upper_blue = np.array([130,255,255])


mask = cv.inRange(another_img1,lower_blue,upper_blue)

result = cv.bitwise_and(img1,img1,mask=mask)
cv.imshow("Display Image",result)
cv.waitKey(0)
cv.destroyAllWindows()
