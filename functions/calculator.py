def add(x, y):
    result = x+y
    return result


def subtract(x, y):
    result = x - y
    return result

def divide(x, y):
    result = x/y
    return result

def multiply(x, y):
    result = x * y 
    return result

def remainder(x, y):
    result = x % y
    return result

def power(x, y):
    result = x ** y 
    return result


def get_sum(*numbers):
    sum = 0 
    for num in numbers:
        sum += num
    return sum

def get_multiplication(*numbers):
    total = 1
    for num in numbers:
        total*=num
    print(total) 

get_multiplication(2, 5, 10)