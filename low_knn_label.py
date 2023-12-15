from sklearn.neighbors import KNeighborsClassifier
import numpy as np
from kmeans_label import low_predict
#现在的x为近邻数，代替了原来的聚类中心数，即n_neighbors的值
def lowknn_predict(n_neighbors):
    l1 = ['./test_pic/mnist_test_13.png',
          './test_pic/mnist_test_2.png', './test_pic/mnist_test_77.png', './test_pic/mnist_test_30.png',
          './test_pic/mnist_test_24.png', './test_pic/mnist_test_45.png', './test_pic/mnist_test_21.png',
          './test_pic/mnist_test_0.png', './test_pic/mnist_test_177.png', './test_pic/mnist_test_12.png']
    p1 = './2Dresult/all_final.txt'
    p2 = './2Dresult/label.txt'
    p3 = './2Dresult/sole_final.txt'
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
    print("knn预测结果为：" + str(y_predict))
    #得出预测结果 要展示的结果
    s1, s2 = low_predict()
    j = 0
    for i in s1:
        if i == y_predict[0]:
            return s2[j];
        else:
            j = j + 1
    if j > 9:
        return l1[int(y_predict[0])]
if __name__== "__main__" :
    #----下列方法也需要调用3次
    lowknn_predict(1)