# coding: utf-8

def testFun(str):
    strLen = len(str)
    if not strLen:
        raise Exception, "输入的字符串长度不能为0"
    elif 1 == strLen:
        return str

    indexBegin = 0
    indeEnd = 1
    for i in range(strLen-1):
        tmp = 1
        for j in range(i+1, strLen):
            if str[i] == str[j]:
                tmp += 1
            else:
                break
        if tmp > indeEnd:
            indexBegin = i
            indeEnd = tmp
    return str[indexBegin:indexBegin+indeEnd]

if __name__ == "__main__":
    str1 = "ffffa"
    str2 = "f"
    str3 = "faff"
    str4 = "ffffabbbbb"
    str5 = "xxxxxxxxxxabbbdddcccfffffffff"
    str6 = "xxxxxx"
    print testFun(str1)
    print testFun(str2)
    print testFun(str3)
    print testFun(str4)
    print testFun(str5)
    print testFun(str6)