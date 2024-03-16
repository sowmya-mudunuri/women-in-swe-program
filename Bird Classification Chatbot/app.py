import os
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from flask import Flask, request, render_template

# Define the path to your saved Keras model
LOCAL_MODEL = "C:/Users/Sowmya Mudunuri/Downloads/archive/EfficientNetB0-525-(224 X 224)- 98.97.h5"

# Define other constants (you should replace these with your actual values)
IMAGE_SIZE = (224, 224)
DIR_TRAIN = "C:/Users/Sowmya Mudunuri/Downloads/archive/train"
BATCH_SIZE_32 = 32

app = Flask(__name__)

# Define a custom metric function
def custom_f1_score(y_true, y_pred):
    # Calculate the F1 score
    true_positives = tf.reduce_sum(tf.math.round(tf.math.multiply(y_true, y_pred)))
    predicted_positives = tf.reduce_sum(tf.math.round(y_pred))
    actual_positives = tf.reduce_sum(y_true)
    
    precision = true_positives / (predicted_positives + tf.keras.backend.epsilon())
    recall = true_positives / (actual_positives + tf.keras.backend.epsilon())
    
    f1 = 2 * (precision * recall) / (precision + recall + tf.keras.backend.epsilon())
    
    return f1

# Register the custom metric function
with custom_object_scope({'custom_f1_score': custom_f1_score}):
    model = load_model(LOCAL_MODEL)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        # Getting the image from the user
        f = request.files['image']
        base_path = os.path.dirname(__file__)
        file_path = os.path.join(base_path, 'uploads', f.filename)
        print("Uploaded image: ", file_path)
        f.save(file_path)

        # Reshaping the image
        img = image.load_img(file_path, target_size=IMAGE_SIZE)
        x = image.img_to_array(img)
        x = np.expand_dims(x, axis=0)

        # Making predictions
        predictions = model.predict(x)
        print("Predictions: ", predictions)

        # Generating batches of tensor image data with real-time data augmentation
        generator = ImageDataGenerator()
        train_ds = generator.flow_from_directory(DIR_TRAIN, target_size=IMAGE_SIZE, batch_size=BATCH_SIZE_32)

        # Classifying
        classes = list(train_ds.class_indices.keys())
        print("Bird species: ", classes[np.argmax(predictions)])

        # Calculating prediction probability
        probability = round(np.max(model.predict(x) * 100), 2)
        print("Probability: ", probability)

        # Printing the output message
        text = "Bird species is : " + str(classes[np.argmax(predictions)]) \
            + " with a probability of " + str(probability) + "%"

    return text

if __name__ == '__main__':
    app.run(debug=True, threaded=False)
