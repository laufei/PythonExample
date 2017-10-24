# coding:utf-8
#递归：求5!

def digui(n):
    if n==1:
        return 1
    else:
        return n*digui(n-1)

print digui(5)