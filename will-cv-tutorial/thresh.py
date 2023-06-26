import cv2 as cv

img = cv.imread('will-cv-tutorial\Photos\cats.jpg')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# Simple thresholding
threshold, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY)      # Use cv.THRESH_BINARY_INV for inverse threshold
cv.imshow("Simple threshold", thresh)

# Adaptive thresholding --> automatrically finds optimal threshold for the specific image
adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 3)
cv.imshow("Adaptive threshold", adaptive_thresh)


cv.waitKey(0)
