# coding: utf-8

# @Time    : 2019/7/31 10:26 AM
# @Author  : 'liufei'
# @Email   : fei.liu@qyer.com
# @Software: PyCharm

'''
假设存在链表 1 → 2 → 3 → Ø，我们想要把它改成 Ø ← 1 ← 2 ← 3。
在遍历列表时，将当前节点的 next 指针改为指向前一个元素。由于节点没有引用其上一个节点，因此必须事先存储其前一个元素。
在更改引用之前，还需要另一个指针来存储下一个节点。不要忘记在最后返回新的头引用！
'''

class Node(object):
    def __init__(self, data, next=None):
        self.val = data
        self.next = next

def reverseList(head):
    pre = None
    cur = head
    while cur:
        tmp = cur.next
        cur.next = pre
        pre = cur
        cur = tmp
    return pre

#测试用例
if __name__ == '__main__':
    l1 = Node(3)
    l1.next = Node(2)
    l1.next.next = Node(1)
    l1.next.next.next = Node(9)
    l = reverseList(l1)
    print (l.val, l.next.val, l.next.next.val, l.next.next.next.val)