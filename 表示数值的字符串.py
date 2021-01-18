import re

# 此题没有正确解答
def isNumber(s: str) -> bool:
    # re+	匹配1个或多个的表达式。
    # re?	匹配0个或1个由前面的正则表达式定义的片段，非贪婪方式
    # re*   匹配0个或多个的表达式。
    # return len(re.findall('([0-9]*\.[0-9]+)', s))
    # return len(re.findall('([0-9]*\.[0-9]+)|([0-9]*\.[0-9]+)', s))
    return (re.findall('^(([\+\-]?[0-9]+[Ee]?\-?[0-9]+)|([0-9]*\.?[0-9]?))', s))


# print(isNumber('e'))
# print(re.findall('^[\+\-]?[0-9]+[Ee]?\-?[0-9]+', "e"))
# print(re.findall('^(([0-9]+\.[0-9]+)|([0-9]+))$', ".1".strip()))
print(re.findall('^(([\+\-]?[0-9]+([Ee]\-?[0-9]+)?)|([0-9]+\.[0-9]+)|([0-9]+))$', ".1".strip()))
# print(re.findall('^(([\+\-]?[0-9]+([Ee]\-?[0-9]+)?)|([0-9]+\.[0-9]+)|([0-9]+))$', ".1".strip()))