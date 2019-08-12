import  numpy as np

a = np.array([1,2,3])

b = np.array([[1,2,3],[4,5,6],[7,8,9]])

b[1,1] = 10

# shape 查看矩阵或数组的维数
print(a.shape)

print(b.shape)


# dtype 查看数据元素的类型
print(a.dtype)