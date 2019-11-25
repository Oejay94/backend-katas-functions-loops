#!/usr/bin/env python
"""Implements math functions without using operators except for '+' """

__author__ = "Joey Brown with help from Coaches and Google"


def add(x, y):
    return x + y
    


def multiply(x, y):
    total = 0
    for a in range(y):
        total = add(x, total)
    return total

   

def power(x, n):
    total = x
    for a in range(n-1):
        total = multiply(x, total)
    return total


def factorial(x):
    total = x
    for a in range(x, 1, -1):
        total = multiply(total, a-1)
    return total


def fibonacci(n):
    a = 0
    b = 1
    for i in range(0, n):
        temp = a
        a = b
        b = temp + b
    return a




if __name__ == '__main__':
    print(add(2, 4))
    print(multiply(6, -8))
    print(power(2, 8))
    print(factorial(4))
    print(fibonacci(8))
    pass
