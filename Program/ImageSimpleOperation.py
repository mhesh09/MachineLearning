import numpy as np
import cv2 as cv

img1 = cv.imread('messi.jpg')
img2 = cv.imread('starry_night.jpg')
img3 = cv.imread('messi2.jpg')


e1 = cv.getTickCount()
e2 = cv.getTickCount()
time = e2-e1
print(time,"\n")
print(cv.getTickFrequency(),"\n")
print(time/cv.getTickFrequency(),"\n")
# result = img1[153:144,54:116]
# img2[153:144,54:116]=result

# result = cv.add(img1,img3)
# result = cv.addWeighted(img1,0.7,img2,0.3,0)
# cv.imshow("New Display",img2)
# cv.waitKey(0)
# cv.destroyAllWindows()














# Way to find the points in images
# def draw_circle(event,x,y,flags,param):
#     if event == cv.EVENT_LBUTTONDBLCLK:
#         print(x,y)

# cv.namedWindow('image')
# cv.setMouseCallback('image',draw_circle)

# while True:
#     cv.imshow('image',img1)
#     if cv.waitKey(0):
#         break

#End of code to find the points in images
# cv.destroyAllWindows()