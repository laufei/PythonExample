# coding: utf-8

# @Time    : 2019/5/15 11:10 AM
# @Author  : 'liufei'
# @Email   : fei.liu@qyer.com
# @File    : 汉诺塔步数.py
# @Software: PyCharm

class Hanio:

    i = 0
    def move(self, n, f, t):
        print "第%d步: 将%d号盘子%s---->%s\n" % (self.i+1, n, f, t)

    def Hanio(self, n, start_pos, tranc_pos, end_pos):
        '''
        汉诺塔递归函数
        n表示要将多少个"圆盘"从起始柱子移动至目标柱子
        start_pos表示起始柱子,tran_pos表示过渡柱子,end_pos表示目标柱子
        '''
        if n == 1:
            self.move(n, start_pos, end_pos)
        else:
            Hanio(n-1, start_pos, end_pos, tranc_pos)
            self.move(n, start_pos, end_pos)
            Hanio(n-1, tranc_pos, start_pos, end_pos)

if __name__ == '__main__':
    Hanio().Hanio(3, 'a', 'b', 'c')