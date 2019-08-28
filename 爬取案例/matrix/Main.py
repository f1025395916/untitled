'''
生命游戏
'''

from 爬取案例.matrix import matrix2d

rows = 5
cols = 5
# 存储图符号的二维数组
life_mat = matrix2d.Matrix2D(rows,cols)

# 存储具体数据的二维数组
nc_mat = matrix2d.Matrix2D(rows,cols)
# 初始化
life_mat.set_cell(1, (1, 3), (2, 1), (2, 3), (3, 2), (3, 3))
# 创建边界字符串
border_str  = ' _ '* cols

def get_mat_str(a_mat):
    """处理打印字符串"""
    disp_str = ""
    for i in range(rows):
        lst = [get_chr(a_mat,i,j) for j in range(cols)]
        disp_str +="".join(lst) +"\n"
    return  disp_str

def get_chr(a_mat,r,c):
    """设置图符号"""
    return ' 1 ' if a_mat.get_cell(r, c) > 0 else ' 0 '

def do_generation():
    """打印当前状态并生成下个状态"""
    print(border_str + '\n' +get_mat_str(life_mat) )
    # 把数据全部置0
    nc_mat.set_all_cells(0)

    # 根据图符号矩阵life_mat 来给nc_mat 赋值

    for i in range(rows):
        for j in range(cols):
            if life_mat.get_cell(i,j):
                # 环绕图像，使有限的二维数组变成没有边界的生命游戏
                im = (i-1) % rows
                ip = (i+1) % rows     # 当前行号-/+1
                jm = (j-1) % rows
                jp = (j+1) % rows     # 当前行号-/+1
                # 设置数据量为1，表示有活细胞
                nc_mat.inc_cells((im,jm),(im,j),(im,jp),(i,jm),
                                 (i,jp),(ip,jm),(ip,j),(ip,jp))
    # 根据邻居数量矩阵按规则生成下一代
    for i in range(rows):
        for j in range(cols):
            n = nc_mat.get_cell(i,j)
            if n<2 or n>3:       # 死亡现象
                life_mat.set_cell(0,(i,j))
            elif n==3:           # 繁殖现象
                life_mat.set_cell(1,(i,j))

import  time
n = 100
for i in range(n):
    # 循环调用迭代
    do_generation()
    # 设置间隔时间
    time.sleep(1)

















