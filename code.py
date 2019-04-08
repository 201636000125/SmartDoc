# -*- coding: utf-8 -*-
"""

Name :SmartDoc
@author: 201636000125

"""


#读取SRS.txt文件
f=open('SRS.txt', 'r')
#读取SRS.txt文件内容
message=f.read()
#print(message)
#关闭文件
f.close()


#生成html文件
out_html="index.html" 
#打开html文件
f=open(out_html,'w')
#写入内容
f.write(message) 
#关闭html文件
f.close()
 
