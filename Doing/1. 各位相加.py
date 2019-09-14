# coding: utf-8

def addDigits(num):
    result = 0
    while num > 9:
        a, b = num/10, num % 10
        result = a + b
        num = result
    return result

print addDigits(98)