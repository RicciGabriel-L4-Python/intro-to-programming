#add more words from exercise 2.
programming = {
    'dictionary': "A collection of key-value pairs.",
    'Loop': "A sequence of instructions that is continually repeated until a certain condition is reached.",
    'string': "A data type used in programming, that is used to represent text rather than number.",
    'list': "Used to store multiple items in a single variablr.",
    'comment': "A text note that gives an explanation about the source code.",
    'variables': "A reserved memory location to store values.",
    'float': "A numerical value with a decimal component.",
    'function': "piece of pre-written code that performs an operation",
    'statements': "Allow you to make decision in your code, which can make your code more efficient and easier to read",
    'print': "it display output on screen.",
}

#make a loop that prints the word in dictionary.
for word, definition in programming.items():
    print(f"\n{word}: {definition}" )