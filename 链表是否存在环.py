# coding: utf-8
class Node(object):
    def __init__(self, data, next=None):
        self.val = data
        self.next = next

def hasCycle(head):
	fast = slow = head
	while slow and fast and fast.next:
		slow = slow.next
		fast = fast.next.next
		if slow is fast:
			return True
	return False

# # 测试用例
if __name__ == '__main__':
    l1 = Node(3)
    l1.next = Node(2)
    l1.next.next = Node(1)
    l1.next.next.next = Node(5)
    l1.next.next.next.next = Node(9)
    l1.next.next.next.next.next = l1.next.next
    print (l1.val, l1.next.val, l1.next.next.val, l1.next.next.next.val, l1.next.next.next.next.val, l1.next.next.next.next.next.val)
    print hasCycle(l1)