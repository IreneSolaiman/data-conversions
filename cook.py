#read vegetables.csv
import csv

with open('veggies.csv') as f:
		#convert to json
		reader = csv.DictReader(f)
		vegetables = list(reader)

#import the JSON library from python 
import json

#open a JSON file with the cooked veggies
with open('cooked_veggies.json', 'w') as f:
    json.dump(vegetables, f, indent=2)