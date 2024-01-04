import sys 

def add(num1, num2):
    addition = num1 + num2
    return addition

def sub(num1, num2):
    sub = num1 -num2 
    return sub

def mul(num1, num2):
    mul = num1 * num2
    return mul

def div(num1, num2):
    div = num1/num2
    return div

num1 = float(sys.argv[1]) #sys.argv by default read the cmd line arg as string #so using typecasting into int 
operation = sys.argv[2] 
num2 = float(sys.argv[3]) # problem will be if the user gives decimal values as the cmd line args; program will break

if operation == "add":
    output = add(num1, num2)
    print(output)


