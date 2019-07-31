# coding: utf-8

# @Time    : 2019/7/31 10:26 AM
# @Author  : 'liufei'
# @Email   : fei.liu@qyer.com
# @File    : 二叉树遍历-递归.py
# @Software: PyCharm

class Node(object):
    def __init__(self, data, next=None):
        self.val = data
        self.next = next

def fun4(head):
    if head == None:
        return None
    L,M,R = None,None,head
    while R.next != None:
        L = M
        M = R
        R = R.next
        M.next = L
    R.next = M
    return R
#测试用例
if __name__ == '__main__':
    l1 = Node(3)
    l1.next = Node(2)
    l1.next.next = Node(1)
    l1.next.next.next = Node(9)
    l = fun4(l1)
    print (l.val, l.next.val, l.next.next.val, l.next.next.next.val)