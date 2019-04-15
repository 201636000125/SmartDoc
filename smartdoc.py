# -*- coding: utf-8 -*-

"""
Name :SmartDoc
@author: 201636000125

"""


"""
def see_rq():
    return 

def see_ral():
    return 

def see_tc():
    return 
"""

#import webbrowser


#读取SRS.txt文件
file_srsTxt=open("SRS.txt", "r");
file_srsTxt_message=''
for line in file_srsTxt.readlines():
    file_srsTxt_message=file_srsTxt_message+"</br>"+line
file_srsTxt.close()


#生成SRS.html文件
file_srsHtml=open("SRS.html","w")
file_srsHtml_message="""
<html>
<head>code</head>
<body>
%s
</body>
</html>
"""%(file_srsTxt_message)
file_srsHtml.write(file_srsHtml_message)
#print(file_srsHtml_message)
file_srsHtml.close()


#读取Scode.py文件
file_codePy=open("code.py", "r",encoding="utf-8")
file_codePy_message=''
for line in file_codePy.readlines():
    file_codePy_message=file_codePy_message+"</br>"+line
file_codePy.close()


#生成code.html文件
file_codeHtml=open("code.html","w")
file_codeHtml_message="""
<html>
<head>code</head>
<body>
%s
</body>
</html>
"""%(file_codePy_message)
file_codeHtml.write(file_codeHtml_message)
#print(file_codeHtml_message)
file_codeHtml.close()

