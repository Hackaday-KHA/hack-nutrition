from flask import Blueprint
import json
import requests
from flask import request
from .config import dataUrl_nutrition, dataheaders_nutrition

get_nutrition = Blueprint('get_nutrition', __name__)

@get_nutrition.route("/get_nutrition")
def articles():

    food = request.args.get('foodType')
    query = { 'query' : food,
    		  'num_servings' : 1
              'use_branded_foods' : true }

    #print(json.dumps(query))
    #print(dataUrl_nutrition)

    response = requests.post( dataUrl_nutrition, data = json.dumps(query), headers = dataheaders_nutrition)

    return response.content.decode('latin1')
