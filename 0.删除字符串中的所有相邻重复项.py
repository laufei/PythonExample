# coding: utf-8

def removeDuplicates(S):
    """
    :type S: str
    :rtype: str
    """
    # 初始化栈
    stack = []
    # 遍历栈元素
    for e in S:
        if stack and stack[-1] == e:
            stack.pop()
        else:
            stack.append(e)
    return "".join(stack)

S = "abbaca"
print(removeDuplicates(S))