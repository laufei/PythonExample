# coding: utf-8

# @Time    : 2019/7/31 6:39 PM
# @Author  : 'liufei'
# @Email   : fei.liu@qyer.com
# @File    : 三数之和.py
# @Software: PyCharm

'''
给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？找出所有满足条件且不重复的三元组。
注意：答案中不可以包含重复的三元组。
'''

def testFun(list):
    result = []
    list_len = len(list)
    for i in range(list_len - 2):
        a = list[i]
        for j in range(i+1, list_len - 1):
            b = list[j]
            for k in range(j+1, list_len):
                c = list[k]
                tmp_list = [a, b, c]
                if sum(tmp_list) == 0:
                    r = sorted(tmp_list)
                    if r not in result:
                        result.append(r)
    return result

if __name__ == "__main__":
    list = [1,-1,-1,0]
    print testFun(list)