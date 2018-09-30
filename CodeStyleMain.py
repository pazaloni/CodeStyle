"""
A simple file to demonstrate/represent coding style.
This file defines several functions to perform some simple arithmetic operations,
and a 'main' function to demonstrate its use.
"""


def addition(num1, num2):
    """ Return the result of adding num1 to num2 """
    return num1+num2


def subtraction(num1, num2):
    """ Return the result of subtracting num2 from num1 """
    return num1-num2


def multiplication(num1, num2):
    """ Return the result of multiplying num1 and num2 """
    return num1*num2


def division(num1, num2):
    """ Return the result of dividing num1 by num2 """
    return float(num1)/float(num2)


def power(num1, num2):
    """ Return the result of raising num1 to the power of num2 """
    result = 1

    # raise to the power of 0
    if num2 == 0:
        return result
    # raise to a positive number
    elif num2 > 0:
        while num2 > 0:
            result = multiplication(result, num1)
            num2 = subtraction(num2, 1)
        return result
    # raise to a negative number
    else:
        num2 = multiplication(num2, -1)
        while num2 > 0:
            result = multiplication(result, num1)
            num2 = subtraction(num2, 1)
        return division(1, result)


def main_function():
    """
    The main function, called if this file is ran as the main file
    """
    try:
        # run tests/try the functions outlined in this file
        print '7+5={}'.format(addition(7, 5))
        print '2-7={}'.format(subtraction(2, 7))
        print '7-2={}'.format(subtraction(7, 2))
        print '5*7={}'.format(multiplication(5, 7))
        print '5*-7={}'.format(multiplication(5, -7))
        print '2/4={}'.format(division(2, 4))
        print '6/2={}'.format(division(6, 2))
        print '5^3={}'.format(power(5, 3))
        print '5^-3={}'.format(power(5, -3))
        print '7^0={}'.format(power(7, 0))
        print '6/0={}'.format(division(6, 0))
    except ArithmeticError as e:
        print ('An arithmetic error has occurred. {}'.format(e.message))

    return


if __name__ == '__main__':
    main_function()
