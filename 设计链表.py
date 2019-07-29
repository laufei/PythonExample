# coding: utf-8

# @Time    : 2019/5/14 3:58 PM
# @Author  : 'liufei'
# @Email   : fei.liu@qyer.com
# @File    : 设计链表.py
# @Software: PyCharm

class Node(object):
    def __init__(self, value, next=None):
        self._value = value
        self._next = next

    def getValue(self):
        return self._value

    def getNext(self):
        return self._next

    def setValue(self, value):
        self._value = value

    def setNext(self, node):
        self._next = node

class MyLinkedList(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._head = None

    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        :type index: int
        :rtype: int
        """
        count = 1
        current = self._head
        while current is not None:
            if count == int(index):
                return current.getValue()
            else:
                current = current.getNext()
                count += 1
        return -1

    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        :type val: int
        :rtype: None
        """
        new = Node(val)
        new.setNext(self._head)
        self._head = new

    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: None
        """
        new = Node(val)
        if self._head is None:
            self._head = new
        else:
            current = self._head
            while current.getNext() is not None:
                current = current.getNext()
            current.setNext(new)

    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        :type index: int
        :type val: int
        :rtype: None
        """
        new = Node(val)
        if index <= 1:
            self._head = new
        else:
            pos = 2
            pre = None
            current = self._head
            while current is not None:
                if index == pos:
                    new.setNext(current.getNext())
                    pre.setNext(new)
                else:
                    pre = current
                    current = current.getNext()
                    pos += 1

    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: None
        """
        if index <= 1:
            self._head = None
        else:
            pos = 2
            pre = None
            current = self._head
            while current is not None:
                if index == pos:
                    pre.setNext(current.getNext)
                else:
                    pre = current
                    current = current.getNext()
                    pos += 1

# Your MyLinkedList object will be instantiated and called as such:
obj = MyLinkedList()
obj.addAtHead(1)
obj.addAtTail(3)
param_1 = obj.get(2)
print param_1
obj.addAtIndex(2,2)
obj.deleteAtIndex(3)