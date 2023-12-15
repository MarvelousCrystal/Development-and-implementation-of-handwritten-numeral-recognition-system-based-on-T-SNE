import numpy as np
from sklearn.cluster import KMeans
import sys
import os
from p_tsne import tsne
from low_dimense import highTOlow,to_2Dresult
from sklearn.metrics.pairwise import pairwise_distances
def low_predict():
# ----对这500张图片进行kmeans，这是降维以后的kmeans,目的是为了找出聚类中心图片，初步设定类别为10----
#首先测试的超参数 这个就是我们要变换的值
    # highTOlow()
    # to_2Dresult()
    path1 = "./2Dresult/all_final.txt"
    path2 = "./2Dresult/centers_10.txt"#这里存的是聚类中心的点的值
    path3 = "./2Dresult/center_label.txt"#这里存的是聚类中心的标签
    path4 = "./2Dresult/centers_10pic.txt"#这里需要存的是聚类中心图片的名称
    path5 = "./2Dresult/label.txt"
    pathe = './img_all/'

    part = np.loadtxt(path1)
    cluster = KMeans(n_clusters=10, init="k-means++",max_iter=200, tol=1e-04)
    cluster = cluster.fit(part)
    centers = cluster.cluster_centers_
    with open(path2 , 'w', encoding='utf-8') as f1:
        np.set_printoptions(threshold=sys.maxsize)
        f1.write(str(centers)+"\n")
    # 对照每个聚类中心属于哪个图片 即确定聚类中心所在位置，每个聚类中心找最近的所在图片
    #dist = cdist(data,sole,metric='euclidean')
    with open("./2Dresult/centers_10new.txt",'w',encoding='utf-8') as f1:
        with open("./2Dresult/centers_10.txt",'r',encoding='utf-8') as f2:
            for line in f2.readlines():
                l = line.replace('[[', '')
                l = l.replace(']]', '')
                l = l.replace('[', '')
                l = l.replace(']', '')
                f1.write(str(l))
    e = np.loadtxt("./2Dresult/centers_10new.txt")
    d = np.loadtxt(path1)
    # #print(e.shape)
    c = pairwise_distances(e,d)
    print(c.shape)
    # print(c[0])
    # x = c[0].argsort()
    # print(x)
    i = 0
    #这里存的是实际的聚类中心的值，该值可以找到对应的图片，但下一步还需做到将这些值一个一个比对，确定真实的图片名称

    l3 = []
    l4 = []
    with open("./2Dresult/centers_10_factual.txt",'w',encoding='utf-8') as f1:
        while(i<10):
            a = c[i]
            #排序出来为415最近，实际为416行的值
            y = a.argsort()
            #加1完成实际在500张图片中的位置
            a1 = int(y[0]/50)
            a2 = y[0]%50#余数
            sort_arr = []
            myFolders = os.listdir(pathe + str(a1))
            for folders in myFolders:
                # 将文件名的后缀去除
                folders = folders.replace(".png", "")
                folders = int(str(folders.replace("mnist_train_", "")))
                sort_arr.append(folders)
            sort_arr.sort()
            # print(sort_arr)
            #寻找folder为a2
            l1 = []
            l2 = []
            for folder in sort_arr:
                folder = str(folder)
                # 获得按文件命名数字大小重新排序后的文件路径
                path = pathe + str(a1) + "/mnist_train_" + folder + ".png"
                l1.append(path)
                l2.append(str(a1))
            f1.write(l1[a2]+"\n")
            l4.append(l1[a2])
            l3.append(l2[a2])#l3存入的为实际数字
            i = i + 1
    print(l3)

    with open(path3,'w',encoding='utf-8') as f1:
        for i in l3:
            f1.write(str(i)+'\n')
    return l3,l4#l3中为数字，l4中为数字对应的图片名称