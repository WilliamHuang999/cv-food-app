import cv2 as cv

img = cv.imread('will-cv-tutorial\Photos\cats.jpg')

# Averaging
average = cv.blur(img , (3,3))
cv.imshow("average",average)

# Median blur
median = cv.medianBlur(img, 7)
cv.imshow("median", median)

# Bilateral blur (retains edges)
bilateral = cv.bilateralFilter(img, 20, 15, 15)
cv.imshow("bilateral", bilateral)

cv.waitKey(0)