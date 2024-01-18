#input age
prompt = "how old are you?"
prompt += "\nEnter 'quit' when you are finished.:"


while True:
    age = int(input(prompt))
    #if a person is under 3
    if age <3:
        print(" your ticket is free!")
    #if a person is under 13
    elif age <13:
        print(" your ticket is 10$.")
    #if a person is above 13
    else:
        print(" your ticket is 15$")