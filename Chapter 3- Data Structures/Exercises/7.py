#list of places
Locations = ['Philippines','U.A.E','Italy','Japan','Korea']

#print the original
print("Original Order:")
print(Locations)

#print the list in alphabetical order using "sorted()"
print("\nAlphabetical:")
print(sorted(Locations))

#Show that your list is still in its original order by printing it.
print("\nOriginal Order:")
print(Locations)

#print the list in reverse alphabetical order using "sorted()"
print("\nReverse Alphabetical:")
print(sorted(Locations, reverse= True))

#Show that your list is still in its original order by printing it again
print("\nOriginal Order:")
print(Locations)

#print the list in reverse order using "reverse()"
print("\nReverse")
Locations.reverse()
print(Locations)

#Show that your list is still in its original order by printing it again
print("\nOriginal Order:")
print(Locations)

#print the list in alphabetical order using "sort()"
print("\nAlphabetical:")
Locations.sort()
print(Locations)

#print the list in reverse alphabetical order using "sort()"
print("\nReverse Alphabetical:")
Locations.sort(reverse=True)
print(Locations)