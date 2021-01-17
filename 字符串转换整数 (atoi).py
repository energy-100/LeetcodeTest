import re
def myAtoi(s: str) -> int:
    # + 匹配前一个元字符1到多次
    # [\+\-] 字符集 匹配内部的任意字符 \是转义符(因为 +,-是特殊字符 )
    # ? 匹配前一个字符 0或1次
    # \d 匹配数字
    # +匹配前一字符1到多次
    tmp=re.findall('[\+\-]?\d+',s)
    # tmp=re.findall('[\+\-]?\d+',s.lstrip())


    return min(max(int(re.findall('[\+\-]?\d+',s)[0]),-1<<31),1<<31+1)


print(myAtoi("words and 987"))
# myAtoi("   -42")