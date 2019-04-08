# -*- coding: utf-8 -*-

"""

Name :SmartDoc
@author: 201636000125

"""


#读取SRS.txt文件
file_srsTxt=open("SRS.txt", "r");
file_srsTxt_message=file_srsTxt.read()
file_srsTxt.close()

#生成SRS.html文件
file_srsHtml=open("SRS.html","w")
file_srsHtml.write(file_srsTxt_message)
print(file_srsTxt_message)
file_srsHtml.close()

#读取Scode.py文件
file_codePy=open("code.py", "r",encoding="utf-8")
file_codePy_message=file_codePy.read()
file_codePy.close()

#生成code.html文件
file_codeHtml=open("code.html","w")
file_codeHtml.write(file_codePy_message)
print(file_codePy_message)
file_srsHtml.close()

