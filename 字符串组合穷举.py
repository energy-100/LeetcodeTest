res=[]
def do(str1,str2):
    if len(str2)==1:
        str1+=str2
        # print(tmpstr)
        res.append(str1)
        return

    for elem in str2:
        str1+=elem
        tmpstr2=str2.replace(elem,'')
        do(str1,tmpstr2)


if __name__ == '__main__':
    do('',"abcdef")
    print(len(res))
    print(res)

