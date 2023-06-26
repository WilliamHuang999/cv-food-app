import cv2 as cv

img = cv.imread('will-cv-tutorial\Photos\cat.jpg')

# Convert to grayscale =================================================================================================
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Gray', gray)

# Blur =================================================================================================================
blur = cv.GaussianBlur(img, (5,5), cv.BORDER_DEFAULT)     # Kernel size controls magnitude of blur
# cv.imshow("Blur", blur)

# Edge cascade =========================================================================================================
canny = cv.Canny(img, 125, 175)         # Finds edges in image with Canny Edges algorithm
cannyBlur = cv.Canny(blur, 125, 175)    # Finds edges of blurred image (will be less)
cv.imshow("Canny Edges", canny)
cv.imshow("Canny Edge Blur", cannyBlur)

# Dilate image --> adds pixels to boundaries of objects in image =======================================================
dilated = cv.dilate(canny, (3,3), iterations=1)     
# cv.imshow("Dilated", dilated)

# Erode image --> removes pixels on object boundaries ==================================================================
eroded = cv.erode(dilated, (3,3), iterations=1)
# cv.imshow("Eroded", eroded)

# Resize ===============================================================================================================
resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)         # Resizes image ignoring aspect ratio
# cv.imshow("Resized", resized)

# Cropping =============================================================================================================
cropped = img[50:200, 200:400]          # Crops image from row 50 to 200 and column 200 to 400
cv.imshow("Cropped", cropped)


cv.waitKey(0)