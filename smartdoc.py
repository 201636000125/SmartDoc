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
#全局变量，读取srs.txt的rq，ra，T，读取code.py的rq
#初始化
list_py_rq=[]
list_srs_rq=[]
list_srs_ra=[]
list_srs_t=[]
"""
Traceability Matrix

def


 
"""

"""
先读取SRS.txt
生成网页和链接
查找关键字 @Requirement [id=?] 生成链接
"""
def checkSeeRqSrs(text,htmlName):
    text_len=len(text)
    reText=''
    endflag=-1

    alph=''
    for i in range(0,text_len):
        if (text[i]!=' ' and text[i]!='\n'):
            alph+=text[i]
    alph_len=len(alph)
    #print(alph)
    alph_pos=-1
    for i in range(0,text_len):
        if (text[i]!=' ' and text[i]!='\n'):
            alph_pos+=1
        if (text[i]=='['):
            sub_alph=''
            for j in range(max(0,alph_pos-12),min(alph_len,alph_pos+4)):
                sub_alph+=alph[j]
            if (sub_alph=='@Requirement[id='):
                add_rq=''
                add_be=min(alph_len,alph_pos+4)
                for j in range(i,text_len):
                    if (text[j]==alph[add_be]):
                        if (text[j]==']'):
                            endflag=j
                            break
                        add_rq+=text[j]
                        add_be+=1
                if (add_be>min(alph_len,alph_pos+4)):
                    list_srs_rq.append(add_rq)
                    reText+='<a name=\"'+add_rq+'\" href=\"'+htmlName+'#'+add_rq+'\">'
            
            sub_alph=''
            for j in range(max(0,alph_pos-9),min(alph_len,alph_pos+4)):
                sub_alph+=alph[j]
            if (sub_alph=='Rationale[id='):
                add_ra=''
                add_be=min(alph_len,alph_pos+4)
                for j in range(i,text_len):
                    if (text[j]==alph[add_be]):
                        if (text[j]==']'):
                            endflag=j
                            break
                        add_ra+=text[j]
                        add_be+=1
                if (add_be>min(alph_len,alph_pos+4)):
                    list_srs_ra.append(add_ra)
                    
            sub_alph=''
            for j in range(max(0,alph_pos-8),min(alph_len,alph_pos+4)):
                sub_alph+=alph[j]
            if (sub_alph=='TestCase[id='):
                add_t=''
                add_be=min(alph_len,alph_pos+4)
                for j in range(i,text_len):
                    if (text[j]==alph[add_be]):
                        if (text[j]==']'):
                            endflag=j
                            break
                        add_t+=text[j]
                        add_be+=1
                if (add_be>min(alph_len,alph_pos+4)):
                    list_srs_t.append(add_t)

        if (text[i]=='\n'):
            reText+='<br/>'
        elif (text[i]==' '):
            reText+='&nbsp'
        else:
            reText+=text[i]
        if (i==endflag):
            reText+='</a>'
    return reText


"""
后读取code.py
生成网页和链接
查找关键字 {see ? } 生成链接
"""
def checkSeeRqCode(text,htmlName):
    text_len=len(text)
    reText=''
    endflag=-1

    alph=''
    for i in range(0,text_len):
        if (text[i]!=' ' and text[i]!='\n'):
            alph+=text[i]
    alph_len=len(alph)
    #print(alph)
    alph_pos=-1
    for i in range(0,text_len):
        if (text[i]!=' ' and text[i]!='\n'):
            alph_pos+=1
        if (text[i]=='{'):
            sub_alph=''
            for j in range(alph_pos,min(alph_len,alph_pos+4)):
                sub_alph+=alph[j]
            #print(sub_alph)
            #print('---\n')
            if (sub_alph=='{see'):
                add_rq=''
                add_be=min(alph_len,alph_pos+4)
                for j in range(i,text_len):
                    if (text[j]==alph[add_be]):
                        if (text[j]=='}'):
                            endflag=j
                            break
                        add_rq+=text[j]
                        add_be+=1     
                if (add_be>min(alph_len,alph_pos+4)):
                    for j in (list_srs_rq):
                        if (j==add_rq):
                            list_py_rq.append(add_rq)
                            reText+='<a name=\"'+add_rq+'\" href=\"'+htmlName+'#'+add_rq+'\">'
                            break


        if (text[i]=='\n'):
            reText+='<br/>'
        elif (text[i]==' '):
            reText+='&nbsp'
        else:
            reText+=text[i]
        if (i==endflag):
            reText+='</a>'
    return reText

#制作Traceability Matrix for requirements
def makeRTM():
    reText=''
    row=len(list_py_rq)
    
    #rq-rq
    column=len(list_srs_rq)
    print(column)
    reText+='<p><table border=\"1\" cellspacing=\"0\" >'
    for i in range(0,row+1):
        reText+='<tr>'
        for j in range(0,column+1):
            reText+='<td>'
            if (i==0 and j>0):
                reText+=('RQ'+str(j)+': '+list_srs_rq[j-1])
            elif (j==0 and i>0):
                reText+=('RQ'+str(i)+': '+list_py_rq[i-1])
            elif (i>0 and j>0 and list_py_rq[i-1]==list_srs_rq[j-1]):
                reText+=''
            reText+='</td>'
        reText+='</tr>'
    reText+='</table></p>'
    
    #rq-ra
    column=len(list_srs_ra)
    reText+='<p><table border=\"1\" cellspacing=\"0\" >'
    for i in range(0,row+1):
        reText+='<tr>'
        for j in range(0,column+1):
            reText+='<td>'
            if (i==0 and j>0):
                reText+=('RA'+str(j)+': '+list_srs_ra[j-1])
            elif (j==0 and i>0):
                reText+=('RQ'+str(i)+': '+list_py_rq[i-1])
            elif (i>0 and j>0 and list_py_rq[i-1]==list_srs_ra[j-1]):
                reText+=''
            reText+='</td>'
        reText+='</tr>'
    reText+='</table></p>'
    
    #rq-t
    column=len(list_srs_t)
    reText+='<p><table border=\"1\" cellspacing=\"0\" >'
    for i in range(0,row+1):
        reText+='<tr>'
        for j in range(0,column+1):
            reText+='<td>'
            if (i==0 and j>0):
                reText+=('T'+str(j)+': '+list_srs_t[j-1])
            elif (j==0 and i>0):
                reText+=('RQ'+str(i)+': '+list_py_rq[i-1])
            elif (i>0 and j>0 and list_py_rq[i-1]==list_srs_t[j-1]):
                reText+=''
            reText+='</td>'
        reText+='</tr>'
    reText+='</table></p>'
    
    
    return reText
    
    




#读取SRS.txt文件
file_srsTxt=open("SRS.txt", "r");
file_srsTxt_message=checkSeeRqSrs(file_srsTxt.read(),'code.html')
file_srsTxt.close()

#读取code.py文件
file_codePy=open("code.py", "r",encoding="utf-8")
file_codePy_message=checkSeeRqCode(file_codePy.read(),'SRS.html')
file_codePy.close()


#生成SRS.html文件
file_srsHtml=open("SRS.html","w")
file_srsHtml_message="""
<html>
<head>code</head>
<body>
%s
</body>
</html>
"""%(file_srsTxt_message+makeRTM())
file_srsHtml.write(file_srsHtml_message)
#print(file_srsHtml_message)
file_srsHtml.close()



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

