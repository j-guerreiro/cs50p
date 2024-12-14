# https://www.tutorialspoint.com/python-prefix-extraction-before-specific-character

expression = input("Expression: ")
print(expression)

# remove white spaces from string
expression = expression.replace(" ", "")

division = expression.find("/")


if expression.find("/") != -1:
    divisionDelimiter = expression.find("/")
    a = expression[:divisionDelimiter] # pre-delimiter -> before operator
    b = expression[divisionDelimiter + 1:] # post-delimiter -> after operator
    a = int(a)
    b = int(b)
    result =  round(a / b, 1) # round and show 1 decimal value
    print(result)

elif expression.find("-") != -1:
    minusDelimiter = expression.find("-")
    a = expression[:minusDelimiter]
    b = expression[minusDelimiter + 1:]
    a = int(a)
    b = int(b)
    result =  a - b
    print(result)

elif expression.find("*") != -1:
    multiplicationDelimiter = expression.find("*")
    a = expression[:multiplicationDelimiter]
    b = expression[multiplicationDelimiter + 1:]
    a = int(a)
    b = int(b)
    result =  a * b
    print(result)

elif expression.find("+") != -1:
    plusDelimiter = expression.find("+")
    a = expression[:plusDelimiter]
    b = expression[plusDelimiter + 1:]
    a = int(a)
    b = int(b)
    result =  a + b
    print(result)