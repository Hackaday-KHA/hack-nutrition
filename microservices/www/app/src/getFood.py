from flask import Blueprint
import json
import requests
from .config import dataUrl, dataHeaders

get_food = Blueprint('get_food', __name__)
clarifaiAPIKey = "d2f08a3a17894b3da12cb03f291f9d6c"

@get_food.route("/get_food")
def articles():

    query = {
        'type': 'select',
        'args': {
            'table': 'article',
            'columns': [
                '*'
            ]
        }
    }
    print(json.dumps(query))
    print(dataUrl)

    response = requests.post( dataUrl, data = json.dumps(query), headers = dataHeaders)

    return response.content
