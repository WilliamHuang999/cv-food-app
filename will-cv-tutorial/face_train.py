# Program to compile training data for facial recognition
import cv2 as cv
import os
import numpy as np


people = []
dir = r"C:\Users\gener\OneDrive\Documents\wildlife-locator-application\will-cv-tutorial\Faces\train"
for i in os.listdir(dir):
    people.append(i)
haar_cascade = cv.CascadeClassifier("will-cv-tutorial\haar_face.xml")

features = []       # Image arrays of faces
labels = []         # List of indices to map to image labels

def create_train():
    """
    Compile training data for face recognition
    """
    # Loop thru person folders in people
    for i in range(0,len(people)):
        path = os.path.join(dir,people[i])
        person = os.listdir(path)

        # Loop thru images in each person folder
        for j in range(0,len(person)):
            # Read in image
            img_path = os.path.join(path,person[j])
            img = cv.imread(img_path)
            gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

            # Detect face in the image
            faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)

            # Crop out face region of interest from image
            for (x,y,w,h) in faces_rect:
                faces_roi = gray[y:y+h, x:x+w]
                features.append(faces_roi)
                labels.append(i)

create_train()
# print("Length of features: " + str(len(features)))
# print("Length of labels: " + str(len(labels)))
features = np.array(features, dtype="object")
labels = np.array(labels)

face_recognizer = cv.face.LBPHFaceRecognizer_create()            # Initialize face recognizer object

# Train recognizer on features and labels lists
face_recognizer.train(features, labels)