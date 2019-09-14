# coding: utf-8

def removeDuplicates(S):
    stack = []
    for i in S:
        if stack and stack[-1] == i:
            stack.pop(-1)
        else:
            stack.append(i)
    return "".join(stack)

S = "abbaca"
print(removeDuplicates(S))