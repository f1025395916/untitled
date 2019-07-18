import  re

s =r"\d+"   #r表示原生字符串，不需要转义

pattern = re.compile(s)

# 从3开始找，到10结束
# 返回一个math对象，找到一个math对象就返回
m = pattern.match("one123two456",3,10)
#
print(m)
print(m.group())
print(type(m))

print(m.start(0))

print(m.end(0))
print(m.span(0))