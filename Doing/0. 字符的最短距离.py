# coding: utf-8

def shortestToChar(S, C):
    n = len(S)-1
    res = []
    for i in range(n+1):     #遍历字符串
        x = 0
        while True:
            if 0<=(i-x)<=n:         #判断左查找索引是否存在
                if S[i-x] == C:
                    res.append(x)
                    print "1--> i=%s, x=%s, res=%s" % (i, x, res)
                    break
            if 0<=(i+x)<=n:         #判断右查找索引是否存在
                if S[i+x] == C:
                    print "2--> i=%s, x=%s, res=%s" % (i, x, res)
                    res.append(x)
                    break
            x += 1
    return res

S = "loveleetcode"
C = 'e'

print(shortestToChar(S, C))