import numpy as np
from skimage.transform import resize
import imageio
import cv2
from fractions import Fraction
import os

#用于对灰度图进行二值化，其中像素设置为0或100
def image2Digit(image):
# 调整为28*28大小（对图片大小进行缩放）
    #im_resized = cv2.resize(image, (28, 28))
    # RGB（三维）转为灰度图（一维） mnist本来就为
    #im_gray = cv2.cvtColor(im_resized, cv2.COLOR_BGR2GRAY)
    #print(im_resized)
    #im_resized2 = im_resized.astype(np.float32)
    im_resized2 = image.astype(np.float32)
    #二值化
    a = cv2.adaptiveThreshold(image,100,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)

    #im_reverse = im_resized2.astype(np.int)
    #reshaped = im_reverse.reshape(1, 784)
    reshaped = a.reshape(1, 784)
    #print(reshaped)
    return reshaped

#path1 = 'D:/A毕业设计/tsne_python/tsne_python/mnist_train'
def image2Digit_all(path):
    #i = 0
    file = os.listdir(path)
    with open("D:/A毕业设计/tsne_python/tsne_python/bu_testvalue/all.txt", 'w', encoding='utf-8') as f1:
        for f in file:  #开始从0文件夹遍历每一个为0的图片
            image = imageio.imread(path + "/"  + f)
            im_reverse = image2Digit(image)
            f1.write(str(im_reverse) + "\n")

image2Digit_all("D:/A毕业设计/tsne_python/tsne_python/bu_test")

def minus_image2Digit_all(path):
     with open(path, 'w', encoding='utf-8') as f1:
        with open("D:/A毕业设计/tsne_python/tsne_python/bu_testvalue/all.txt", 'r', encoding='utf-8') as f2:
            for line in f2.readlines():
                #l = line.replace(' ','')
                l = line.replace('\n', '')
                l = l.replace(']]', '\n')
                l = l.replace('[[','')
                f1.write(str(l))

minus_image2Digit_all('D:/A毕业设计/tsne_python/tsne_python/bu_testvalue/all_final.txt')

