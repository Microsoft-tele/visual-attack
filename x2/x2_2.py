import math

from PIL import Image
import matplotlib.pyplot as plt
from scipy.stats import chi2, chi2_contingency
import numpy as np


def d_list(l, len):
    a = []
    b = []
    for i in range(0, len):
        if (i % 2 == 0):
            a.append(l[i])
        else:
            b.append(l[i])
            if (a[-1] == 0 and b[-1] == 0):
                a.pop()
                b.pop()
    return [a, b]

def min(a,b):
    if a>b:
        return b
    else:
        return a

img = Image.open('lsb.bmp')
# img = Image.open('src/加密图片.bmp')

h = img.height
w = img.width
size = 100  # 分隔后图像块的大小

spov_r = []
spov_g = []
spov_b = []
p_value_r = []
p_value_g = []
p_value_b = []

k = 0
img_rgb = img.convert('RGB')  # 转换图像格式为RGB

# 循环切割图片
for l in range(0, 5): # 取整 512 // 100 向上取整 = 5
    for k1 in range(0, 5):
        # 选中指定图像块
        l_r = [0 for e1 in range(0, 256)]
        l_g = [0 for e2 in range(0, 256)]
        l_b = [0 for e3 in range(0, 256)]

        # 区块内的直方图
        for x in range(0, 100):
            for y in range(0, 100):
                data = img_rgb.getpixel((l * 100 + x, k1 * 100 + y))
                # print("(" + str(x) + "," + str(y) + ")")
                print( "k = " + str(k) + " " + "l = " + str(l) + " " + "(" + str(l * 100 + x) + "," + str(k * 100 + y) + ")")
                r = data[0]
                g = data[1]
                b = data[2]
                l_r[r] += 1
                l_g[g] += 1
                l_b[b] += 1

        # 将l分为h_2i\h_2i+1两个列表
        # print(d_list(l_r, len(l_r)))

        # 三个通道分别做卡方分析
        r_r = chi2_contingency(d_list(l_r, len(l_r)))
        r_g = chi2_contingency(d_list(l_g, len(l_g)))
        r_b = chi2_contingency(d_list(l_b, len(l_b)))

        spov_r.append(r_r[0])
        p_value_r.append(r_r[1])
        spov_g.append(r_g[0])
        p_value_g.append(r_g[1])
        spov_b.append(r_b[0])
        p_value_b.append(r_b[1])
        k += 1

plt.rcParams['font.family']='MicroSoft YaHei'  #设置字体，默认字体显示不了中文
plt.figure(figsize=(10,8))

plt.subplot(231)
plt.title("R：X^2分布")
plt.plot(range(0,k), spov_r,label='R',color='red')
plt.subplot(234)
plt.title("R：p分布")
plt.plot(range(0,k), p_value_r,label='R',color='red')
plt.subplot(232)
plt.title("G：X^2分布")
plt.plot(range(0,k), spov_g,label='G',color='green')
plt.subplot(235)
plt.title("G：p分布")
plt.plot(range(0,k), p_value_g,label='G',color='green')
plt.subplot(233)
plt.title("B：X^2分布")
plt.plot(range(0,k), spov_b,label='B',color='blue')
plt.subplot(236)
plt.title("B：p分布")
plt.plot(range(0,k), p_value_b,label='B',color='blue')

plt.show()