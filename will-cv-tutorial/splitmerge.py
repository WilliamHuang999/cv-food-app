import cv2 as cv
import numpy as np

img = cv.imread('will-cv-tutorial\Photos\park.jpg')
blank = np.zeros(img.shape[:2],dtype='uint8')

# Splitting color channels (will show as "grayscale" images)
b,g,r = cv.split(img)
cv.imshow("b",b)
cv.imshow("g",g)
cv.imshow("r",r)

# Show split color channels in color
blue = cv.merge([b, blank, blank])
green = cv.merge([blank, g, blank])
red = cv.merge([blank, blank, r])
cv.imshow("blue",blue)
cv.imshow("green",green)
cv.imshow("red",red)

# Merging color channels
merged = cv.merge([b,g,r])
cv.imshow("merged", merged)


cv.waitKey(0)