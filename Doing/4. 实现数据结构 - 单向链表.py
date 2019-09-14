# coding: utf-8

# @Time    : 2019/7/30 8:34 PM
# @Author  : 'liufei'
# @Email   : fei.liu@qyer.com
# @File    : 实现数据结构 - 单向链表.py
# @Software: PyCharm

class Node():
    __slots__ = ['_item','_next']
    def __init__(self,item):
        self._item = item
        self._next = None

    def getItem(self):
        return self._item

    def getNext(self):
        return self._next

    def setItem(self, newitem):
        self._item = newitem

    def setNext(self, newnext):
        self._next = newnext

class SingleLinkedList():
    def __init__(self):
        self._head = None  #初始化为空链表

    # 是否为空
    def isEmpty(self):
        return self._head == None

    # 链表长度
    def size(self):
        current = self._head
        count = 0
        while current != None:
            count += 1
            current = current.getNext()
        return count

    # 遍历链表
    def travel(self):
        current = self._head
        while current != None:
            print current.getItem()
            current = current.getNext()

    # 头部新增节点
    def add(self, item):
        temp = Node(item)
        temp.setNext(self._head)
        self._head = temp

    # 尾部新增节点
    def append(self, item):
        temp = Node(item)
        if self.isEmpty():
            self._head = temp   #若为空表，将添加的元素设为第一个元素
        else:
            current = self._head
            while current.getNext() != None:
                current = current.getNext()   #遍历链表
            current.setNext(temp)   #此时current为链表最后的元素

    # 是否存在某个节点数据
    def search(self, item):
        current = self._head
        founditem = False
        while current != None:
            if current.getItem() == item:
                founditem = True
                break
            else:
                current = current.getNext()
        return founditem

    # 某个节点数据的位置
    def index(self, item):
        current = self._head
        count = 0
        found = None
        while current != None and not found:
            count += 1
            if current.getItem() == item:
                found = True
            else:
                current = current.getNext()
        if found:
            return count
        else:
            raise ValueError, '%s is not in linkedlist' % item

    # 删除某个节点
    def remove(self, item):
        current = self._head
        pre = None
        while current != None:
            if current.getItem() == item:
                if not pre:
                    self._head = current.getNext()
                else:
                    pre.setNext(current.getNext())
                break
            else:
                pre = current
                current = current.getNext()

    # 在某个位置插入节点
    def insert(self, pos, item):
        if pos <= 1:
            self.add(item)
        elif pos > self.size():
            self.append(item)
        else:
            temp = Node(item)
            count = 1
            pre = None
            current = self._head
            while count < pos:
                count += 1
                pre = current
                current = current.getNext()
            pre.setNext(temp)
            temp.setNext(current)

if __name__ == '__main__':
    a=SingleLinkedList()
    for i in range(1,10):
        a.append(i)
    print a.size()
    a.travel()
    print a.search(6)
    print a.index(5)
    a.remove(4)
    a.travel()
    a.insert(4,100)
    a.travel()