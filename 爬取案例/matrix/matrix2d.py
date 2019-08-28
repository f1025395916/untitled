'''
二维矩阵类
'''

class Matrix2D:
    """ 通用的二维矩阵类"""


    def __init__(self,rows,cols):
        '''初始化矩阵row行，col列'''
        self.grid = [[0]*cols for _ in range(rows) ]
        self.rows = rows
        self.cols = cols
    def get_cell(self,r,c):
        """获取单元格(r,c)的值"""
        return self.grid[r][c]

    def set_cell(self,n,  *args):
        """设置某个位置的值"""
        for r,c in args:
            self.grid[r][c] = n

    def inc_cells(self,*args):
        """将任意的单元格+1"""
        for r,c in args:
            self.grid[r][c] +=1

    def set_all_cells(self,n=0):
        """将所有单元格都设置为n"""
        for i in range(self.rows):
            for j in range(self.cols):
                self.grid[i][j] = n



















