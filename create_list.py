'''
在Main文件夹中划分好的数据集进行位置索引，生成含有图像及对应的label文件的地址信息的文件。
'''
import os
import random
import re

devkit_dir = './'
output_dir = './'


def get_dir(devkit_dir, type):
    return os.path.join(devkit_dir, type)


def walk_dir(devkit_dir):
    filelist_dir = get_dir(devkit_dir, 'main')
    annotation_dir = get_dir(devkit_dir, 'annotations_Wei')
    img_dir = get_dir(devkit_dir, 'images')
    trainval_list = []
    train_list = []
    val_list = []
    test_list = []

    added = set()  # 创建无序集合

    for _, _, files in os.walk(filelist_dir):
        for fname in files:
            img_ann_list = []
            if re.match('trainval.txt', fname):
                img_ann_list = trainval_list
            elif re.match('train.txt', fname):
                img_ann_list = train_list
            elif re.match('val.txt', fname):
                img_ann_list = val_list
            elif re.match('test.txt', fname):
                img_ann_list = test_list
            else:
                continue
            fpath = os.path.join(filelist_dir, fname)
            for line in open(fpath):
                name_prefix = line.strip().split()[0]
                # print(name_prefix)

                added.add(name_prefix)
                ann_path = annotation_dir + '/' + name_prefix + '.png'
                # print(ann_path)
                img_path = img_dir + '/' + name_prefix + '.png'
                assert os.path.isfile(
                    ann_path), 'file %s not found.' % ann_path
                assert os.path.isfile(
                    img_path), 'file %s not found.' % img_path
                img_ann_list.append((img_path, ann_path))

            print(img_ann_list[:4])
    return trainval_list, train_list, test_list, val_list


def prepare_filelist(devkit_dir, output_dir):
    trainval_list = []
    train_list = []
    test_list = []
    val_list = []

    trainval, train, test, val = walk_dir(devkit_dir)

    trainval_list.extend(trainval)
    train_list.extend(train)
    test_list.extend(test)
    val_list.extend(val)

    with open(os.path.join(output_dir, 'trainval.txt'), 'w') as ftrainval:
        for item in trainval_list:
            ftrainval.write(item[0] + ' ' + item[1] + '\n')
    with open(os.path.join(output_dir, 'train.txt'), 'w') as ftrain:
        for item in train_list:
            ftrain.write(item[0] + ' ' + item[1] + '\n')
    with open(os.path.join(output_dir, 'test.txt'), 'w') as ftest:
        for item in test_list:
            ftest.write(item[0] + ' ' + item[1] + '\n')
    with open(os.path.join(output_dir, 'val.txt'), 'w') as fval:
        for item in val_list:
            fval.write(item[0] + ' ' + item[1] + '\n')


if __name__ == '__main__':
    prepare_filelist(devkit_dir, output_dir)
