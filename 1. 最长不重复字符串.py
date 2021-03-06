# coding: utf-8


def testFun(str):
    str_len = len(str)
    if str_len < 2:
        return str
    index_begin = 0
    index_end = 1
    for i in range(str_len-1):
        tmp = 1
        tmp_list = [str[i]]
        for j in range(i+1, str_len):
            tmp_list.append(str[j])
            if all([str[i] != str[j], len(set(tmp_list)) == len(tmp_list)]):
                tmp += 1
            else:
                break
        if tmp > index_end:
            index_begin = i
            index_end = tmp
    return str[index_begin: index_begin+index_end]


if __name__ == "__main__":
    str1 = "aaabbbbcccccaaaaaabcd"
    str2 = "aa"
    str3 = "a"
    str4 = "abccccccccccccccc"
    print testFun(str1)
    print testFun(str2)
    print testFun(str3)
    print testFun(str4)