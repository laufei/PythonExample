# coding: utf-8

# @Time    : 2019/8/3 9:37 PM
# @Author  : 'liufei'
# @Email   : fei.liu@qyer.com
# @File    : requests.py
# @Software: PyCharm

import requests
def testFunc(url):
    s = requests.Session()
    response = s.get(url=url, params={'wd': 'datadance'})
    return response.text

url = "https://www.baidu.com/s"
print testFunc(url)