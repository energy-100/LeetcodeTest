

def divide(dividend: int, divisor: int) -> int:
    def recursion_fun(dividend: int, divisor: int, times: int):
        if dividend < divisor:
            return times
        else:
            return recursion_fun(dividend - divisor, divisor, times + 1)

    return recursion_fun(dividend, divisor, 0)


def divide_bit(dividend: int, divisor: int) -> int:
    # 移位运算判断两个数是否同号 按位异或（其实只是比较第一位，）<0异号
    if (dividend^divisor) <0:
        




print(divide(10,3))