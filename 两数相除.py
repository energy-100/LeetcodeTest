
# 暴力版本
def divide(dividend: int, divisor: int) -> int:
    import sys
    sys.setrecursionlimit(1000000)
    sign = 1
    if (dividend > 0 and divisor < 0):
        sign = -1
        divisor = -divisor
    elif (dividend < 0 and divisor > 0):
        sign = -1
        dividend = -dividend
    elif (dividend < 0 and divisor < 0):
        dividend = -dividend
        divisor = -divisor

    def recursion_fun(dividend: int, divisor: int, times: int):
        if dividend < divisor:
            return times
        else:
            return recursion_fun(dividend - divisor, divisor, times + 1)

# 位运算版本
def divide_bit(dividend: int, divisor: int) -> int:
    if (dividend == 0):
        return 0
    sign = True
    # 移位运算判断两个数是否同号 按位异或（其实只是比较第一位，）<0异号
    if (dividend ^ divisor) < 0:
        sign = False
    dividendabs = abs(dividend)
    divisor = abs(divisor)
    if (dividendabs < divisor):
        return 0

    result = 0
    for i in range(31, -1, -1):
        if (dividendabs >> i >= divisor):
            result += 1 << i
            dividendabs -= divisor << i
    return min((1 << 31) - 1, result) if sign else -result

# 内存优化版本
def divide_bit_test(dividend:int,divisor:int) ->int:
    sign=False
    if (dividend==0):
        return 0

    #记住 符号位 0正数 1负数
    if (dividend^divisor)<0:
        sign=True

    divideend=abs(dividend)
    divisor=abs(divisor)
    times=0
    for i in range(31,-1,-1):
        if((divideend>>i)>=divisor):
            times+=1<<i
            divideend-=divisor<<i

    return -times if sign else min((1<<31)-1,times)




# print(divide(10,3))
print(-1^1)
# print(divide_bit(-2147483648,-1))
# print(divide_bit_test(-2147483648,-1))


