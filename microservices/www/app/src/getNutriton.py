from flask import Blueprint
import json
import requests
from .config import dataUrl_nutrition, dataHeaders_nutrition

get_nutrition = Blueprint('get_nutrition', __name__)

@get_nutrition.route("/get_nutrition")
def nutrition_query():

    query = { 'query': 'select' }
    
    print(json.dumps(query))
    print(dataUrl_nutrition)

    response = requests.post( dataUrl_nutrition, data = json.dumps(query), headers = dataHeaders_nutrition)

    return response.content
