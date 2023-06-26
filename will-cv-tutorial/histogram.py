# Histograms visualize distribution of pixel intensities of image
import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread('will-cv-tutorial\Photos\cats 2.jpg')
blank = np.zeros(img.shape[:2], dtype='uint8')     # Needs to be the same size as the image
circle = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)       # Create mask

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
mask = cv.bitwise_and(gray, gray, mask=circle)
cv.imshow("mask",mask)

# # Grayscale histogram
# grayHist = cv.calcHist([gray], [0], mask, [256], [0,256])       # Creates histogram of pixel intensities in the specified mask

# plt.figure()
# plt.title("Grayscale Histogram")
# plt.xlabel("Bins")
# plt.ylabel("# of pixels")
# plt.plot(grayHist)
# plt.xlim([0,256])
# plt.show()


# Color histogram
plt.figure()
plt.title("Color Histogram")
plt.xlabel("Bins")
plt.ylabel("# of pixels")
colors = ('b','g','r')
for i,col in enumerate(colors):
    hist = cv.calcHist([img], [i], None, [256], [0,256])
    plt.plot(hist, color=col)
    plt.xlim([0,256])

plt.show()


cv.waitKey(0)
