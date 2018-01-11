vegetables = [
 {"name": "eggplant", "color": "purple"},
 {"name": "tomato", "color": "red"},
 {"name": "corn", "color": "yellow"},
 {"name": "zucchini", "color": "green"},
 {"name": "artichoke", "color": "green"},
 {"name": "butternut squash", "color": "yellow"},
 {"name": "mushroom", "color": "brown"},
 {"name": "broccoli", "color": "green"},
]

#Write header file to csv
import csv

with open('veggies.csv', 'w') as f:
	writer = csv.writer(f)
	writer.writerow(['name', 'color', 'length'])

#Loop through each veggie
	for veggie in vegetables:
#For each veggie write a row to the csv
		name = veggie["name"]
		color = veggie["color"]
		length = len(name)
		writer.writerow([name, color, length])