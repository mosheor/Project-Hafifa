import torch
from flask import Flask
import cv2
from minioClient import download_file
import os

app = Flask(__name__)


@app.route('/predict/<buck_name>/<file_name>')
def predict(buck_name, file_name):
    path = os.path.dirname(os.path.abspath(__file__)) + '/' + file_name
    download_file(buck_name, file_name, path)
    image = cv2.imread(path)
    preds = fa.detect_faces(image)
    os.remove(path)

    if len(preds) == 0:
        return "0"

    return "1"


@app.errorhandler(404)
def not_found(e):
    return '', 404


if __name__ == '__main__':
    model_name = 'FaceAlignment.model'
    model_path = os.path.dirname(os.path.abspath(__file__)) + '/' + model_name

    fa = torch.load(model_path)
    app.run(host='0.0.0.0', port=5000)