import os
i = 0
while(i<10):
    path = 'D:/A毕业设计/data/mnist_test/'
    folder_names = os.listdir(path+str(i))
    print(folder_names)
    for name in folder_names:
        print(name)
        #必须还是目录
        # pic_names = os.listdir(path+str(i)+'/'+name)
        # for pic_name in pic_names:
        new_name = path+str(i)+'/'+str(i)+name
        old_name = path+str(i)+'/'+name
        os.rename(old_name,new_name)
    i = i+1
# p1 = './img_all/'
# folder_names = os.listdir(p1)
# for name in folder_names:
#     print(name)
#     #必须还是目录
#     # pic_names = os.listdir(path+str(i)+'/'+name)
#     # for pic_name in pic_names:
#     old_name = p1+name
#     new_name = p1+'0'+name
#     os.rename(old_name,new_name)