import matplotlib.pyplot as plt
import math

_coor=[(0,0),(0,1),(1,1),(1,0)]
'''
环境中固定粒子的坐标,二维
'''
_myp=[0.33,0.33]
'''
运动粒子的坐标,二维
'''
'''
粒子间相互作用力为斥力,简单的平方反比
'''

def u_x(_coor:list,_myp:list)->float:
    ux=0
    for i in _coor:
        r0=math.sqrt((_myp[0]-i[0])**2+(_myp[1]-i[1])**2)
        ux+=1/r0
    return ux

def show_u(_coor:list,_myp:list)->None:
    plt.ion()
    u=[]
    path=[]
    i=0
    while _myp[1] <= 1 and _myp[0] <= 1:
        path.append(i)
        u.append(u_x(_coor,_myp))
        _myp[1]+=0.005
        i+=0.005
        plt.plot(path,u,color='r')
        plt.pause(0.01)
    plt.pause(999)

show_u(_coor,[0.5,0])

