

# 冒泡排序：
循环次数为元素数量，循环完一次最后一个数固定不再循环

arr = [5,6,3,1,15,24,10,13]
for i in range(len(arr)-1):  #设置循环的次数
    for j in range(len(arr)-i-1): # j为列表下标
        if arr[j] >arr[j+1]:
            arr[j],arr[j+1] = arr[j+1],arr[j]
print(arr)



