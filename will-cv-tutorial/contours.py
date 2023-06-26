import cv2 as cv
import numpy as np

img = cv.imread('will-cv-tutorial\Photos\cats.jpg')
blank = np.zeros(img.shape, dtype="uint8")

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# blur = cv.GaussianBlur(gray, (5,5), cv.BORDER_DEFAULT)
canny = cv.Canny(gray, 125, 175)

# Returns list of contours that were found in the image and hierarchcal representation of those contours
# cv.RETR_LIST refers to the mode of contouring (this one returns all contours)
contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
print("# of contours found: " + str(len(contours)))
cv.drawContours(blank, contours, -1, (0,0,255), 1)      # Draws contours on image --> pass in image to draw over, contours, how many contours to draw (-1 is all), color, and thickness
cv.imshow("Contours Drawn", blank)

ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)      # This function "binarizes" image. If intensity of pixel is below 125 it sets the pixel to black. If above 125, it sets pixel to white (255)
cv.imshow("Thresh", thresh)
contours, hierarchies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
print("# of contours found: " + str(len(contours)))



cv.waitKey(0)