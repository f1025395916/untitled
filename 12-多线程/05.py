

def odd():
    print("Step 1")
    yield  1
    print("Step 2")
    yield  2
    print("Step 3")
    yield 3
#odd 是调用生成器
g=odd()
one = next(g)
print(one)
two = next(g)
print(two)
three = next(g)
print(three)