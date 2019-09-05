# coding: utf-8

class myNode():
    def __init__(self, value=None):
        self._value = value
        self._next = None

    def setVal(self, value):
        self._value = value

    def setNext(self, node):
        self._next = node

    def getVal(self):
        return self._value

    def getNext(self):
        return self._next

class mySlinkedList():
    def __init__(self):
        self._head = None

    # 头部新增节点
    def add(self, value):
        tmp = myNode(value)
        tmp.setNext(self._head)
        self._head = tmp

    # 尾部新增节点
    def append(self, value):
        tmp = myNode(value)
        if self.isEmpty():
            self._head = tmp
        else:
            current = self._head
            while current.getNext() is not None:
                current = current.getNext()
            current.setNext(tmp)

    # 是否存在某个节点数据
    def search(self, value):
        found = False
        current = self._head
        while current is not None:
            if current.getVal() == value:
                found = True
                break
            else:
                current = current.getNext()
        return found

    # 某个节点数据的位置
    def index(self, value):
        found = False
        current = self._head
        index = 0
        while current is not None:
            if current.getVal() == value:
                found = True
                break
            else:
                index += 1
                current = current.getNext()
        if found:
            return index
        else:
            raise ValueError, '%s is not in linkedlist' % value

    # 删除某个节点
    def remove(self, value):
        current = self._head
        pre = None
        while current is not None:
            if current.getVal() == value:
                if not pre:
                    self._head = current.getNext()
                else:
                    pre.setNext(current.getNext())
                break
            else:
                pre = current
                current = current.getNext()

    # 在某个位置插入节点
    def insert(self, index, value):
        index = int(index)
        new = myNode(value)
        if index <= 1:
            self.add(value)
        elif index > self.size():
            self.append(value)
        else:
            current = self._head
            pre = None
            count = 1
            while current is not None:
                if count == index:
                    pre.setNext(new)
                    new.setNext(current)
                    break
                else:
                    pre = current
                    current = current.getNext()
                    count += 1

    # 是否为空
    def isEmpty(self):
        return self._head is None

    # 链表长度
    def size(self):
        count = 0
        current = self._head
        while current is not None:
            count += 1
            current = current.getNext()
        return count

    # 遍历链表
    def getList(self):
        current = self._head
        while current is not None:
            print current.getVal()
            current = current.getNext()

if __name__ == "__main__":
    n1 = myNode("Mon")
    n2 = myNode("Wed")
    n3 = myNode("Sat")
    n4 = myNode("Tue")
    n5 = myNode("Sun")

    n1.setNext(n4)
    n4.setNext(n2)
    n2.setNext(n3)
    n3.setNext(n5)

    h = n1
    while h is not None:
        print h.getVal()
        h = h.getNext()

    sl = mySlinkedList()
    print "该链表是否为空", sl.isEmpty()
    sl.add("Liu")
    sl.append("Fei")
    print "该链表是否为空", sl.isEmpty()
    sl.getList()
    print "该链表长度为:", sl.size()
    print '------------------------------------'
    print sl.search("Luca")
    print sl.search("Fei")
    print '------------------------------------'
    sl.append("Luca")
    sl.append("xhn")
    sl.getList()
    print '------------------------------------'
    print sl.index("xhn")
    sl.remove("xhn")
    sl.getList()
    print '------------------------------------'
    sl.insert(5, "xiaonan")
    sl.getList()
    print '------------------------------------'
    sl.insert(1, "tanxin")
    sl.getList()
    print '------------------------------------'
    sl.insert(3, "xiaopeng")
    sl.getList()