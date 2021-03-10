def is_valid(num):
    return type(num) == int or type(num) == float
def add(x, y):
    if is_valid(x) and is_valid(y):
        return x + y
    else:
        return None

def sub(x, y):
    if is_valid(x) and is_valid(y):
        return x - y
    else:
        return None

def mul(x, y):
    if is_valid(x) and is_valid(y):
        return x * y
    else:
        return None

def div(x, y):
    if is_valid(x) and is_valid(y):
       try:
           return x / y
        except ZeroDivisionError:
            return [] # for handling zero div
    else:
        return None

calculations = {
    "*" : mul,
    "+": add,
    "-" : sub, 
    "/" : div
}


num1 = float(input("Enter your number 1: "))
num2 = float(input("Enter your number 2: "))

op = input("Enter your operator: ")

op_func = calculations.get(op)

if op_func:
    result = op_func(num1,num2)
    if result == []:
        print("Zero Division Occured")
    if not result:
        print("Invalid number")
    else:
        print(f"Answer: {result}")


