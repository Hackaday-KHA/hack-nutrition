# testing json parsing to get the nutritional values
import json 
from pprint import pprint

def extract_nutri(data_json):
	
	data_dict = json.loads(data_json)
	data_dict_foods = data_dict["foods"] # this is a python list with info of all foods in query
	
	# the tags we want to extract from the big json file
	nutrition_tags = {}
	nutrition_tags['calories'] = 'nf_calories'
	nutrition_tags['cholesterol'] = 'nf_cholesterol'
	nutrition_tags['dietary_fiber'] = 'nf_dietary_fiber'
	nutrition_tags['potassium'] = 'nf_potassium'
	nutrition_tags['protein'] = 'nf_protein'
	nutrition_tags['saturated_fat'] = 'nf_saturated_fat'
	nutrition_tags['sodium'] = 'nf_sodium'
	nutrition_tags['sugars'] = 'nf_sugars'
	nutrition_tags['total_carbohydrate'] = 'nf_total_carbohydrate'
	nutrition_tags['total_fat'] = 'nf_total_fat'

	# Creating a new dict with only the most required info corresponding to tags in nutrition_tags
	my_nutri_dict = {}
	for idx in range(len(data_dict_foods)):
	  food_key = data_dict_foods[idx]["food_name"]
	  food_nutri_dict = {}
	  
	  for key,value in nutrition_tags.items():
	    food_nutri_dict[key] = data_dict_foods[idx][value]
	    
	  my_nutri_dict[food_key] = food_nutri_dict  


	return my_nutri_dict
  
  
  
  




