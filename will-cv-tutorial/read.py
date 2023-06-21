import cv2 as cv

# Reading images =======================================================================================================
# img = cv.imread('will-cv-tutorial\Photos\cat_large.jpg')            # Read in image at listed path and convert to matrix

# cv.imshow("Cat", img)           # Display img object as an image in window called "Cat"

# cv.waitKey(0)           # Wait for key press (0 = infinity)

# Reading videos =======================================================================================================

capture = cv.VideoCapture("will-cv-tutorial\Videos\dog.mp4")     # Takes in path to video or ints 0, 1, 2, 3 for when computer camera is used

# Display video --> need to do it frame by frame
while True:
    isTrue, frame = capture.read()      # Reads in capture video object frame by frame. Also returns whether or not read was successful
    cv.imshow("Video", frame)

    # If letter 'd' is pressed, break out of loop
    if cv.waitKey(20) & 0xFF == ord('d'):
        break

# Release variables and close all windows
capture.release()
cv.destroyAllWindows()