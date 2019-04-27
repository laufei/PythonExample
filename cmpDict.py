# coding: utf-8
__author__ = 'liufei'

def cmpDict(d_from_db, d_from_page):
    keys = d_from_db.keys()
    result = {}
    for k in keys:
        if d_from_db[k] != d_from_page[k]:
            result[k] = "d_from_db:%s, d_from_page:%s" % (d_from_db[k], d_from_page[k])
    return result


a = {1:2, 2:3, 3:4}
b = {1:2, 3:3, 2:5}

print cmpDict(a, b)