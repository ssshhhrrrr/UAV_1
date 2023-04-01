import random
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits import mplot3d 
import numpy as np



fig = plt.figure()
ax = plt.axes(projection='3d')            #创建三维坐标轴,下面画三维图像


x = np.random.randint(2000, size =(50))  
y = np.random.randint(2000, size =(50))  
z = np.random.randint(100, size =(50))






#画图参数设置（暂时只学到这么多，可能图片还是没那么好看/(ㄒoㄒ)/~~）

#以下三行分别设置x轴、y轴与z轴标题与字号大小
ax.set_xlabel('X/m', size=12, labelpad=8)

ax.set_ylabel('Y/m', size=12, labelpad=8)

ax.set_zlabel('Z/m', size=12, labelpad=8)





#前3个参数用来调整各坐标轴的缩放比例
ax.get_proj = lambda: np.dot(Axes3D.get_proj(ax), np.diag([1, 1, 0.5, 1]))
#转换视角
#分别上下旋转和左右旋转，可以自己设置成一个比较好的参数
ax.view_init(32, -32)

#换底色
ax.xaxis.set_pane_color((1.0, 1.0, 1.0, 1.0))
ax.yaxis.set_pane_color((1.0, 1.0, 1.0, 1.0))
ax.zaxis.set_pane_color((1.0, 1.0, 1.0, 1.0))

# 设置坐标轴线宽
ax.xaxis.line.set_lw(0.6)
ax.yaxis.line.set_lw(0.6)
ax.zaxis.line.set_lw(0.6)

#框定坐标轴范围
ax.set_xlim([0,2000])
ax.set_ylim([0,2000])
ax.set_zlim([0,100])

#调整刻度
ax.tick_params(labelsize=8,pad=1)
ax.set_xticks([0,200,400,600,800,1000,1200,1400,1600,1800,2000])
ax.set_yticks([200,400,600,800,1000,1200,1400,1600,1800],)
ax.set_zticks([0,20,40,60,80,100])


ax.scatter3D(x, y, z, color = "royalblue")

 #绘图区域的边框是否显示
#sub1.spines['top'].set_visible(False)
#sub1.spines['right'].set_visible(False)



#添加图例
plt.legend(loc='upper right',bbox_to_anchor=(1.2,1))
plt.title("3D scatter plot")
plt.show() 