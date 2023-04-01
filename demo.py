import random
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import math as ma





#马尔可夫和随机对比



fig = plt.figure()
ax = plt.axes(projection='3d')            #创建三维坐标轴,下面画三维图像


#定义简单随机游走
def randwalk(n):
    x =50
    y =50
    z =10
    step_x = [x]
    step_y = [y]
    step_z = [z]


    for i in range(1,n+1):
        
            p = random.randint(30,150)
            q = random.randint(25,65)
            x = x + 20*np.sin(np.pi*p/180)*np.cos(np.pi*q/180)
            y = y + 20*np.sin(np.pi*p/180)*np.sin(np.pi*q/180)
            z = z + 20*np.cos(np.pi*p/180)

            step_x.append(x)
            step_y.append(y)
            step_z.append(z)
    return [step_x, step_y, step_z]




#定义markov游走
def markovrandwalk(n):
    x = 50
    y = 50
    z = 10
    a = 0.4                    #决策优化变量
    s = 8.0
    step_x = [x]
    step_y = [y]
    step_z = [z]
    p = 0
    q = 0
    pav = 55
    qav = 35
    sav = 8
    for i in range(1,n+1):
        #高斯随机变量
             sr=random.gauss(8,4)
             qr=random.gauss(0,50)
             pr=random.gauss(20,10)
             p = a*p+(1-a)*pav+(ma.sqrt(1-a**2))*pr
             q = a*q+(1-a)*qav+(ma.sqrt(1-a**2))*qr
             s = a*s+(1-a)*sav+(ma.sqrt(1-a**2))*sr
             x = x + s*np.sin(np.pi*p/180)*np.cos(np.pi*q/180)
             y = y + s*np.sin(np.pi*p/180)*np.sin(np.pi*q/180)
             z = z + s*np.cos(np.pi*p/180)

             step_x.append(x)
             step_y.append(y)
             step_z.append(z)
    return [step_x, step_y, step_z]

#'''Plotting the 3-D Random Walks'''


#改点数
markovrandwalk1 = markovrandwalk(50)
# markovrandwalk2 = markovrandwalk(100)
# markovrandwalk3 = markovrandwalk(100)
randwalk1 = randwalk(50)
# randwalk2 = randwalk(100)
# randwalk3 = randwalk(100)






# ax.plot(markovrandwalk3[0], markovrandwalk3[1], markovrandwalk3[2], 'c--', label = "randwalk3")
# ax.plot(randwalk3[0], randwalk3[1], randwalk3[2], 'b-', label = "randwalk3")
ax.plot(markovrandwalk1[0], markovrandwalk1[1], markovrandwalk1[2], color='royalblue',linestyle='--',label = "markov walk")
# ax.plot(markovrandwalk2[0], markovrandwalk2[1], markovrandwalk2[2], 'y-', linestyle='--',label = "randwalk2")
ax.plot(randwalk1[0], randwalk1[1], randwalk1[2], color='limegreen', label = "random walk")
# ax.plot(randwalk2[0], randwalk2[1], randwalk2[2], 'g-', label = "randwalk2")




#画图参数设置（暂时只学到这么多，可能图片还是没那么好看/(ㄒoㄒ)/~~）

#以下三行分别设置x轴、y轴与z轴标题与字号大小
ax.set_xlabel('X/m', size=12, labelpad=8)

ax.set_ylabel('Y/m', size=12, labelpad=8)

ax.set_zlabel('Z/m', size=12, labelpad=8)





#前3个参数用来调整各坐标轴的缩放比例
ax.get_proj = lambda: np.dot(Axes3D.get_proj(ax), np.diag([1, 1, 0.5, 1]))

#转换视角
#分别上下旋转和左右旋转，可以自己设置成一个比较好的参数
ax.view_init(30, -134)

#换底色
ax.xaxis.set_pane_color((1.0, 1.0, 1.0, 1.0))
ax.yaxis.set_pane_color((1.0, 1.0, 1.0, 1.0))
ax.zaxis.set_pane_color((1.0, 1.0, 1.0, 1.0))

# 设置坐标轴线宽
ax.xaxis.line.set_lw(0.6)
ax.yaxis.line.set_lw(0.6)
ax.zaxis.line.set_lw(0.6)

#框定坐标轴范围，
ax.set_xlim([0,1000])
ax.set_ylim([0,1000])
ax.set_zlim([0,100])



####调整刻度在这里改刻度值
ax.tick_params(labelsize=8,pad=1)
ax.set_xticks([0,200,400,600,800,1000])
ax.set_yticks([200,400,600,800,1000],)
ax.set_zticks([0,25,50,75,100])






#添加图例
plt.legend(loc='center',bbox_to_anchor=(0.8,0.35),fontsize=7)
plt.title('Comparison between random walk and markov walk of UAV')
plt.show() 