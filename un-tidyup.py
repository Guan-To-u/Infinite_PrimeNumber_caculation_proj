

import itertools
import math
import random
import os

"""
starter_cycle  = 0          # starter_cycle  是程序现在在   第几个周期  由人工指定 ，或读取 配置txt文件 
cycle_size     = 1_000_000  # 每一百万 （1M nums）  为一个周期
                #这个"_"写法仅仅 for py
cycle_position = 0          # 计数


有bug!!!  例如 990000000，后面会变成一堆零  也就是有漏掉的地方  但是会有最大数值限制来着

"""

Count_until_infinete = 2    # up to infinite
"""
while 1: #  RUN THIS CACULATION FOREVER!

    #读取文件 

    filee = open("examp.txt","a")
    

    # name  = 

    for i in range(3,int(Count_until_infinete/2),2):
        if Count_until_infinete % i == 0:
#            filee.writelines(str(Count_until_infinete))
            filee.write(str(Count_until_infinete) + os.linesep)


            #print("not")
            
    Count_until_infinete = Count_until_infinete + 1

filee.close()

"""




    #读取文件 

filee = open("examp.txt","a")
    

    # name  = 

for i in range(3,int(Count_until_infinete/2),2):
    if Count_until_infinete % i == 0:
#            filee.writelines(str(Count_until_infinete))
        filee.write(str(Count_until_infinete) + os.linesep)


            #print("not")
            
Count_until_infinete = Count_until_infinete + 1

filee.close()



# 写的很烂  别跑  目前还没有整理
