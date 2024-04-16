from flask import Flask, jsonify, request
import base64
import numpy as np
from detect import object_detect
import os

app = Flask(__name__)


@app.route('/image', methods=['POST'])
def register_new():
    photo = request.get_json()['user_photo']
    
    photo_data = base64.b64decode(photo)
    
    path = "images/test.jpg"
    with open(path, "wb") as file:
        file.write(photo_data)
    res = object_detect(path)
    return str(res)
    
    