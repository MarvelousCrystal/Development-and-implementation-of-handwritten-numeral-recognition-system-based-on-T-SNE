import numpy as np
path = "D:/A毕业设计/tsne_python/tsne_python/data/"
#path2 = "D:/A毕业设计/tsne_python/tsne_python/data/00.txt"

#处理[[]]变为str
def minus_image2Digit_all(i,path):
    while(i<10):
        with open(path+ str(i) + str(i) + ".txt", 'w', encoding='utf-8') as f1:
            with open(path + str(i) + ".txt", 'r', encoding='utf-8') as f2:
                for line in f2.readlines():
                    #l = line.replace(' ','')
                    l = line.replace('\n', '')
                    l = l.replace(']]', '\n')
                    l = l.replace('[[','')
                    f1.write(str(l))
        i = i + 1

#X = np.loadtxt("D:/A毕业设计/tsne_python/tsne_python/data/11.txt")
#print(X.shape)