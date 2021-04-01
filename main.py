import operations
testNumbers = [6, 5, 0.32, 0.82, 0, 65, 0.5, 32, 8, 0.506, 432, 456.2, 0]

def testCode(data):
    for number in data:
        if number == 0:
            print("Skipping 0\n")
            continue
        try:
            print("{0} squared is {1}\n".format(number,operations.squared(number)))
            print("{0} cubed is {1}\n".format(number,operations.cubed(number)))
            print("{0} multiplied by 3 is {1}\n".format(number,operations.multiply(number,3)))
            print("{0} halved is {1}\n".format(number,operations.halved(number)))
            print("{0} quartered is {1}\n".format(number,operations.quartered(number)))
            print("{0} divided by zero is {1}\n".format(number,operations.divide(number,0)))

        except ZeroDivisionError:
            print("Divisor cannot be zero\n")
