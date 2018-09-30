"""
A simple file to demonstrate/represent coding style.
This file defines several functions to perform some simple arithmetic operations,
and a 'main' function to test their use.
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

    # raise to a fraction (not implemented)
    if -1 < num2 < 1 and num2 != 0:
        raise NotImplementedError('Raising by a fraction is not supported at this time.')
    # raise to a negative number
    elif num2 < 0:
        num2 = multiplication(num2, -1)
        while num2 > 0:
            result = multiplication(result, num1)
            num2 = subtraction(num2, 1)
        return division(1, result)
    # raise to a positive number or 0
    else:
        while num2 > 0:
            result = multiplication(result, num1)
            num2 = subtraction(num2, 1)
        return result


def inverse(num):
    """ Return the inverse of num """
    return power(num, -1)


def test_function():
    """
    The main function, called if this file is ran as the main file.
    The purpose of this function is to test the functions outlined in this file.
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
        print 'inverse 0.2 = {}'.format(inverse(0.2))
        print 'inverse 10 = {}'.format(inverse(10))
        # ## test for errors, only one test at a time ##
        # print '6/0={}'.format(division(6, 0))
        # print '6/0={}'.format(addition('test', 0.5))
        # print '6/0={}'.format(power(4, 0.5))
    except ArithmeticError as e:
        print ('An arithmetic error has occurred. {}'.format(e.message))
    except NotImplementedError as e:
        print ('This feature is not yet implemented. {}'.format(e.message))
    except TypeError as e:
        print ('Wrong type provided. {}'.format(e.message))

    return


if __name__ == '__main__':
    test_function()
