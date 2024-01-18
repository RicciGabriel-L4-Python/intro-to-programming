#Make a list called sandwich_orders
sandwich_orders = [' Hotdog',' ham',' vegetabble',' cheese',' chicken']

#empty list of finished sanwich
finished_sandwiches = []

#loops through the list
while sandwich_orders:
    #'.pop' remvoves a specific item from the collection
    sandwich = sandwich_orders.pop()
    print(f"I'm making your{sandwich} sandwich.")
    finished_sandwiches.append(sandwich)

print("\n")
for sandwich in finished_sandwiches:
    print(f"I made you a{sandwich} sandwich.")

