# coding: utf-8

def kthSmallest(root, k):
    # 先广度优先遍历
    width = [root]
    val = [root.val]
    i = 0
    while i < len(width):
        cur = width[i]
        if cur.left is not None:
            width.append(cur.left)
            val.append(cur.left.val)
        if cur.right is not None:
            width.append(cur.right)
            val.append(cur.right.val)
        i += 1
    val.sort()

    return val[k-1]

root = [5, 3, 6, 2, 4, None, None, 1]
k = 3
print(kthSmallest(root, k))