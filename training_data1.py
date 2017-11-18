#coding:utf-8
import skimage.io as io
import numpy as np
import os

def vectorized_result(j):
    #将标签看做一个10*1的矩阵，如果哪一行为真，则那一行为1，否则为0
    e = np.zeros((10, 1))
    e[j] = 1.0
    return e
#读取训练图片数据
str= 'F:/TrainingSet/*.bmp'
coll = io.ImageCollection(str)
training_inputs=[]
for y in coll:
    training_inputs.append(np.array(y,dtype=float).reshape(784,1)/255.0)
#读取图片的文件名，提取标签
image_name=[]
image_label=[]
for filename in os.listdir(r"F:/TrainingSet/"):
    image_name.append(filename)
for i in image_name:
    i = i[0]
    image_label.append(int(i))
print len(image_label)
training_label = [vectorized_result(y) for y in image_label]
#将图片和标签结合为一个Tuple
training_data1 = zip(training_inputs, training_label)
