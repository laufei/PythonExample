# coding: utf-8

class Node(object):
    def __init__(self, data, next=None):
        self._val = data
        self._next = next

def reverseList(head):
    pass

# # 测试用例
if __name__ == '__main__':
    l1 = Node(3)
    l1._next = Node(2)
    l1._next._next = Node(1)
    l1._next._next._next = Node(5)
    l1._next._next._next._next = Node(9)
    print (l1._val, l1._next._val, l1._next._next._val, l1._next._next._next._val)
    l = reverseList(l1)
    print (l._val, l._next._val, l._next._next._val, l._next._next._next._val)