# -*- coding: utf-8 -*-

"""
Name :SmartDoc
@author: 201636000125

"""

def checkSeeRqSrs(text,htmlName):
    textLen=len(text)
    reText=''
    endflag=-1
    for i in range(0,textLen):
        tempText=''
        for j in range(i,min(i+6,textLen)):
            tempText+=text[j]
        if (tempText=='[id=rq'):
            subText=''
            for k in range(i+6,textLen):
                if (text[k]==']'):
                    endflag=k
                    break
                subText+=text[k]
            reText+='<a name=\"'+subText+'\" href=\"'+htmlName+'#'+subText+'\">'
        tempText=''
        for j in range(i,min(i+8,textLen)):
            tempText+=text[j]
        if (tempText=='[id = rq'):
            subText=''
            for k in range(i+8,textLen):
                if (text[k]==']'):
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

def checkSeeRqCode(text,htmlName):
    textLen=len(text)
    reText=''
    endflag=-1
    for i in range(0,textLen):
        tempText=''
        for j in range(i,min(i+7,textLen)):
            tempText+=text[j]
        if (tempText=='{see rq'):
            subText=''
            for k in range(i+7,textLen):
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
'''
def see_rq():
    return 

def see_ral():
    return 

def see_tc():
    return 
'''

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

