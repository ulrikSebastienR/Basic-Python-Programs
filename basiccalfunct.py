
def add(num1,num2):
    return(num1+num2)

def sub(num1,num2):
    return(num1-num2)

def mult(num1,num2):
    return(num1*num2)

def div(num1,num2):
    return(num1/num2)

val1=float(input("Enter a number. "))
opt=input("Select operator: \n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n")
val2=float(input("Enter another number. "))

if opt == '1':
    print(add(val1, val2))
elif opt == '2':
    print(sub(val1, val2))
elif opt == '3':
    print(mult(val1, val2))
elif opt == '4':
    print(div(val1, val2))
else:
    print("Invalid input")
