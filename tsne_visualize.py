import matplotlib
import numpy as np
import matplotlib.pyplot as plt
path = "D:/A毕业设计/tsne_python/tsne_python/2Dresult/all.txt"
path1 = "D:/A毕业设计/tsne_python/tsne_python/2Dresult/finalall.txt"
path2 = "D:/A毕业设计/tsne_python/tsne_python/2Dresult/label.txt"
with open(path1,'w',encoding='utf-8') as f1:
    with open(path,'r',encoding='utf-8') as f2:
        for line in f2.readlines():
            l = line.replace("[",'')
            l = l.replace(']','')
            f1.write(l)
j = 0
with open(path2,'w',encoding='utf-8') as f1:
    while(j<10):
        i = 0
        while(i<1000):
            f1.write(str(j))
            f1.write("\n")
            i = i+1
        j = j + 1
color = ['blue', 'purple', 'green', 'gold', 'black',
         'pink', 'red', 'yellow', 'grey', 'brown']
# color = ['red', 'red', 'red', 'red', 'red',
#     'red', 'red', 'red', 'red', 'red',]
# 可视化展示
X = np.loadtxt(path1)
y = np.loadtxt(path2)
plt.figure(figsize=(100, 100))
plt.title('t-SNE process')
print(int(y[0]))


print(X[0,1])

# plt.xlim((-1.1, 1.1))
# plt.ylim((-1.1, 1.1))
# for i in range(len(result)):
#     plt.text(result[i,0], result[i,1], str(y[i]),
#              color=color[y[i]], fontdict={'weight': 'bold', 'size': 9})
# for i in range(len(y)):
#     plt.scatter(X[i,0], X[i,1], c=color[int(y[i])], s=1)

type0 = []
type1 = []
type2 = []
type3 = []
type4 = []
type5 = []
type6 = []
type7 = []
type8 = []
type9 = []
for i in range(len(y)):
    if y[i] == 0:
        type0.append(X[i])
    elif y[i] == 1:
        type1.append(X[i])
    elif y[i] == 2:
        type2.append(np.array(X[i]))
    elif y[i] == 3:
        type3.append(np.array(X[i]))
    elif y[i] == 4:
        type4.append(np.array(X[i]))
    elif y[i] == 5:
        type5.append(np.array(X[i]))
    elif y[i] == 6:
        type6.append(np.array(X[i]))
    elif y[i] == 7:
        type7.append(np.array(X[i]))
    elif y[i] == 8:
        type8.append(np.array(X[i]))
    else:
        type9.append(np.array(X[i]))

type0 = np.array(type0)
type1 = np.array(type1)
type2 = np.array(type2)
type3 = np.array(type3)
type4 = np.array(type4)
type5 = np.array(type5)
type6 = np.array(type6)
type7 = np.array(type7)
type8 = np.array(type8)
type9 = np.array(type9)
print(type9)

g0 = plt.scatter(type0[:, 0], type0[:, 1], c='blue')
g1 = plt.scatter(type1[:, 0], type1[:, 1], c='purple')
g2 = plt.scatter(type2[:, 0], type2[:, 1], c='green')
g3 = plt.scatter(type3[:, 0], type3[:, 1], c='gold')
g4 = plt.scatter(type4[:, 0], type4[:, 1], c='black')
g5 = plt.scatter(type5[:, 0], type5[:, 1], c='pink')
g6 = plt.scatter(type6[:, 0], type6[:, 1], c='red')
g7 = plt.scatter(type7[:, 0], type7[:, 1], c='yellow')
g8 = plt.scatter(type8[:, 0], type8[:, 1], c='grey')
g9 = plt.scatter(type9[:, 0], type9[:, 1], c='brown')
plt.legend(handles=[g0, g1, g2,g3,g4,g5,g6,g7,g8,g9], labels=['0', '1', '2','3','4','5','6','7','8','9'])



# plt.savefig('static/img/plot.png')
plt.show()