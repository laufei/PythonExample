# coding: utf-8

class Node(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def deleteDuplicates(head):
    p = head
    # 当前节点存在并且当前节点的next指向也存在，就遍历链表
    while p and p.next:
        # 判断当前节点与下一个节点的大小关系
        if p.val == p.next.val:
            # 如果相等就把当前节点的next指向下下个节点的next，也就是相当于把下一个节点给删除了
            p.next = p.next.next
        else:
            # 否则就继续判断下个节点与下下个节点间的关系
            p = p.next
    # 遍历完后，返回修改后的链表
    return p

if __name__ == '__main__':
    l1 = Node(1)
    l1.next = Node(1)
    l1.next.next = Node(1)
    l1.next.next.next = Node(9)
    print(deleteDuplicates(l1).val)
