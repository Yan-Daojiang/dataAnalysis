#_*_coding:utf-8_*_
#file: newton.py

#牛顿插值
def newton(X,Y,x):
    """X,Y为已知条件
        x为被插节点
        函数返回被插节点处所插结果"""
    n=len(X)
    #构造差商表
    for j in range(1,n):
        for i in range(n-1,j-1,-1):
            Y[i]=(Y[i]-Y[i-1])/(X[i]-X[i-j])
    #牛顿插值
    y=Y[n-1]
    for i in range(n-2,-1,-1):
        y=Y[i]+(x-X[i])*y
    return y