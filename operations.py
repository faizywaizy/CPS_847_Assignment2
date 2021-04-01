def halved(value):
    return value/2

def quartered(value):
    return value/4

def divide(value,divisor):
    if divisor == 0:
        raise ZeroDivisionError('Cannot divide by zero.')
    return  (value/divisor)

def squared(value):
    return value*value

def cubed(value):
    return value*value*value

def multiply(value,multiplier):
    return value*multiplier
