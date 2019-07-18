'''
正则使用方法：
-match:从开始位置开始查找，一次匹配
-search:从任何位置查找，一次匹配
-finall：把符合条件的全部查找出来

'''



import re

s = r'([a-z]+)([a-z]+)'
pattern = re.compile(s,re.I) #re.I标识忽略大小写

m = pattern.match("hello  world wide web")
all  =pattern.findall("hello  world wide web")
print(all)
print(type(all))
for i in all:
    print(i)

s = m.group(0)
print(s)

a = m.span(0)
print(a)

s = m.group(1)
print(s)

a = m.span(1)
print(a)

a = m.span(2)
print(a)


print(".................")
s = m.groups()
print(s)

print(".............")
all  =pattern.finditer("hello  world wide web")
print(all)
print(type(all))
for i in all:
    print(i)