# coding: utf-8

class Node(object):
    def __init__(self, data, next=None):
        self.val = data
        self.next = next

class test(object):
	def swapPairs(self, head):
		pre, pre.next = self, head
		while pre.next and pre.next.next:
			a = pre.next
			b = a.next
			pre.next, b.next, a.next = b, a, b.next
			pre = a
		return self.next

# # 测试用例
if __name__ == '__main__':
    l1 = Node(3)
    l1.next = Node(2)
    l1.next.next = Node(1)
    l1.next.next.next = Node(5)
    l1.next.next.next.next = Node(9)
    print (l1.val, l1.next.val, l1.next.next.val, l1.next.next.next.val, l1.next.next.next.next.val)
    l = test().swapPairs(l1)
    print (l.val, l.next.val, l.next.next.val, l.next.next.next.val, l.next.next.next.next.val)
