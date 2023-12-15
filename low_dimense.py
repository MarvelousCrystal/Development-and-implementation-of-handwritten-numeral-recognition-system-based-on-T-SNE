import numpy as np
from sklearn.cluster import KMeans
from sklearn.metrics.pairwise import pairwise_distances
import sys
from p_tsne import tsne
from split_50 import split_file
import os
import cv2
# #对要上传的图片进行处理
# def image2Digit(image):
#     #调整为28*28大小
#     im_resized = cv2.resize(image, (28, 28))
#     # CV2默认数据格式是float64的，np默认格式是float32的，这里要把数据格式转一下，否则后面会报错
#     im_resized2=im_resized.astype(np.float32)
#     # RGB（三维）转为灰度图（一维）
#     im_gray = cv2.cvtColor(im_resized2, cv2.COLOR_RGB2GRAY)
#     #二值化
#     im_gray2 = im_gray.astype(np.uint8)
#     #cv2.adaptive_threshold需要数据类型为uint8的输入数组
#     a = cv2.adaptiveThreshold(im_gray2,100,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)
#     reshaped = a.reshape(1, 784)
#     return reshaped
def highTOlow():
    p1 = "./data/all.txt"
    p2 = "./data/oldxxx.txt"
    p3 = "./2Dresult/mix.txt"
    p4 = "./2Dresult/all.txt"
    with open(p3, 'w', encoding='utf-8') as f1:
        with open(p2, 'r', encoding='utf-8') as f2:
            for line in f2.readlines():
                f1.write(str(line)+"\n")
    with open(p3, 'a', encoding='utf-8') as f1:
        with open(p1, 'r', encoding='utf-8') as f2:
            for line in f2.readlines():
                f1.write(str(line))
    x = np.loadtxt(p3)
    #降维
    Y = tsne(x, 2, 50, 20.0)
    print(Y)

    with open(p4,"w",encoding = 'utf-8') as f:
        np.set_printoptions(threshold=sys.maxsize)
        f.write(str(Y))
    return Y

def to_2Dresult():
    path1 = "./2Dresult/all.txt"
    path2 = "./2Dresult/all_final.txt"
    path3 = "./2Dresult/all_sole.txt"
    path4 = "./2Dresult/sole_final.txt"
    #向原来数据里面添加待预测数据然后一块降维 每次上传图片时需要再写入一个新文件中，要不然一直增加不对
    #tsne()
    with open(path2, 'w', encoding='utf-8') as f1:
        with open(path1, 'r', encoding='utf-8') as f2:
            for line in f2.readlines():
                l = line.replace(']', '')
                l = l.replace('[', '')
                f1.write(str(l))
    with open(path3, 'w', encoding='utf-8') as f1:
        with open(path1, 'r', encoding='utf-8') as f2:
            for line in f2.readlines():
                f1.write(str(line))
                break
    # txt文本单次删除第一行
    with open(path2, 'r', encoding='utf-8') as f:
        line = f.readlines()  # 读取文件
        try:
            line = line[1:]  # 只读取第一行之后的内容
            f = open(path2, 'w', encoding='utf-8')  # 以写入的形式打开txt文件
            f.writelines(line)  # 将修改后的文本内容写入
            f.close()  # 关闭文件
        except:
            pass
    with open(path4, 'w', encoding='utf-8') as f1:
        with open(path3, 'r', encoding='utf-8') as f2:
            for line in f2.readlines():
                l = line.replace(']', '')
                l = l.replace('[[', '')
                f1.write(str(l))
    # data = np.loadtxt(path2)
    # sole = np.loadtxt("./2Dresult/all_sole.txt")
    # print(sole.shape)
    # #将矩阵秩设置为1*2
    # sole = sole.reshape(1,-1)
    # print(sole.shape)
    # print(data.shape)

