import pickle

from flask import Blueprint, request

import numpy as np


model=pickle.load(open('city_predictor.pkl','rb'))


prediction = Blueprint("do_signup", __name__)

@prediction.route('/predict',methods=['POST'])
def predict():
    lat=float(request.args.get("lat"))
    long=float(request.args.get("long"))
    result=model.predict(np.array([lat,long]).reshape(-1,2))

    return result[0]