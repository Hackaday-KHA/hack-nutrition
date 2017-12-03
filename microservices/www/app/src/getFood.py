from flask import Blueprint
import json
import requests
from .config import dataUrl, dataHeaders

dataUrl_clarifai = "https://api.clarifai.com/v2/models/dfebc169854e429086aceb8368662641/outputs"
dataheaders_clarifai = {
"Content-Type": "application/json",
"Authorization": "d2f08a3a17894b3da12cb03f291f9d6c"}

get_food = Blueprint('get_food', __name__)
clarifaiAPIKey = "d2f08a3a17894b3da12cb03f291f9d6c"

#model = appClarify.models.get('food-items-v1.0')

#image = ClImage(url='http://www.bulkingbro.com/wp-content/uploads/2014/11/bulkingbro-pasta.jpg')
#result = model.predict([image])

@get_food.route("/get_food")
def articles():
    query = {"inputs": [{"data": {"image":{"url": "https://samples.clarifai.com/metro-north.jpg"}}}]}

    response = requests.post( dataUrl_clarifai, data = json.dumps(query), headers = dataheaders_clarifai)
    result = response.content.decode('latin1')
    #print(json.dumps(result))
    #print(dataUrl)

    #response = requests.post( dataUrl, data = json.dumps(query), headers = dataHeaders)

    return result#response.content
