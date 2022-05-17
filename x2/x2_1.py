from  scipy.stats import chi2_contingency
import numpy as np
import pandas as pd
from PIL import Image, ImageDraw

image_name = "lsb_3.bmp"
im = Image.open(image_name)  # 需要分析的图片

for k in range(16):
    for l in range(16):
        x2_array = np.zeros(1024).reshape(32, 32)
        for y in range(32):
            for x in range(32):
                pix = im.getpixel((k * 32 + x, l * 32 + y))  # 依次获取原图像素点                  
                x2_array[x][y] = pix[2]
        # print(x2_array)
        stat,p,dof,expected = chi2_contingency(x2_array) # stat卡方统计值，p：P_value，dof 自由度，expected理论频率分布
        # print('%.4f'%p)
        print('%.4f'%stat)


