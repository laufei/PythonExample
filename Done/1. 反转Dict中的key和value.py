# coding: utf-8

# @Time    : 2019/8/25 8:29 PM
# @Author  : 'liufei'
# @Email   : fei.liu@qyer.com
# @File    : 反正Dict中的key和value.py
# @Software: PyCharm

d = {'a': 1, 'b': 2, 'c': 3}
def revert_dict(source):
    return dict((v, k) for k, v in d.items())
if __name__ == "__main__":
    print revert_dict(d)