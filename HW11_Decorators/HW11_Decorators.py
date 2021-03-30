# # 1. double_result
# # This decorator function should return the result of another function multiplied by two
# def double_result(func):
#     # return function result multiplied by two
#     pass
#
#
# def add(a, b):
#     return a + b
#
#
# add(5, 5)  # 10
#
#
# @double_result
# def add(a, b):
#     return a + b
#
#
# add(5, 5)  # 20
from functools import wraps


def double_result(func):
    # return function result multiplied by two
    @wraps(func)
    def inner(a, b):
        print(f'Result of function <{func.__name__}> multiplied by 2')
        multiplied = func(a, b) * 2
        return multiplied

    return inner


@double_result
def add(a, b):
    return a + b


print(add(5, 5))  # 20


# 2. only_odd_parameters
# This decorator function should only allow a function to have odd numbers as parameters,
# otherwise return the string "Please use only odd numbers!"

def only_odd_parameters(func):
    # if args passed to func are not odd - return "Please use only odd numbers!"
    @wraps(func)
    def inner(*args):
        for i in args:
            if i % 2 == 0:
                return "Please use only odd numbers!"
            else:
                continue

        add_odd = func(*args)
        return add_odd

    return inner


@only_odd_parameters
def add_var(a, b):
    return a + b


@only_odd_parameters
def multiply(a, b, c, d, e):
    return a * b * c * d * e


print(add_var(5, 2))  # 10
print(multiply(1, 3, 5, 7, 1))


# 3.* logged
# Write a decorator which wraps functions to log function arguments and the return value on each call.
# Provide support for both positional and named arguments (your wrapper function should take both *args
# and **kwargs and print them both):

def logged(func):
    # log function arguments and its return value
    @wraps(func)
    def inner(*args):
        """
        logged
        :param args:
        :return: func(args)
        """
        print(func.__name__, args)
        return func(args)

    return inner


@logged
def func(*args):
    """
    func
    :param args:
    :return: 3+len(*args)
    """
    return 3 + len(*args)


print(f"Log of func: {func.__doc__} \n and name of function: <{func.__name__}>")
print(func(4, 4, 4))


# you called func(4, 4, 4)
# it returned 6

# 4. type_check
# you should be able to pass 1 argument to decorator - type.
# decorator should check if the input to the function is correct based on type.
# If it is wrong, it should print(f"Wrong Type: {type}"), otherwise function should be executed.

def type_check(correct_type):
    def import_times2(func):
    # put code here
        @wraps(func)
        def inner(args):
            if isinstance(args, correct_type):
                return func(args)
            return print(f"Wrong Type: {type(args)} it should be {correct_type}")

        return inner
    return import_times2


@type_check(int)
def times2(num):
    return num * 2


print(times2(2))
times2('Not A Number')  # "Wrong Type: string" should be printed, since non-int passed to decorated function


@type_check(str)
def first_letter(word):
    return word[0]


print(first_letter('Hello World'))
first_letter(['Not', 'A', 'String'])  # "Wrong Type: list" should be printed, since non-str passed to decorated function
