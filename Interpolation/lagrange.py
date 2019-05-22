#_*_coding:utf-8_*_
#file: lagrange.py

# 拉格朗日插值
def lagrange(X,Y,x):
    """X,Y为给定的已知条件，
        x为要进行插值的结点，
        返回插值y"""
    n=len(X)
    y=0
    for k in range(n):
        t=1
        for j in range(n):
            if j!=k:
                t=t*(x-X[j])/(X[k]-X[j])
        y=y+t*Y[k]
    return y