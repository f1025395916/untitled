# -*- coding: utf-8 -*-

with open(r'F:\123.txt',mode="r+") as file:
    file.write('zzzz')
    content = file.read()
    print("123")
    print(content)