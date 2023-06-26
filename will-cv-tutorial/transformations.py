import cv2 as cv
import numpy as np

img = cv.imread('will-cv-tutorial\Photos\park.jpg')

# Translation ==========================================================================================================
def translate(img, x, y):
    """
    Translate image along x-axis and y-axis the specified amount. Positive x is right. Positive y is down.
    """

    translateMatrix = np.float32([[1,0,x],[0,1,y]])     # Translation matrix
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, translateMatrix, dimensions)

# cv.imshow("Translated", translate(img, 100, 100))

# Rotation =============================================================================================================
def rotate(img, angle, rotPoint=None):
    """
    Rotates image by specified angle about the rotation point. Positive angle is CCW.
    """
    (height, width) = img.shape[:2]
    if rotPoint is None:
        rotPoint = (width//2, height//2)
    
    rotMatrix = cv.getRotationMatrix2D(rotPoint, angle, 1)
    dimensions = (width,height)

    return cv.warpAffine(img, rotMatrix, dimensions)
 
# cv.imshow("Rotated", rotate(img, 45))

# Flip =================================================================================================================
# cv.imshow("Flipped", cv.flip(img, 0))       # Flips image over x axis
# cv.imshow("Flipped", cv.flip(img, 1))       # Flips image over y axis
# cv.imshow("Flipped", cv.flip(img, -1))       # Flips image over x and y axes

cv.waitKey(0)