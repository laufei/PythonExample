# coding: utf-8

for n in range(2, 1001):
    tmp = 0
    items = []
    for i in range(1, n):
        if n % i == 0:
            tmp += i
            items.append(i)
    if tmp == n:
        print tmp
        print items
