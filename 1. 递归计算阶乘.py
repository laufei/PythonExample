# coding: utf-8

def testFunc(n):
    if n == 1:
        return 1
    else:
        return n * testFunc(n - 1)
if __name__ == "__main__":
    print testFunc(5)