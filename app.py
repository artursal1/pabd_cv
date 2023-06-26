from flask import Flask, render_template
import flask
# from PIL import Image
from predict import predict
from matplotlib import image as Image
from skimage.transform import resize
import numpy as np

app = Flask(__name__, template_folder='frontend/template', static_folder='frontend/static')

@app.route('/')
def home():
    print('Render index.html')
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict_frontend():

    imagefile = flask.request.files.get('imagefile', '')
    image = Image.imread(imagefile)
    res_image = resize(image, (180, 180))
    data = np.asarray(res_image)

    predicted_class = predict(data)
    return render_template('index.html', prediction_text=predicted_class)


if __name__=='__main__':
    app.run(debug=True)