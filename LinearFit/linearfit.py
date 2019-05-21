#_*_coding:utf-8_*_
#file: linearfit.py

import numpy as np
from matplotlib import pyplot as plt
import xlrd

def linearfit(x,y):
    #构造系数矩阵A
    A=[]
    A.append(len(x))
    A.append(sum(x))
    A.append(sum(x))
    A.append(sum(x*x))
    A=np.array(A).reshape(2,2)
    #构造矩阵b
    b=[]
    b.append(sum(y))
    b.append(sum(x*y))
    b=np.array(b).reshape(2,1)
    #求解线性方程组，返回结果
    return np.linalg.inv(A).dot(b)

if __name__ == '__main__':
    #从文件中读取数据
    ExcelFile = xlrd.open_workbook(r'data.xlsx')
    sheet = ExcelFile.sheet_by_index(0)
    cols_1 = sheet.col_values(0)
    cols_2 = sheet.col_values(1)
    # 剔除数据的表头
    x = np.array(cols_1[1:])
    y = np.array(cols_2[1:])
    #调用拟合函数得到结果
    ans = linearfit(x, y)
    print("得到的拟合直线方程为:\t" + "y=" + str(ans[(0, 0)]) + str(ans[(1, 0)]) + "*x")
    #绘制图像
    x_ = np.arange(0, 8, 1)
    y_ = ans[(0, 0)] + ans[(1, 0)] * x_
    plt.scatter(x, y)
    plt.plot(x_, y_)
    plt.show()
    #残差分析
    print("模型的残差平方和为:"+str(sum((y - (ans[(0, 0)] + ans[(1, 0)] * x)) * (y - (ans[(0, 0)] + ans[(1, 0)] * x)))))