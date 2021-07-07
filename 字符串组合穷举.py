import copy
res=[]
def do(str1,str2):
    if len(str2)==1:
        tmpstr=str1+str2
        # print(tmpstr)
        res.append(tmpstr)
    else:
        for elem in str2:
            tmpstr1=str1+elem
            tmpstr2=str2.replace(elem,'')
            do(tmpstr1,tmpstr2)


if __name__ == '__main__':
    do('',"abcdef")
    print(len(res))
