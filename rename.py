import os
path = "C:/Users/mf164/Desktop/hanfeng/annotations_Wei/"
f = os.listdir(path)
# print(len(f))
# print(f[0])

n = 0
i = 0

for i in f:
    oldname = f[n]
    newname = i[:-11] + '.png'
    os.rename(path+oldname, path+newname)
    print(oldname, '======>', newname)
    n += 1
