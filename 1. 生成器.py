# coding: utf-8

# 28. 生成器 & 迭代器练习
# 生成器: 在Python中，这种一边循环一边计算的机制，称为生成器：generator
# python中生成器是迭代器的一种，使用yield返回值函数，每次调用yield会暂停，而可以使用next()函数和send()函数恢复生成器。

l = [1, 2, 3, 4, 5, 6, 7, 8]
ll = map(lambda x: x+2, l)
lll = reduce(lambda x,y: x*y, l)
llll = [i+2 for i in l]
print ll
print lll
print llll

generator = (i+2 for i in l)
print generator.next()
print generator.send(i)
print next(generator)
print '---------'
for i in generator:
    print i

def foo():
    print("starting...")
    while True:
        res = yield 4
        print("res:",res)
g = foo()
print(next(g))
print("*"*20)
print(next(g))
print(g.send(44))

def fib():
    i = 10
    a, b = 1, 1
    while i > 0:
        i -= 1
        yield a, b
        a, b = b, a+b

fib = fib()
for i in range(20):
    try:
        print fib.next()
    except StopIteration as e:
        break