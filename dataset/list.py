import os
import random

trainval_percent = 0.95
train_percent = 0.9
labelfilepath = 'C:/Users/mf164/Desktop/hanfeng/annotations_Wei'
txtsavepath = 'C:/Users/mf164/Desktop/hanfeng/main'
total_xml = os.listdir(labelfilepath)

num = len(total_xml)
list = range(num)  # 192
tv = int(num * trainval_percent)  # 0.95 * 192 = 182.4
tr = int(num * train_percent)  # 0.9 * 192 = 172.8
trainval = random.sample(list, tv)
train = random.sample(list, tr)

ftrainval = open('C:/Users/mf164/Desktop/hanfeng/main/trainval.txt', 'w')
ftest = open('C:/Users/mf164/Desktop/hanfeng/main/test.txt', 'w')
ftrain = open('C:/Users/mf164/Desktop/hanfeng/main/train.txt', 'w')
fval = open('C:/Users/mf164/Desktop/hanfeng/main/val.txt', 'w')

for i in list:
    name = total_xml[i][:-4] + '\n'
    if i in trainval:
        ftrainval.write(name)
        if i in train:
            ftrain.write(name)
        else:
            fval.write(name)
    else:
        ftest.write(name)

ftrainval.close
ftrain.close
ftest.close
fval.close
