#list of orders with 3 pastrami
sandwich_orders = [' Hotdog','pastrami',' ham',' vegetabble','pastrami',' cheese',' chicken','pastrami']

#empty list
finished_sandwiches = []

#for pastrami orders
print("I'm sorry, we're out of pastrami.")
while 'pastrami' in sandwich_orders:
    #delete pastrami from the list using '.remove'
    sandwich_orders.remove('pastrami')

print("\n")
while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print(f"I'm making your{sandwich} sandwich.")
    finished_sandwiches.append(sandwich)

print("\n")
for sandwich in finished_sandwiches:
    print(f"I made you a{sandwich} sandwich.")