#_*_coding:utf-8_*_
#file: NewtonSolve.py
# 牛顿迭代法求解线性方程组,进行求解的是在1附近的根
import math
import numpy as np
from numpy import *
import matplotlib.pyplot as plt

def Fun(x,num):
    """方程组在这里，三个变量分别是x的三个分量，
        num是未知数个数，这里是3，f是三个方程组
    """
    i = num
    f = np.zeros((i),dtype=float)
    f[0] = x[0]*x[1]-x[2]*x[2]-1.
    f[1] = x[0]*x[1]*x[2]+x[1]*x[1]-x[0]*x[0]-2.
    f[2] = math.exp(x[0])+x[2]-math.exp(x[1])-3.
    return f

def dfun(x,num):
    """计算雅可比矩阵的逆矩阵"""
    df = np.zeros((num,num),dtype=float)
    dx = 0.00001
    x1 = np.copy(x)
    for i in range(0,num):              # 求导数，i是列，j是行
        for j in range(0,num):
            x1 = np.copy(x)
            x1[j] = x1[j]+dx           #x+dx
            df[i,j] = (Fun(x1,num)[i]-Fun(x,num)[i])/dx   #f(x+dx)-f（x）/dx
    df_1 = np.linalg.inv(df)                              #计算逆矩阵
    return df_1

def Newton(x,num):
    x1 = np.copy(x)
    i = 0
    delta = np.copy(x)
    #dfun0=dfun(x,num)          #也可以使用简化牛顿法
    while(np.sum(abs(delta)) > 1.e-8 and i < 20):  #控制循环次数
        x1 = x-dot(dfun(x,num),Fun(x,num))  #公式
        delta = x1-x                     #比较x的变化
        x = x1
        i = i+1
        print(x)
    return x

if __name__=='__main__':
    num =3                      # 方程未知数的个数
    x = np.ones((num),dtype=float)#初始值
    a = Newton(x,num)
    print(a)