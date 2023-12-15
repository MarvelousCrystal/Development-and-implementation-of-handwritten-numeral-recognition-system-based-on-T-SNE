1.环境依赖
Python3.6.2
框架：Flask 2.0.3
2.进入界面需运行web1.py,当控制台出现http://127.0.0.1:5000/静态地址时，即可直接点击该地址进入该系统。
3.目录结构描述
（1）数据集：
├── 2Dresult 
│   └── all.txt 降维后的501张数据集的二维值
│   └── all.final.txt 对all.txt中预处理后的值
│   └── all_sole.txt 待预测图片的二维值
│   └── center_label.txt 结果标签表示的真正数字
│   └── centers_10.txt 结果标签的二维值
│   └── centers_10_factual.txt 结果标签对应的图片地址
│   └── centers_10new.txt 对centers_10.txt中预处理后的值
│   └── label.txt 500张图片对应的真正数字
│   └── mix.txt 降维前的501张数据集的784维值
│   └── sole_final.txt 对all_sole.txt中预处理后的值
├── bu_2Dresult 
    │   └── predict.txt 存放计算低维预测准确率时的预测结果
├── bu_data
│   └── x.txt（x为数字0-9）存放计算高维预测准确率时的784维度值
│   └── all.txt
│   └── all_final.txt
│   └── label.txt
│   └── mix.txt
│   └── mix_2D.txt
│   └── mix_train.txt
│   └── mix_trainfinal.txt
│   └── predict.txt 存放计算高维预测准确率时的预测结果
│   └── standard.txt 正确结果的值
├── bu_test 存放2140张测试集图片，用于计算准确率
├── bu_testvalue
├── bu_train 存放5000张训练集图片，用于计算准确率
├── data 
├── image_all 存放500张训练集，用于网页端数据
（2）框架：
├── static
│   └── css 存放css样式
│   └── img 存放网页端所需图片
│   └── js 存放js文件
│   └── plugins 存放插件
├── templates
│   └── dimensereduct.html 为降维前后运用knn进行分类预测并呈现结果的界面
│   └── homepage.html 为系统的进入界面
│   └── show.html 为展示二维后可视化图片的界面
├── web1.py 系统进入页面

（3）算法程序：
├── test_pic 存放10张矫正过后的预测标签
├── kmeans_label.py 运用k-means对降维后的数据找出最终预测结果的标签
├── high_knn_label.py 为高维时对单张图片的预测结果
├── low_knn_label.py 为低维时对单张图片的预测结果
├── low_dimense.py 为对测试集进行降维
├── bu_highprecise.py 为预测高维时knn算法的准确率
├── bu_lowprecise.py 为预测低维时knn算法的准确率
├── decode.py 对从官网上下载的mnist数据集进行解码
├── modify_filename.py 修改数据集名称，便于排序
├── p_tsne.py t-SNE算法
├── predeal.py 对解码后的图片进行数值转化
├── tsne_visualize.py 将降维后的数据进行可视化
