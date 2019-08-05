# coding: utf-8

# @Time    : 2019/7/29 2:42 PM
# @Author  : 'liufei'
# @Email   : fei.liu@qyer.com
# @File    : 最长不重复字符串.py
# @Software: PyCharm

def testFun(str):
    str_len = len(str)
    if str_len < 2:
        return str_len

    result = 1
    begin = 0
    tmp_list = []
    for i in range(str_len - 1):
        tmp = 1
        tmp_list.append(str[i])
        for j in range(i+1, str_len):
            tmp_list.append(str[j])
            if len(set(tmp_list)) == len(tmp_list):
                tmp += 1
                if tmp > result:
                    result = tmp
                    begin = i
            else:
                tmp_list = []
                break
    return str[begin:begin+result]


if __name__ == "__main__":
    str = "aaabbbbcccccaaaaaabcd"
    print testFun(str)