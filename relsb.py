import sys
import random
import time

from PIL import Image, ImageDraw

image_name = "lsb_2.bmp"
save_name = "extract_lsb_2.bmp"

im = Image.open(image_name)  # 需要分析的图片
width, height = im.size
lsb_data_cnt = 0


out = Image.new('RGB', (width, height))  # 输出图像
draw = ImageDraw.Draw(out)  # 画图
cnt = 1
for y in range(height):
    for x in range(width):
        pix = im.getpixel((x, y))  # 依次获取原图像素点
        # print(pix[0], pix[1], pix[2])  # 调试信息
        pix_b = pix[2]
        pix_b_bin = bin(pix_b) # 二进制
        # print(pix_b_bin)
        pix_b_bin_last = pix_b_bin[-1:]

        co_list = list()
        print("进度:" + str(cnt) + ":" + str(pix_b_bin_last));
        cnt += 1
        if int(pix_b_bin_last) == 1: # 画一个白色
            co_list.append(255)
            co_list.append(255)
            co_list.append(255)
            co_tuple = tuple(co_list)
            draw.point((x, y), fill=co_tuple)  # 颜色元组，并且在（x,y）上画一个像素点
            out.save(save_name, 'bmp')
        else:   # 画一个黑色
            co_list.append(0)
            co_list.append(0)
            co_list.append(0)
            co_tuple = tuple(co_list)
            draw.point((x, y), fill=co_tuple)  # 颜色元组，并且在（x,y）上画一个像素点
            out.save(save_name, 'bmp')
