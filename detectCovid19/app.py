#Import necessary libraries
from flask import Flask, render_template, request
import pandas as pd
import numpy as np
import tensorflow.compat.v1 as tf
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from keras.models import load_model
import os

# Create flask instance
app = Flask(__name__)

#Set Max size of file as 10MB.
app.config['MAX_CONTENT_LENGTH'] = 10 * 1024 * 1024

#Allow files with extension png, jpg and jpeg
ALLOWED_EXTENSIONS = ['png', 'jpg', 'jpeg']
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def init():
    global graph
    graph = tf.get_default_graph()

# Function to load and prepare the image in right shape
def read_image(filename):
    # Load the image
    img = load_img(filename, color_mode = "rgb", target_size=(224, 224, 3))
    # Convert the image to array
    img = img_to_array(img)
    img = np.expand_dims(img, axis=0)
    print(img.shape)
    return img



@app.route("/", methods=['GET', 'POST'])
def home():
    return render_template('home.html')

@app.route("/predict", methods = ['GET','POST'])
def predict():
    if request.method == 'POST':
        file = request.files['file']
        try:
            if file and allowed_file(file.filename):
                filename = file.filename
                file_path = os.path.join('static/images', filename)
                file.save(file_path)
                img = read_image(file_path)
                # Predict the class of an image

                with graph.as_default():
                    model1 = load_model('covid19detector.h5')
                    p = model1.predict(img)
                    print(p[0,0])
                    
                #Map category with the numerical class
                if p[0,0] == 0:
                    final_result = "Covid Positive"
                elif p[0,0] == 1:
                    final_result = "Covid Negative"
                return render_template('predict.html', final_result = final_result)
        except Exception as e:
            print (e)
            return "Unable to read the file. Please check if the file extension is correct."

    return render_template('predict.html')

@app.route("/detect.html")
def detect():
    return render_template('detect.html')

@app.route("/about.html")
def about():
    return render_template('about.html')

if __name__ == "__main__":
    init()
    app.run()