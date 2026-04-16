s = open("C:\\Users\\olesy\\Downloads\\24-345(1).txt").readline()
from re import *
num = "[1-9ABCD][0-9A-D]+[02468AC]"
reg = rf"{num}"
m = max(findall(reg, s), key=len)
ind = s.find(m)
print(ind)