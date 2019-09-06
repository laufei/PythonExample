# coding: utf-8

# @Time    : 2019/7/30 5:52 PM
# @Author  : 'liufei'
# @Email   : fei.liu@qyer.com
# @File    : 字典排序.py
# @Software: PyCharm

from collections import OrderedDict
dict = {
            8: {'k': 8, 'v': 'eight'},
            2: {'k': 2, 'v': 'two'},
            1: {'k': 1, 'v': 'one'},
            10: {'k': 10, 'v': 'ten'},
}
result = OrderedDict(sorted(dict.items(), key=lambda x:x[0]))
print dict.items()
print result.items()