from  scipy.stats import chi2_contingency
import numpy as np
from PIL import Image, ImageDraw
import math

from PIL import Image
import matplotlib.pyplot as plt
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

image_name = "lsb_3.bmp"
im = Image.open(image_name)  # 需要分析的图片

p_value_b = []

for k in range(5):
    for l in range(5):

        l_r = [0 for e1 in range(0, 255)]
        l_g = [0 for e2 in range(0, 255)]
        l_b = [0 for e3 in range(0, 255)]

        for y in range(100):
            for x in range(100):
                pix = im.getpixel((k * 100 + x, l * 100 + y))  # 依次获取原图像素点    
                r = pix[0]
                g = pix[1]
                b = pix[2]
                l_r[r] += 1
                l_g[g] += 1
                l_b[b] += 1           

        # print(x2_array)
        r_b = chi2_contingency(d_list(l_b, len(l_b))) # stat卡方统计值，p：P_value，dof 自由度，expected理论频率分布
        # print('%.4f'%p)
        # print('%.4f'%stat)
        p_value_b.append(r_b[1])


# plt.rcParams['font.family']='MicroSoft YaHei'  #设置字体，默认字体显示不了中文
# plt.figure(figsize=(10,8))

# plt.subplot(236)
# plt.title("B：p分布")
# plt.plot(range(0,k), p_value_b,label='B',color='blue')

# plt.show()

