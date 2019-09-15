# coding: utf-8

class Node(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def deleteDuplicates(head):
    p = head
    # 当前节点存在并且当前节点的next指向也存在，就遍历链表
    while p and p.next:
        if p.val == p.next.val:
            p.next = p.next.next
        else:
            p = p.next
    return head

if __name__ == '__main__':
    l1 = Node(1)
    l1.next = Node(1)
    l1.next.next = Node(1)
    l1.next.next.next = Node(9)
    l1.next.next.next.next = Node(3)
    p = deleteDuplicates(l1)
    while p is not None:
        print p.val
        p = p.next
