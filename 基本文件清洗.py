# encoding:utf-8
import os
#IO操作前
#可以用作数据清洗
path = '/home/dong/Downloads/trains/normal'
for file, i in zip(os.listdir(path), range(1, 2454)):
    newname = str(i) + '(2).jpg'
    try:
        os.rename(os.path.join(path,file),os.path.join(path,newname))
        # os.path.splitext():分离文件名与扩展名
        if os.path.splitext(file)[1] == '.jpg':
            print (file)
    except:
        print("IOError")
