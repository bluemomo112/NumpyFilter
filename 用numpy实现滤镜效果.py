# 滤镜套装
# -*- coding: utf-8 -*-
from PIL import Image
import numpy as np
import os

filePath="violet.png"
img = Image.open(filePath)
rgb = np.asarray(img, dtype='int')

r = rgb[:, :, 0]
g = rgb[:, :, 1]
b = rgb[:, :, 2]
a = rgb[:, :, 3]

# 1:绿色
F = np.array([[[1, 0, 0, 0, 50],
               [0, 2, 0, 0, 0],
               [0, 0, 1, 0, 0],
               [0, 0, 0, 1, 0]],
              # 2:紫色
              [[1, 0, 0, 0, 50],
               [0, 1, 0, 0, 0],
               [0, 0, 2, 0, 0],
               [0, 0, 0, 1, 0]],
              # 3:黄色
              [[2, 0, 0, 0, 0],
               [0, 1, 0, 0, 50],
               [0, 0, 1, 0, 0],
               [0, 0, 0, 1, 0]],
              # 4:红色
              [[2, 0, 0, 0, 0],
               [0, 1, 0, 0, 0],
               [0, 0, 1, 0, 0],
               [0, 0, 0, 1, 0]],
              # 5:橙色
              [[2, 0, 0, 0, 0],
               [0, 1, 0, 0, 0],
               [0, 0, 1, 0, 0],
               [0, 0, 0, 1, 0]]])


def filter(num):
	newr = F[num - 1][0][0] * r + F[num - 1][0][1] * g + F[num - 1][0][2] * b + F[num - 1][0][3] * a + F[num - 1][0][4]
	newg = F[num - 1][1][0] * r + F[num - 1][1][1] * g + F[num - 1][1][2] * b + F[num - 1][1][3] * a + F[num - 1][1][4]
	newb = F[num - 1][2][0] * r + F[num - 1][2][1] * g + F[num - 1][2][2] * b + F[num - 1][2][3] * a + F[num - 1][2][4]
	newa = F[num - 1][3][0] * r + F[num - 1][3][1] * g + F[num - 1][3][2] * b + F[num - 1][3][3] * a + F[num - 1][3][4]
	y, x = r.shape
	im = Image.new("RGBA", (x, y))
	for j in range(0, x):
		for i in range(0, y):
			# rgb转化为像素
			im.paste(((int(newr[i, j]), int(newg[i, j]), int(newb[i, j]), int(newa[i, j]))), (j, i, j + 1, i + 1))
	im.save("result.png")


filter(5)