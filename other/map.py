# coding: utf-8
__author__ = 'liufei'

def format_name(s):
    s1=s[0:1].upper()+s[1:].lower();
    return s1;

l = ['adam', 'LISA', 'barT']
print map(format_name, l)
print l