#----
def low_predict(n_clusters):
    # ----对每个txt进行kmeans，求取不同的聚类中心，初步对每个文件为10，20，30个聚类中心选取----
    #首先测试的超参数 这个就是我们要变换的值
    path1 = "./2Dresult/all_final_part"
    path2 = "./2Dresult/center_"
    path3 = "./2Dresult/finalcenter_"
    pathe = './img_all/'
    # with open("./2Dresult/all_final_backup.txt",'w',encoding='utf-8') as f1:
    #     with open("./2Dresult/all_final.txt",'r',encoding='utf-8') as f2:
    #         for line in f2.readlines():
    #             f1.write(str(line))
    split_file('./2Dresult/all_final.txt', 50)

    j = 0
    while(j<10):
        part = np.loadtxt(path1 + str(j) +".txt")
        cluster = KMeans(n_clusters=n_clusters, init="k-means++",max_iter=200, tol=1e-04)
        cluster = cluster.fit(part)
        centers = cluster.cluster_centers_
        with open(path2 + str(j) + ".txt", 'w', encoding='utf-8') as f1:
            np.set_printoptions(threshold=sys.maxsize)
            f1.write(str(centers)+"\n")
        j = j+1
    i = 0
    while(i<10):
        with open(path3 + str(i) +".txt",'w',encoding='utf-8') as f1:
            with open(path2 + str(i) + ".txt", 'r', encoding='utf-8') as f2:
                for line in f2.readlines():
                    l = line.replace('[[', '[')
                    l = l.replace(']]',']')
                    l = l.replace('\n','')
                    l = l.replace('[','\n')
                    l = l.replace('[','')
                    l = l.replace(']', '')
                    f1.write(str(l))
        i = i + 1
    k = 0

    with open("./2Dresult/centers_all.txt",'w',encoding='utf-8') as f1:
        while(k<10):
            x = np.loadtxt(path3+str(k)+".txt")
            f1.write(str(x)+"\n")
            k = k+1
    # 对照每个聚类中心属于哪个图片 即确定聚类中心所在位置，每个聚类中心找最近的所在图片
    #dist = cdist(data,sole,metric='euclidean')
    with open("./2Dresult/centers_allnew.txt",'w',encoding='utf-8') as f1:
        with open("./2Dresult/centers_all.txt",'r',encoding='utf-8') as f2:
            for line in f2.readlines():
                l = line.replace('[[', '[')
                l = l.replace(']]', ']')
                l = l.replace('\n', '')
                l = l.replace('[', '\n')
                l = l.replace('[', '')
                l = l.replace(']', '')
                f1.write(str(l))
    e = np.loadtxt("./2Dresult/centers_allnew.txt")
    d = np.loadtxt("./2Dresult/result.txt")
    d = d.reshape(1,-1)
    #print(e.shape)
    c = pairwise_distances(d,e)
    # print(c.shape)
    y = c.argsort()
    print(y )
    #写入第
    with open("./2Dresult/result.txt",'w',encoding='utf-8') as f1:
        with open("./2Dresult/centers_allnew.txt", 'r',encoding='utf-8') as file:
            line = file.readline()
            counts = 1
            while line:
                if counts >= y[0][0]+2:
                    break
                line = file.readline()
                counts += 1
            f1.write(line)
    #----找出高维值属于img_all中的哪张图片
    data = np.loadtxt("./2Dresult/all_final.txt")
    s = np.loadtxt("./2Dresult/result.txt")
    s = s.reshape(1,-1)
    f = pairwise_distances(s, data)
    n = f.argsort()
    print(n[0][0])#即为对应的照片在文件夹中的位置

    #----找出对应文件名
    #每50张各自排序
    z = 0

    l1 = []
    while(z<10):
        sort_arr = []
        myFolders = os.listdir(pathe+str(z))
        #print(len(myFolders))
        #print(myFolders)
        for folders in myFolders:
            # 将文件名的后缀去除
            folders = folders.replace(".png", "")
            folders = int(str(folders.replace("mnist_train_", "")))
            sort_arr.append(folders)
        # 对文件夹中的文件编号进行排序
        sort_arr.sort()
        #print(sort_arr)
        for folder in sort_arr:
            folder = str(folder)
            # 获得按文件命名数字大小重新排序后的文件路径
            path = pathe + str(z) + "/mnist_train_" +folder + ".png"
            l1.append(path)
        #print(l1)
        z = z+1
    #print(len(l1))
    print(l1[n[0][0]])
    return l1[n[0][0]]
if __name__== "__main__" :
    highTOlow()
    to_2Dresult()
    #----下面函数参数要一直变化，为10或20或30
    low_predict(30)