import tensorflow as tf
import os
from keras.utils import img_to_array, load_img
import numpy as np
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Dropout, Flatten, Dense
from keras.preprocessing.image import ImageDataGenerator
from keras.callbacks import EarlyStopping
import pandas as pd


trainPath = r"C:\Users\gener\OneDrive\Documents\fruits360\fruits-360\Train"
testPath = r"C:\Users\gener\OneDrive\Documents\fruits360\fruits-360\Test"

batchSize = 64      # Reduce value if you have less GPU

# Read in example image and get shape
# img = load_img(trainPath + r"\Quince\0_100.jpg")
# plt.imshow(img)
# plt.show()

# imgA = img_to_array(img)
# print(imgA.shape)

# Build model
model = Sequential()
# Base
model.add(Conv2D(filters=128, kernel_size=3, activation="relu", input_shape=(100,100,3)))
model.add(MaxPooling2D())
model.add(Conv2D(filters=64, kernel_size=3, activation="relu"))
model.add(Conv2D(filters=32, kernel_size=3, activation="relu"))
model.add(MaxPooling2D())
model.add(Dropout(0.5))
model.add(Flatten())
# Head
model.add(Dense(5000, activation="relu"))
model.add(Dense(1000, activation="relu"))
model.add(Dense(131, activation="softmax"))

print(model.summary())

# Compile model
model.compile(loss="categorical_crossentropy", optimizer="adam", metrics=["accuracy"])

# Load data
train_datagen = ImageDataGenerator(rescale=1./255, shear_range=0.3, horizontal_flip=True, vertical_flip=True, zoom_range=0.3)

test_datagen = ImageDataGenerator(rescale=1./255)

train_generator = train_datagen.flow_from_directory(trainPath, target_size=(100,100), batch_size=batchSize, color_mode="rgb", class_mode="categorical", shuffle=True)


test_generator = test_datagen.flow_from_directory(trainPath, target_size=(100,100), batch_size=batchSize, color_mode="rgb", class_mode="categorical")

stepsPerEpoch = np.ceil(train_generator.samples / batchSize)
validationSteps = np.ceil(test_generator.samples / batchSize)

# Early stopping
stop_early = EarlyStopping(monitor="val_accuracy", patience=5, min_delta=0.001)

history = model.fit(train_generator, steps_per_epoch=stepsPerEpoch, epochs=50, validation_data=test_generator, validation_steps=validationSteps, callbacks=[stop_early])

# Plot learning curves
# history_frame = pd.DataFrame(history.history)
# history_frame.loc[:, ['loss', 'val_loss']].plot()
# history_frame.loc[:, ['binary_accuracy', 'val_binary_accuracy']].plot()

model.save(r"C:\Users\gener\OneDrive\Documents\cv-food-app\fruits360Model-v1.h5")     # Add file path to save the model to


