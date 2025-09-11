def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b


function_table = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}


number1 = float(input('Enter the first number: '))
number2 = float(input('Enter the second number: '))
op = input('What do you want to do [+, -, *, /]? : ')

f = function_table[op]

result = f(number1, number2)

print(f'The result is {result}')