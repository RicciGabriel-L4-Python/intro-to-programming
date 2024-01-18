#Make several dictionaries, where each dictionary represents a different pet
pets=[]

pet = {
    'animal type': 'Dog',
    'name': 'Ginger',
    'owner': 'ricci',
}

pets.append(pet)


pet = {
    'animal type': 'Snake',
    'name': 'Boogie',
    'owner': 'ricci',
}

pets.append(pet)


pet = {
    'animal type': 'Dinosaur',
    'name': 'Wugi Wugi',
    'owner': 'ricci',
}

pets.append(pet)

#loop through your list and asyou do, print everything you know about 
for pet in pets:
    print(f"\nHere's the information about {pet['name']}:")
    for key, value in pet.items():
        print(f"\t{key}: {value}")
