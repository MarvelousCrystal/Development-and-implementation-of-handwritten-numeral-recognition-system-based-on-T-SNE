import numpy as np
from sklearn.neighbors import KNeighborsClassifier
# #highTOlow()
#
# l1 = ['./test_pic/mnist_test_13.png',
# './test_pic/mnist_test_2.png','./test_pic/mnist_test_77.png','./test_pic/mnist_test_30.png',
# './test_pic/mnist_test_24.png','./test_pic/mnist_test_45.png','./test_pic/mnist_test_21.png',
# './test_pic/mnist_test_0.png','./test_pic/mnist_test_177.png','./test_pic/mnist_test_12.png']
p1 = './bu_data/all_final.txt'
p2 = './bu_data/label.txt'
p3 = './bu_testvalue/all_final.txt'

X_train = np.loadtxt(p1)
Y_train = np.loadtxt(p2)
x = np.loadtxt(p3)
# #拟合训练数据
knn_classifier = KNeighborsClassifier(n_neighbors=6)
knn_classifier.fit(X_train,Y_train)

# #将样本维度变为二维，因为我训练的维度就是二维的。
# #
# #print(x[0])
# #利用knn算法进行预测
l1 = []
i = 0
with open('./bu_data/predict.txt', 'w', encoding='utf-8') as f1:
    while(i<2140):
        x1 = x[i].reshape(1, -1)
        y_predict = knn_classifier.predict(x1)
        f1.write(str(y_predict[0])+'\n')
        l1.append(y_predict[0])
        print("knn预测结果为：" + str(y_predict[0]))
        i = i+1
    #得出预测结果 要展示的结果
    #开始要返回图片名称
    print(l1)
# j = 0
# with open('./bu_data/standard.txt', 'w',encoding='utf-8') as f:
#     while(j<10):
#         f.write((str(j)+'.0\n') * 214)
#         j = j + 1
count =  0
with open('./bu_data/predict.txt', 'r',encoding='utf-8') as f1, open('./bu_data/standard.txt', 'r',encoding='utf-8') as f2:
    lines1 = f1.readlines()
    lines2 = f2.readlines()#这个为将全部文本都读出来了，即所有行
    for i, (line1, line2) in enumerate(zip(lines1, lines2)):
        if line1.strip() == line2.strip():
            count = count + 1
print(count)