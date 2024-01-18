 #Make a dictionary containing three major rivers.
rivers = {
    'pasig river' : 'philippines',
    'amazon river' : 'south america',
    'Yangtze River': 'china',
}

#Use a loop to print the name of each river included in the dictionary.
for river, country in rivers.items():
    print(f"{river} flows through {country}")

print("\n")

for river in rivers.keys():
    print(f"{river}")
print("\n")

for country in rivers.values():
    print (f"{country}")