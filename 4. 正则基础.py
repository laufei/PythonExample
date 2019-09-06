# coding: utf-8

# @Time    : 2019/7/30 4:32 PM
# @Author  : 'liufei'
# @Email   : fei.liu@qyer.com
# @File    : 正则基础.py
# @Software: PyCharm

import re
# 1) re.match
print(re.match('www', 'www.runoob.com').span())  # 在起始位置匹配
print(re.match('com', 'www.runoob.com'))         # 不在起始位置匹配

# 2)
# re.MatchObject
# group() 返回被 RE 匹配的字符串。
# start() 返回匹配开始的位置
# end() 返回匹配结束的位置
# span() 返回一个元组包含匹配 (开始,结束) 的位置

line = "Cats are smarter than dogs"
matchObj = re.match( r'(.*) are (.*?) .*', line, re.M|re.I)
if matchObj:
   print "matchObj.group() : ", matchObj.group()
   print "matchObj.group(1) : ", matchObj.group(1)
   print "matchObj.group(2) : ", matchObj.group(2)
else:
   print "No match!!"

# 3) re.search
print(re.search('www', 'www.runoob.com').span())  # 在起始位置匹配
print(re.search('com', 'www.runoob.com'))         # 不在起始位置匹配

 # 4)
line = "Cats are smarter than dogs";
searchObj = re.search( r'(.*) are (.*?) .*', line, re.M|re.I)
if searchObj:
   print "searchObj.group() : ", searchObj.group()
   print "searchObj.group(1) : ", searchObj.group(1)
   print "searchObj.group(2) : ", searchObj.group(2)
else:
   print "Nothing found!!"

# 5) re.sub
phone = "2004-959-559 # 这是一个国外电话号码"
# 删除字符串中的 Python注释
num = re.sub(r'#.*$', "", phone)
print "电话号码是: ", num
# 删除非数字(-)的字符串
num = re.sub(r'\D', "", phone)
print "电话号码是 : ", num

# 6) re.sub
# 将匹配的数字乘以 2
def double(matched):
    value = int(matched.group('value'))
    return str(value * 2)

s = 'A23G4HFD567'
print(re.sub('(?P<value>\d+)', double, s))

# 7) re.compile
# re.RegexObject
# re.compile() 返回 RegexObject 对象。
pattern = re.compile(r'\d+')                    # 用于匹配至少一个数字
m = pattern.match('one12twothree34four', 3, 10) # 从'1'的位置开始匹配，正好匹配s
print m.group(0)   # 可省略 0
print m.start(0)   # 可省略 0
print m.end(0)     # 可省略 0
print m.span(0)    # 可省略 0

# 8) re.findall
pattern = re.compile(r'\d+')   # 查找数字
result1 = pattern.findall('runoob 123 google 456')
result2 = pattern.findall('run88oob123google456', 0, 10)
print result1
print result2

# 9) re.finditer
pattern = re.compile(r'\d+')   # 查找数字
it = pattern.finditer("12a32bc43jf3")
for match in it:
    print (match.group())

# 10) re.split
print re.split('\W+', 'runoob, runoob, runoob.')
print re.split('(\W+)', ' runoob, runoob, runoob.')
print re.split('\W+', ' runoob, runoob, runoob.', 1)
print re.split('a*', 'hello world')   # 对于一个找不到匹配的字符串而言，split 不会对其作出分割