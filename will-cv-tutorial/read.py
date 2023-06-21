import cv2 as cv

img = cv.imread("cat.jpg")     # Takes in path to image and returns image as matrix of pixels

# cv.imshow("Cat", img)               # Opens img in new window called "Cat"

# cv.waitKey(0)   # Waits for key to be pressed in seconds (0 = infinity)