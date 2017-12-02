from flask import Flask
from .hasuraExamples import hasura_examples
from .getFood import get_food
from .get_nutrition import get_nutrition
app = Flask(__name__)

# This line adds the hasura example routes form the hasuraExamples.py file.
# Delete this, and then delete the file to remove them from your project
app.register_blueprint(hasura_examples)
app.register_blueprint(get_food)
app.register_blueprint(get_nutrition)
from .server import *
