# coding: utf-8
'''
题目：有n个整数，使其前面各数顺序向后移m个位置，最后m个数变成最前面的m个数
'''

# coding: utf-8
def fn(array, m):
    n = len(array)
    for t in range(m):
        tmp = array[n-1]
        for i in range(n-1, -1, -1):
            array[i] = array[i-1]
        array[0] = tmp

a = [2, 8, 6, 1, 78, 45, 34, 2]
fn(a, 7)
print a