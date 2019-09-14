# coding: utf-8

# @Time    : 2019/9/3 12:14 PM
# @Author  : 'liufei'
# @Email   : fei.liu@qyer.com
# @File    : 括号是否合法.py
# @Software: PyCharm

def isValid_1(s):
    stack = []
    paren_map = {")": "(", "]": "[", "}": "{"}
    for c in s:
        if c not in paren_map:
            stack.append(c)
        elif not stack or paren_map[c] != stack.pop():
            return False
    return not stack

def isValid_2(s):
    """
        三种失败的情况:
        1. [(}]   2. [])  3. ([]
    """
    stack = []
    paren_map = {"(": ")", "[": "]", "{": "}"}
    for c in s:
        if c in paren_map:
            stack.append(c)
        elif not stack:
            return False   # 覆盖失败情况1, 2
        elif paren_map[stack[-1]] == c:
            stack.pop()
    return not stack      # 覆盖失败情况3

print(isValid_1("({(){}[{}()]})"))
print(isValid_2("({(){}[{}()]})"))
print(isValid_1("([})"))
print(isValid_2("([})"))
print(isValid_1("([]"))
print(isValid_2("([]"))
print(isValid_1("[])"))
print(isValid_2("[])"))
