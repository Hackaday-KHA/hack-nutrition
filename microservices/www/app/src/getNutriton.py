from flask import Blueprint
import json
import requests
from .config import dataUrl_nutrition, dataheaders_nutrition

get_nutrition = Blueprint('get_nutrition', __name__)

@get_nutrition.route("/get_nutrition")
def article():

    query = { 'query': 'apple' }

    #print(json.dumps(query))
    #print(dataUrl_nutrition)

    response = requests.post( dataUrl_nutrition, data = json.dumps(query), headers = dataheaders_nutrition)

    return response.content.decode('latin1')
