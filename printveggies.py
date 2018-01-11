vegetables = [
 {"name": "eggplant"},
 {"name": "tomato"},
 {"name": "corn"},
 {"name": "zucchini"},
 {"name": "artichoke"},
 {"name": "butternut squash"},
 {"name": "mushroom"},
 {"name": "broccoli"},
]

#Write header file to csv
import csv

with open('veggies.csv', 'w') as f:
	writer = csv.writer(f)
	writer.writerow(['name', 'length'])

#Loop through each veggie
	for veggie in vegetables:
#For each veggie write a row to the csv
		name = veggie["name"]
		length = len(name)
		writer.writerow([name, length])