import tensorflow as tf
import os
from keras.utils import img_to_array, load_img
import numpy as np
import cv2 as cv

# Load model
model = tf.keras.models.load_model("===========")       # Put in model path here
print(model.summary())

# Load categories
source_folder = "Test folder here"
categories = os.listsdir(source_folder).sort()
print(categories)
print(len(categories))      # Should be 131

# Load and prepare image
def prepareImage(path):
    img = load_img(img, target_size=(100,100))
    imgArray = img_to_array(img)
    # print(imgArray.shape)
    imgArray = np.expand_dims(imgArray, axis=0)
    imgArray = imgArray / 255.
    return imgArray

testImgPath = "======================="
imageForModel = prepareImage(testImgPath)

resultArray = model.predict(testImgPath, verbose=1)
answers = np.argmax(resultArray, axis=1)
print(categories[answers[0]])

# Show image with text below



