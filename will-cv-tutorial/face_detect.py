import cv2 as cv

img = cv.imread("will-cv-tutorial\Photos\group 2.jpg")
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# Read in haar cascade
haar_cascade = cv.CascadeClassifier("will-cv-tutorial\haar_face.xml")

# faces_rect is a list of np arrays of the face detection rectangles. Each rectangle list element is in the form: (x,y,w,h). (x,y) is the top left corner of the rectangle and w and h are the width and height of the shape.
faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor = 1.1, minNeighbors=6)   # Detects faces and returns rectangular coordinates of the face as a list
print("Number of faces found: " + str(len(faces_rect)))

# Get coords of rectangle for face and draw rectangle
for (x,y,w,h) in faces_rect:
    cv.rectangle(img, (x,y), (x+w,y+h), (0,255,0), thickness=2)
    cv.putText(img, "Face", (x,y-5), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,0),1)

cv.imshow("Detected faces", img)

cv.waitKey(0)