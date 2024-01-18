#Write a loop that prompts the user to enter a series of pizza toppings until they enter a 'quit' value.
prompt = "\nWhat topping would you like on your pizza?"
prompt += "\nEnter 'quit' when you are finished: "

while True:
    topping = input(prompt)
    if topping != 'quit':
      
      #print a message saying you’ll add that topping to their pizza.
        print(f"  I'll add {topping} to your pizza.")
    else:
        break
