#Read superheroes.json
import json

from pprint import pprint

with open('superheroes.json') as f:
	data = json.load(f)

all_powers=[]

#Get members
members = data['members']

#Loop over the members
for m in members:
	powers = m['powers']
	for p in powers: 
		#for each member, get their powers
		all_powers.append(p)



#get unique list of powers
unique_powers=list(set(powers))
#print to terminal
print unique_powers