#Read superheroes.json
import json

from pprint import pprint

with open('superheroes.json') as f:
	data = json.load(f)

#write csv
import csv

with open('superheroes.csv', 'w') as f:
    writer = csv.writer(f)
    header = ["name", "age", "secret identity", "powers", "squad Name", "hometown", "formed", "secret base", "active"]
    writer.writerow(header)

	members = data['members']
	for m in members: 
		name = m["name"]
		age = m["age"]
		secretIdentity = m["secret identity"]
		squadName = data["squad Name"]
		hometown = data["hometown"]
		formed = data["formed"]
		secretbase = data["secret base"]
		active = data["active"]

		writer.writerow([name, age,secretIdentity,powers,squadName,hometown,formed,secretbase,active])