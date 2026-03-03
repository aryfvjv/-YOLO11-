本数据集包含焊缝图像192张，并使用伪彩色标注进行训练，下面对数据集各文件夹进行说明：

1、annotations_Hui：里面包含灰度标注图像192张

2、annotations_Wei:  里面包含伪彩色标注图像192张

3、Hui_txt:  使用该目录下的txt将使用灰度标注图像进行训练

4、Wei_txt:  使用该目录下的txt将使用伪彩色标注图像进行训练

5、images:  原图所在文件夹

6、label.txt:  数据集标签

7、coco.json:  使用EISeg交互式分割标注工具标注生成的json文件

8、*.py皆为组建数据集所使用的.py文件，使用步骤依次运行rename.py、list.py、create.py、最后view.py可为数据集可视化

English：
This data set contains 192 weld images. The folders of the data set are described below:

1、annotations_ Hui: it contains 192 grayscale images

2、annotations_ Wei: it contains 192 pseudo color annotation images

3、Hui_ Txt: using TXT in this directory will use grayscale annotation images for training

4、Wei_ Txt: using TXT in this directory will use pseudo color annotation images for training

5. Images: folder of original image

6. Label.txt: dataset label

7. Coco.json: annotate the generated JSON file using eiseg interactive segmentation annotation tool

8. *. Py is the. Py file used to build the dataset. Use the steps to run rename.py, list.py, create.py, and finally view.py to visualize the dataset