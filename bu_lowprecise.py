from low_dimense import highTOlow,to_2Dresult
import numpy as np
from p_tsne import tsne
import sys
from sklearn.neighbors import KNeighborsClassifier

p3 = "./bu_data/mix.txt"
p4 = "./bu_data/mix_2D.txt"
# with open(p3, 'w', encoding='utf-8') as f1:
#     with open(p2, 'r', encoding='utf-8') as f2:
#         for line in f2.readlines():
#             f1.write(str(line)+"\n")
# with open(p3, 'a', encoding='utf-8') as f1:
#     with open(p1, 'r', encoding='utf-8') as f2:
#         for line in f2.readlines():
#             f1.write(str(line))
# x = np.loadtxt(p3)
# #降维
# Y = tsne(x, 2, 50, 20.0)
# print(Y)
# #
# with open(p4,"w",encoding = 'utf-8') as f:
#     np.set_printoptions(threshold=sys.maxsize)
#     f.write(str(Y))



p1 = './bu_data/mix_train.txt'
p2 = './bu_data/label.txt'
p3 = './bu_testvalue/predict.txt'
p4 = './bu_data/mix_trainfinal.txt'
p5 = './bu_testvalue/predict_final.txt'
# with open(p5, 'w', encoding='utf-8') as f1:
#     with open(p3, 'r', encoding='utf-8') as f2:
#         for line in f2.readlines():
#             l = line.replace(']', '')
#             l = l.replace('[', '')
#             f1.write(str(l))
X_train = np.loadtxt(p4)
Y_train = np.loadtxt(p2)
x = np.loadtxt(p5)
#拟合训练数据
knn_classifier = KNeighborsClassifier(n_neighbors=6)
knn_classifier.fit(X_train,Y_train)

#将样本维度变为二维，因为我训练的维度就是二维的。
#
#print(x[0])
#利用knn算法进行预测
l1 = []
i = 0
with open('./bu_2Ddata/predict.txt', 'w', encoding='utf-8') as f1:
    while(i<2140):
        x1 = x[i].reshape(1, -1)
        y_predict = knn_classifier.predict(x1)
        l1.append(y_predict[0])
        f1.write(str(y_predict[0]) + '\n')
        print("knn预测结果为：" + str(y_predict[0]))
        i = i+1
    #得出预测结果 要展示的结果
    #开始要返回图片名称
print(l1)
count =  0
with open('./bu_2Ddata/predict.txt', 'r',encoding='utf-8') as f1, open('./bu_data/standard.txt', 'r',encoding='utf-8') as f2:
    lines1 = f1.readlines()
    lines2 = f2.readlines()#这个为将全部文本都读出来了，即所有行
    for i, (line1, line2) in enumerate(zip(lines1, lines2)):
        if line1.strip() == line2.strip():
            count = count + 1
print(count)