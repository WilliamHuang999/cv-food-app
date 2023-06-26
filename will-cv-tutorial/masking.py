# Masking allows focusing on certain part of image (e.g. masking/focusing on faces of people)
import cv2 as cv
import numpy as np

img = cv.imread('will-cv-tutorial\Photos\cats.jpg')
blank = np.zeros(img.shape[:2], dtype='uint8')     # Needs to be the same size as the image

mask = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)       # Create mask

masked = cv.bitwise_and(img, img, mask=mask)
cv.imshow("Masked image", masked)

cv.waitKey(0)