# coding: utf-8

# @Time    : 2019/7/29 2:42 PM
# @Author  : 'liufei'
# @Email   : fei.liu@qyer.com
# @File    : 最长不重复字符串.py
# @Software: PyCharm

def testFun(str):
    sLen = len(str)
    if not sLen:
        raise Exception, "输入的字符串长度不能为0"
    elif 1 == sLen:
        return str

    index = 0
    rLen = 1
    for i in range(sLen-1):
        tmp = 0
        for j in range(i+1, sLen):
            a = len(set(str[i:j]))
            b = len(str[i:j])
            if a == b:
                tmp += 1
                print "i=%d, j=%d, a=%d, b=%d, tmp=%d" % (i, j, a, b, tmp)
            else:
                break
        if tmp > rLen:
            index = i
            rLen = tmp
    print index, rLen
    return str[index: index+rLen]

if __name__ == "__main__":
    str = "bccccdeeeeefadbbb"
    print testFun(str)