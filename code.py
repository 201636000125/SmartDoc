# -*- coding: utf-8 -*-

"""

Name :SmartDoc
@author: 201636000125

"""


#读取SRS.txt文件
with open("SRS.txt", "r")as f:
    message = f.read()

#生成SRS.html文件
with open("SRS.html", "w")as f:
    f.write(message)


#读取code.py文件
with open("code.py", "r")as f:
    message = f.read()


#生成code.html文件
with open("code.html", "w")as f:
    f.write(message)

