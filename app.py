from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
# from PIL import Image
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import RandomForestRegressor
from pickle import load
from numpy import array
# import numpy as np
import os
import glob


# print("Reading H5 model")
# pre_model = tf.keras.models.load_model("EffNetV2SModel.h5")
# print("Writing pb model")
# pre_model.save("saved_model")
# quit(0)
app = Flask(__name__)
model = load(open('model.pkl', 'rb'))

@app.route('/')
def home():
	return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
	feature_list = request.form
	feature_list = feature_list.split(',')
	pred = model.predict([feature_list])
#return str(vals[np.argmax(pred)])
	value = str(pred[0][0])
	output_string = "Prediction = " + value
	return render_template('index.html', prediction_text=output_string.format(text))

if __name__ == '__main__':
	app.run()
