# coding: utf-8
class Solution(object):
    def __init__(self):
        self.r, self.t = 1, 1
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = len(s)
        if l == 0:
            return 0
        for i in range(l-1):
            rl = [s[i]]
            for j in range(i+1, l):
                rl.append(s[j])
                if len(rl) == len(list(set(rl))):
                    self.t +=1
                    if self.t > self.r:
                        self.r = self.t
                        print "[%s, %s]" % (i, j), self.t, self.r, rl
            else:
                self.t = 1
        return self.r

print Solution().lengthOfLongestSubstring("aaaaaaaaaaaabbbbbbbbbbbbbbbbbbcccccccccccccdasdfaea4rq34yw46io6798pu;i")