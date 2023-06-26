from keras.models import load_model
import tensorflow as tf
import keras.utils as image
import numpy as np
import os

model_path = 'models/my_model'
classes = ['Cat', 'Dog']

def predict(img):
    print('Loading model...')
    model = tf.keras.models.load_model(model_path)
    print('Done')

    metrics = [
        tf.metrics.BinaryAccuracy(),
        tf.metrics.Precision(),
        tf.metrics.Recall()
    ]
    model.compile(metrics=metrics)

    x = np.expand_dims(img, axis=0)

    images = np.vstack([x])
    prediction = model.predict(images)
    dog_probability = float(prediction[0])
    print(dog_probability)
    idx = dog_probability > 0.5
    return ('Cat', 'Dog')[idx]
    # predicted_class = classes[np.argmax(prediction)]Bug
    # return predicted_class