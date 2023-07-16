import tensorflow as tf
import os
from keras.utils import img_to_array, load_img
import numpy as np
import cv2 as cv

# Load model
model = tf.keras.models.load_model(r"C:\Users\gener\OneDrive\Desktop\fruits360.h5")       # Put in model path here
# print(model.summary())

# Load categories
source_folder = r"C:\Users\gener\OneDrive\Documents\fruits360\fruits-360\Test"
categories = os.listdir(source_folder)
categories.sort()
# print(categories)
# print(len(categories))      # Should be 131

# Load and prepare image
def prepareImage(path):
    img = load_img(path, target_size=(100,100))
    imgResult = img_to_array(img)
    imgResult = np.expand_dims(imgResult, axis=0)
    imgResult = imgResult / 255.
    return imgResult

testFolderPath = r"C:\Users\gener\OneDrive\Documents\cv-food-app\fruit-images"

for i in os.listdir(testFolderPath):
    imageForModel = prepareImage(testFolderPath + r"\\" + i)
    resultArray = model.predict(imageForModel, verbose=0)
    answers = np.argmax(resultArray, axis=1)
    print(i)
    print(categories[answers[0]])



