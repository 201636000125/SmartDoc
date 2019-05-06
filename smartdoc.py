# -*- coding: utf-8 -*-

"""
Name :SmartDoc
@author: 201636000125

"""


"""
SRS格式参考样式为：

@Requirement [id=rq1] [description=???]
Rationale  [id=ra1???] [description=???]
TestCase   [id=tc???] [description=???]
Priority   [Low/Medium/High]
 
"""


"""
生成网页和链接
查找关键字 [id= ？ ] 生成链接
"""

def checkSeeRqSrs(text,htmlName):
    textLen=len(text)
    reText=''
    endflag=-1
    for i in range(0,textLen):
        tempText=''
        for j in range(i,min(i+4,textLen)):
            tempText+=text[j]
        #找到关键字前缀
        if (tempText=='[id='):
            subText=''
            for k in range(i+4,textLen):
                if (text[k]==']'):
                    endflag=k
                    break
                subText+=text[k]
            #生成链接
            reText+='<a name=\"'+subText+'\" href=\"'+htmlName+'#'+subText+'\">'
        tempText=''
        for j in range(i,min(i+6,textLen)):
            tempText+=text[j]
        #考虑关键字间的空格
        if (tempText=='[id = '):
            subText=''
            for k in range(i+6,textLen):
                if (text[k]==']'):
                    endflag=k
                    break
                subText+=text[k]
            reText+='<a name=\"'+subText+'\" href=\"'+htmlName+'#'+subText+'\">'
        #空格和换行的转换
        if (text[i]=='\n'):
            reText+='<br/>'
        elif (text[i]==' '):
            reText+='&nbsp'
        else:
            reText+=text[i]
        #链接结束
        if (i==endflag):
            reText+='</a>'
    return reText

"""
生成网页和链接
查找关键字 {see ? } 生成链接
"""
def checkSeeRqCode(text,htmlName):
    textLen=len(text)
    reText=''
    endflag=-1
    for i in range(0,textLen):
        tempText=''
        for j in range(i,min(i+5,textLen)):
            tempText+=text[j]
        #关键字前缀
        if (tempText=='{see '):
            subText=''
            for k in range(i+5,textLen):
                if (text[k]=='}'):
                    endflag=k
                    break
                subText+=text[k]
            reText+='<a name=\"'+subText+'\" href=\"'+htmlName+'#'+subText+'\">'
        if (text[i]=='\n'):
            reText+='<br/>'
        elif (text[i]==' '):
            reText+='&nbsp'
        else:
            reText+=text[i]
        if (i==endflag):
            reText+='</a>'
    return reText

#import webbrowser


#读取SRS.txt文件
file_srsTxt=open("SRS.txt", "r");
file_srsTxt_message=checkSeeRqSrs(file_srsTxt.read(),'code.html')
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
file_codePy_message=checkSeeRqCode(file_codePy.read(),'SRS.html')
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

