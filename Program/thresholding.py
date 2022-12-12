import numpy as np
import cv2 as cv
import matplotlib as plt


img1 = cv.imread("gradient.jpeg",cv.COLOR_BGR2GRAY)

res = cv.resize(img1,None,fx=2,fy=2,interpolation=cv.INTER_CUBIC)



ret,resOne = cv.threshold(res,127,255,cv.THRESH_TOZERO_INV)

cv.imshow("Displaying Image",resOne)
cv.waitKey(0)
cv.destroyAllWindows()

