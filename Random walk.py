import matplotlib.pyplot as plt
from random import choice
'''随机漫步'''
#创建randomwalk class
class RandomWalk():
    def __init__(self,num_point=5000):
        self.num_point=num_point
        #起点
        self.x=[0]
        self.y=[0]

    def walking(self):
        while len(self.x)<self.num_point:
            #choice()函数选择方向
            x_direction=choice([1,-1])#choice位于random
            x_distance=choice([0,1,2,3,4])
            x_step=x_distance*x_direction

            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_distance * y_direction

            #拒绝原地踏步
            if x_step==0 and y_step==0:
                continue
            else:
                next_x=self.x[-1]+x_step
                next_y=self.y[-1]+y_step

            self.x.append(next_x)
            self.y.append(next_y)
            #生成数据完成


rw=RandomWalk(num_point=10000)
rw.walking()
#渐变
point_number=list(range(rw.num_point))
#调整窗口尺寸
plt.figure(figsize=(8,5))
plt.scatter(rw.x,rw.y,s=1,c=point_number,cmap=plt.cm.Blues)
# 突出起点和终点,放在绘制好的图之后，不然会覆盖掉
plt.scatter(0, 0, s=50, c='red')
plt.scatter(rw.x[-1], rw.y[-1], s=50, c='red')
#隐藏坐标轴
'''
plt.xticks([])  # 去掉x轴
plt.yticks([])  # 去掉y轴
plt.axis('off')  # 去掉坐标轴
'''
#plt.axes().get_xaxis().set_visible(False)
#plt.axes().get_yaxis().set_visible(False)
#这不行，要放在图片生成之前，不然会没有数据
#这说明这个方法是直接创建一个空白区域覆盖坐标轴(maybe)
plt.axis('off')

plt.show()

