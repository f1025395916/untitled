import  re

s = r'\d+'

pattern = re.compile(s)
m = pattern.search("one51sdg556aaa555")
print(m.group())


m = pattern.search("one51sdg556aaa555",10,40)
print(m.group())

