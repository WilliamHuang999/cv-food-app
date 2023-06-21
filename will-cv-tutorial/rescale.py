import cv2 as cv

img = cv.imread('will-cv-tutorial\Photos\cat_large.jpg')

def rescaleFrame(frame, scale=0.75):
    """
    Resizes frame by specified scale (works for images, videos, and live video).
    """
    width = int(frame.shape[1] * scale)         # frame.shape[1] is width of frame
    height = int(frame.shape[0] * scale)
    dim = (width, height)

    return cv.resize(frame, dim, interpolation=cv.INTER_AREA)       # Resizes frame to particular dimension

def changeLiveVidRes(video, width, height):
    """
    Changes resolution of VideoCapture object video (only works with live video).
    """
    video.set(3, width)         # 3 references video's width
    video.set(4,height)         # 4 references video's height


imgResized = rescaleFrame(img, 0.1)     # Assign resized frame to new object
cv.imshow("Resized", imgResized)

cv.waitKey(0)