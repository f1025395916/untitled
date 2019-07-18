import  re

patten = re.compile(r'\d+')
s = patten.findall('i am 18 yaers old  and 185 height')

print(s)

s = patten.finditer('i am 18 yaers old  and 185 height')

print(s)
print(type(s))

for i in s:
    print(i.group())


string = "hello there"
patten1 = re.compile('hello (\w+)')
math = patten1.match(string)

print(math.group(0))