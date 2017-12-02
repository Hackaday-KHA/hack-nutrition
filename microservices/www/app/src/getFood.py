from flask import Blueprint
import json
import requests
from .config import dataUrl, dataHeaders

# The package will be accessible by importing clarifai:
from clarifai import rest
from clarifai.rest import ClarifaiApp
from clarifai.rest import Image as ClImage

hasura_examples = Blueprint('hasura_examples', __name__)
clarifaiAPIKey = "d2f08a3a17894b3da12cb03f291f9d6c"

app = ClarifaiApp(api_key=clarifaiAPIKey)

# get the general model
model = app.models.get('food-items-v1.0')
# predict with the model
#model.predict_by_url(url='https://samples.clarifai.com/metro-north.jpg')
image = ClImage(url='http://www.bulkingbro.com/wp-content/uploads/2014/11/bulkingbro-pasta.jpg')
result = model.predict([image])

@hasura_examples.route("/get_food")
def articles():


    print(json.dumps(result))
    print(dataUrl)

    #response = requests.post( dataUrl, data = json.dumps(query), headers = dataHeaders)

    return result#response.content
