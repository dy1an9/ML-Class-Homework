#coding:utf-8
import skimage.io as io
import numpy as np
#读取测试图片数据
str= 'F:/TestSet/*.bmp'
coll = io.ImageCollection(str)
io.imshow(coll[0])
test_inputs=[]
for y in coll:
    test_inputs.append(np.array(y,dtype=float).reshape(784,1)/255.0)
# 读取图片的文件名，提取标签
image_name=[]
test_label=[]
import os
for filename in os.listdir(r"F:/TestSet/"):
    image_name.append(filename)
for i in image_name:
    i = i[0]
    test_label.append(int(i))
print len(test_label)
#将图片和标签结合为一个Tuple
test_data1 = zip(test_inputs, test_label)
