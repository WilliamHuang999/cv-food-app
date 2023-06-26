import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3), dtype="uint8")          # Create blank image of 500 by 500 pixels with 3 color channels
# v.imshow("Blank", blank)

# Paint on image =======================================================================================================
# blank[:] = 0,255,255          # Color entire image yellow (BGR)
# blank[200:300, 300:400] = 0,0,255          # Color pixels on rows 200 to 300 and columns 300 to 400 red
# cv.imshow('Green',blank)

# Draw rectangle =======================================================================================================
cv.rectangle(blank, (0,0), (blank.shape[0]//2,blank.shape[1]//2), (0,255,0), thickness=-1)  # Draw rectangle w/ green outline from (0,0) to (250,250)
# cv.imshow("Rectangle", blank)

# Draw circle ==========================================================================================================
cv.circle(blank, (250,250), 40, (0,0,255), thickness=3)
# cv.imshow("Circle",blank)

# Draw line ============================================================================================================
cv.line(blank, (0,0), (blank.shape[0]//2,blank.shape[1]//2), (255,255,0), thickness=3)
#cv.imshow("Line", blank)

# Write text ===========================================================================================================
cv.putText(blank, "hello", (225,225), cv.FONT_HERSHEY_TRIPLEX, 1.0, (255, 255, 255), 2)
cv.imshow("Text", blank)

cv.waitKey(0)