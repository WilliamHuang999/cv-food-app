import tensorflow as tf
from keras.utils import img_to_array, load_img
import numpy as np
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Dropout, Flatten, Dense
from keras.preprocessing.image import ImageDataGenerator
from keras.callbacks import EarlyStopping

kerasModel = tf.keras.models.load_model(r"C:\Users\gener\OneDrive\Documents\cv-food-app\flowersModel.h5")
converter = tf.lite.TFLiteConverter.from_keras_model(kerasModel)
tfliteModel = converter.convert()
open(r"C:\Users\gener\OneDrive\Documents\cv-food-app\flowersModel.tflite", "wb").write(tfliteModel)



# # Load TFLite model and allocate tensors.
# interpreter = tf.lite.Interpreter(model_content=tfliteModel)
# interpreter.allocate_tensors()
# #get input and output tensors
# input_details = interpreter.get_input_details()
# output_details = interpreter.get_output_details()

# # Load and preprocess image
# image_path = r"C:\Users\gener\OneDrive\Documents\cv-food-app\fruit-images\apple1.png"
# image = tf.keras.preprocessing.image.load_img(image_path, target_size=(100, 100))
# image = tf.keras.preprocessing.image.img_to_array(image)
# image = np.expand_dims(image, axis=0)
# image = image / 255.0  # Normalize the image

# # Set the input tensor
# interpreter.set_tensor(input_details[0]['index'], image)

# # Run the inference
# interpreter.invoke()

# # Get the output tensor
# output_tensor = interpreter.get_tensor(output_details[0]['index'])
# predictions = np.squeeze(output_tensor)

# # Get the predicted class label
# predicted_class_index = np.argmax(predictions)

# print('Predicted class:', predicted_class_index)
# print('Confidence:', predictions[predicted_class_index])
