from sklearn.neighbors import KNeighborsClassifier
import numpy as np
import numpy as np
import imageio
import cv2
import sys
from sklearn.metrics.pairwise import pairwise_distances
import os
from low_dimense import highTOlow
from kmeans_label import low_predict
def image2Digit(image):
    #二值化
    a = cv2.adaptiveThreshold(image,100,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)
    reshaped = a.reshape(1, 784)
    return reshaped
def dealdata(pre):
## 每次运行要改变的值
    img = imageio.imread(pre)
    print(img.shape)
    X = image2Digit(img)
    with open('./data/xxx.txt', 'w') as f:
        f.write(str(X))
    with open('./data/oldxxx.txt', 'w', encoding='utf-8') as f3:
        with open('./data/xxx.txt', 'r', encoding='utf-8') as f2:
            for line in f2.readlines():
                l = line.replace('\n', '')
                l = l.replace(']', '')
                l = l.replace('[', '')
                f3.write(str(l))
    data = np.loadtxt("./data/all.txt")
    sole = np.loadtxt("./data/oldxxx.txt")#含有待预测图片的值，为1*784
    sole = sole.reshape(1,-1)
    return sole
#现在的x为近邻数，代替了原来的聚类中心数，即n_neighbors的值
def highknn_predict(n_neighbors):
    #highTOlow()
    l1 = ['./test_pic/mnist_test_13.png',
    './test_pic/mnist_test_2.png','./test_pic/mnist_test_77.png','./test_pic/mnist_test_30.png',
    './test_pic/mnist_test_24.png','./test_pic/mnist_test_45.png','./test_pic/mnist_test_21.png',
    './test_pic/mnist_test_0.png','./test_pic/mnist_test_177.png','./test_pic/mnist_test_12.png']
    p1 = './data/all.txt'
    p2 = './2Dresult/label.txt'
    p3 = './data/oldxxx.txt'
    p4 = './2Dresult/centers_10_factual.txt'
    X_train = np.loadtxt(p1)
    Y_train = np.loadtxt(p2)
    x = np.loadtxt(p3)
    #拟合训练数据
    knn_classifier = KNeighborsClassifier(n_neighbors)
    knn_classifier.fit(X_train,Y_train)

    #将样本维度变为二维，因为我训练的维度就是二维的。
    x1 = x.reshape(1, -1)

    #利用knn算法进行预测
    y_predict = knn_classifier.predict(x1)
    print("knn预测结果为：" + str(y_predict[0]))
    #得出预测结果 要展示的结果
    #开始要返回图片名称
    s1,s2 = low_predict()
    j= 0
    for i in s1:
        if i== y_predict[0]:
            return s2[j];
        else:
            j = j+1
    if j>9:
        return l1[int(y_predict[0])]

if __name__== "__main__" :
    #----下列方法也需要调用3次
    highknn_predict(1)