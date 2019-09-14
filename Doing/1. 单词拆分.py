# coding: utf-8

def wordBreak(s, wordDict):
    if not s:
        return False

    breakp = [0]

    for i in range(len(s) + 1):
        for j in breakp:
            if s[j:i] in wordDict:
                breakp.append(i)
                break
    return breakp[-1] == len(s)

s = "aaaaaaa"
wordDict = ["aa", "aaaaa"]
print wordBreak(s, wordDict)