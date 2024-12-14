# https://www.tutorialspoint.com/python-prefix-extraction-before-specific-character -> this helped

expression = input("Expression: ")

# remove white spaces from string
expression = expression.replace(" ", "")

if expression.find("/") != -1:
    divisionDelimiter = expression.find("/")
    a = expression[:divisionDelimiter] # pre-delimiter -> before operator
    b = expression[divisionDelimiter + 1:] # post-delimiter -> after operator
    a = int(a)
    b = int(b)
    result =  round(a / b, 1) # round and show 1 decimal value
    print(result)

elif expression.find("-", 1) != -1: # find the operator starting from index 1
    minusDelimiter = expression.find("-",1)

    # left hand negative number check
    # if expression[0] == "-":
    #   expression = expression[1:]
    #   a = expression[minusDelimiter]
    #   a = int(a)
    #   a = a * -1
    # else:    
    #     a = expression[:minusDelimiter]
    #     a = int(a)

    a = expression[:minusDelimiter]
    b = expression[minusDelimiter + 1:]
    a = int(a)
    b = int(b)
        
    # b = expression[minusDelimiter + 1:]
    # b = int(b)

    result = round(a - b, 1)
    print(result)

elif expression.find("*", 1) != -1:
    multiplicationDelimiter = expression.find("*")
    a = expression[:multiplicationDelimiter]
    b = expression[multiplicationDelimiter + 1:]
    a = int(a)
    b = int(b)
    result = round(a * b, 1)
    print(result)

elif expression.find("+", 1) != -1:
    plusDelimiter = expression.find("+",1)
    a = expression[:plusDelimiter]
    b = expression[plusDelimiter + 1:]
    a = int(a)
    b = int(b)
    result =  round(a + b, 1)
    print(result)

#TODO fix negative number input ex: with sign in front: -1 + 100