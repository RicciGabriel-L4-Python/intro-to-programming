#invited guest list to dinner
guests = ['Mr. Abitria','Mr. Macalagay','Mr. Viernes']

##print the guest list with message, inviting them to dinner
name = guests[0]
print(f"{name} please come to dinner.")
name = guests[1]
print(f"{name} please come to dinner.")
name = guests[2]
print(f"{name} please come to dinner.")

print(f"\nLooks like {guests[2]}, can't make it dinner.")

#Mr. Viernes can't make it to dinner! replace him with Mr. Locsin
del(guests[2])
guests.insert(2, 'Mr. Locsin')

#re-print the invitation
name = guests[0]
print(f"\n{name} please come to dinner.")
name = guests[1]
print(f"{name} please come to dinner.")
name = guests[2]
print (f"{name} please come to dinner.")

#there's no enough space 
print(f"\nOh no! Looks like We don't have enough space for three.")

#remove 1 guest
name = guests.pop()
print(f"\nSorry {name}, We don't have enough space at the table.")

#re-print the invitation
name = guests[0]
print(f"{name} please come to dinner.")
name = guests[1]
print(f"{name} please come to dinner.")

#empty the list, and prove the list is empty
del(guests[0])
del(guests[0])
print(guests) 