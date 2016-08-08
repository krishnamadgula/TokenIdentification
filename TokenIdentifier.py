import numpy
import re
import string
keywords=["auto",	"double",	"int"	,"struct"
,"break",	"else",	"long"	,"switch",
"case",	"enum"	,"register"	,"typedef",
"char"	,"extern",	"return"	,"union"
,"const"	,"float"	,"short",	"unsigned",
"continue",	"for",	"signed",	"void",
"default",	"goto",	"sizeof",	"volatile",
"do",	"if",	"static"	,"while"]
if __name__ == '__main__':
    f=open("somefile.c",'r')
    l=f.readlines()
    a={}

    print l
    for i in range(len(l)):
        m=l[i]
        l[i]=[]
        #print m,len(l[i])
        for j in range(len(m)):
           # print m[j]
            if( m[j]!='\n' and m[j]!='  ' and m[j]!=';'):
                l[i].append(m[j])
        l[i]=string.join(l[i],'')
        m=l[i]
        tempTokens=re.split(' ',l[i])
        #for z in range (len(tempTokens)):
         #   print tempTokens[z]

        if (re.search("[#][a-z]*[<][a-z]*[.][h][>]",l[i]) != None):
            a.update({l[i]:'header'})
        #elif(re.search('[^0-9a-zA-Z]',l[i])!=None):
         #   a.update(({l[i]:'syntactical token'}))

        else :




            flag=numpy.zeros(len(tempTokens))
            for k in range(len(tempTokens)):

                for x in range(len(keywords)):

                    if(keywords[x]==tempTokens[k]):
                        flag[k]=1
                        a.update({tempTokens[k]:"keyword"})



            print flag.shape,flag
            for k in range(len(tempTokens)):
                if(flag[k]!=1):
                    if(re.search("^[^0-9a-zA-Z]",tempTokens[k])!=None):
                        a.update({tempTokens[k]:"operator"})
                    elif(re.search("[a-zA-Z][a-zA-Z0-9]*[(].*[)]",tempTokens[k])!=None):
                        a.update({tempTokens[k]:"functtion"})
                    elif(re.search("([0-9]+|\'.*\')",tempTokens[k])!=None):
                        a.update({tempTokens[k]:"constant"})
                    else:
                        a.update({tempTokens[k]:"identifier"})


    print l,'\n',a,'\n'
