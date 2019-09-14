# coding: utf-8

def removeDuplicates(S):
    # 初始化栈
    stack = []
    # 遍历栈元素
    for e in S:
        if stack and stack[-1] == e:
            stack.pop(-1)
        else:
            stack.append(e)
    return "".join(stack)

S = "abbaca"
print(removeDuplicates(S))