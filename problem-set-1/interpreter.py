# These links below helped a lot:
# https://www.tutorialspoint.com/python-prefix-extraction-before-specific-character
# https://stackoverflow.com/questions/48122608/how-do-i-generate-random-float-and-round-it-to-1-decimal-place
#
# author jguerreiro

expression = input("Expression: ")

# remove white spaces from string
expression = expression.replace(" ", "")

if expression.find("/") != -1:
    divisionDelimiter = expression.find("/")
    # pre-delimiter -> before operator
    a = expression[:divisionDelimiter]
    # post-delimiter -> after operator
    b = expression[divisionDelimiter + 1:] 
    a = int(a) # cast strings -> int
    b = int(b)
    result = a / b
    # cast int -> float
    result = float(result)
     # round and show 1 decimal value
    result =  round(result, 1)
    print(result)

# find the operator starting from index 1
elif expression.find("-", 1) != -1: 
    minusDelimiter = expression.find("-",1)
    a = expression[:minusDelimiter]
    b = expression[minusDelimiter + 1:]
    a = int(a)
    b = int(b)       
    result = a - b
    result = float(result)
    result = round(result, 1)
    print(result)

elif expression.find("*") != -1:
    multiplicationDelimiter = expression.find("*")
    a = expression[:multiplicationDelimiter]
    b = expression[multiplicationDelimiter + 1:]
    a = int(a)
    b = int(b)
    result = a * b
    result = float(result)
    result = round(result, 1)
    print(result)

elif expression.find("+", 1) != -1: 
    plusDelimiter = expression.find("+",1)
    a = expression[:plusDelimiter]
    b = expression[plusDelimiter + 1:]
    a = int(a)
    b = int(b)
    result = a + b
    result = float(result)
    result = round(result, 1)
    print(result)
else:
    print("Invalid operator!")