# 此文件用来记录经典或有趣的数学问题
# It's really fun to swim in the ocean of mathematics

# 百钱白鸡问题：1只公鸡5元，1只母鸡3元，3只小鸡1元，100元买100只鸡，问：公鸡母鸡小鸡各有多少？
# 经典三元一次方程求解，设各有x，y，z只

# 解法一：推断每种鸡花费依次轮询，运行时间最短，2019-7-24最优方案
# import time
# start = time.perf_counter_ns()    # 用自带time函数统计运行时长
for x in range(0, 101, 5):  # 公鸡花费x元在0-100范围包括100，步长为5
    for y in range(0, 101 - x, 3):  # 母鸡花费y元在0到100元减去公鸡花费钱数，步长为3
        z = 100 - x - y  # 小鸡花费z元为100元减去x和y
        if x / 5 + y / 3 + z * 3 == 100:
            print("公鸡：%d只，母鸡：%d只，小鸡：%d只" % (x / 5, y / 3, z * 3))
            # pass
# end = time.perf_counter_ns()
# time1 = end - start
# print("解法一花费时间：", time1)

# 解法二：枚举法
# 解题思路：若只买公鸡最多20只，但要买100只，固公鸡在0-20之间不包括20;若只买母鸡则在0-33之间不包括33;若只买小鸡则在0-100
# 之间不包括100
for x in range(0, 20):
    for y in range(0, 33):
        z = 100 - x - y  # 小鸡个数z等于100只减去公鸡x只加母鸡y只
        if 5 * x + 3 * y + z / 3 == 100:  # 钱数相加等于100元
            print("公鸡：%d只，母鸡：%d只，小鸡：%d只" % (x, y, z))

# 解法三：解法和解法一类似
# 解题思路：买一只公鸡花费5元，剩余95元(注意考虑到不买公鸡的情况)，再买一只母鸡花费3元剩余92元，依次轮询下去，钱数不断减
# 少，100元不再是固定的。假设花费钱数依次为x、y、z元
for x in range(0, 101, 5):  # 公鸡花费x元在0-100范围包括100，步长为5
    for y in range(0, 101 - x, 3):  # 母鸡花费y元在0到100元减去公鸡花费钱数，步长为3
        for z in range(0, 101 - x - y):
            if x / 5 + y / 3 + z * 3 == 100 and x + y + z == 100:  # 花费和鸡数都是100
                print("公鸡：%d只，母鸡：%d只，小鸡：%d只" % (x / 5, y / 3, z * 3))

# 经典斐波那契数列
# 定义:https://wikimedia.org/api/rest_v1/media/math/render/svg/c374ba08c140de90c6cbb4c9b9fcd26e3f99ef56
# 用文字来说，就是斐波那契数列由0和1开始，之后的斐波那契系数就是由之前的两数相加而得出
# 方法一：使用递归
def fib1(n):
    if n<0:
        print("Incorrect input")
    elif n==1:
        return 0    # 第一个斐波那契数是0
    elif n==2:
        return 1    # 第二斐波那契数是1
    else:
        return fib1(n-1)+fib1(n-2)

print(fib1(2))

# 方法二：使用动态编程
FibArray = [0, 1]


def fib2(n):
    if n < 0:
        print("Incorrect input")
    elif n <= len(FibArray):
        return FibArray[n - 1]
    else:
        temp_fib = fib2(n - 1) + fib2(n - 2)
        FibArray.append(temp_fib)
        return temp_fib

# 方法三：空间优化

def fibonacci(n):
    a = 0
    b = 1
    if n < 0:
        print("Incorrect input")
    elif n == 0:
        return a
    elif n == 1:
        return b
    else:
        for i in range(2,n):
            c = a + b
            a = b
            b = c
        return b


# 水仙花数：水仙花数即此数字是各位立方和等于这个数本身的数。例：153 = 1**3 + 5**3 + 3**3
# 找出1-1000之间的水仙花数

# 分别四个数字：1,2,3,4，组成不重复的三位数。问题扩展：对于给定数字或给定范围的数字，组成不重复的n位数

# 方法一：解答四个数组成不重复三位数(暂未想到更优方法)
for x in range(1, 5):
    for y in range(1, 5):
        for z in range(1, 5):
            if (x != y) and (x != z) and (z != y):
                print(x, y, z)


# 计算pi小数点任意位数
from __future__ import division
import math
from time import time
time1 = time()
number = int(input('输入计算的位数：'))
number1 = number + 10  # 多计算十位方式尾数取舍影响
b = 10 ** number1

# 求含4/5的首项
x1 = b * 4 // 5
# 求含1/239的首项
x2 = b // -239

# 求第一大项
he = x1 + x2
# 设置下面循环的终点，即共计算n项
number *= 2

# 循环初值=3，末值2n,步长=2
for i in range(3, number, 2):
    # 求每个含1/5的项及符号
    x1 //= -25
    # 求每个含1/239的项及符号
    x2 //= -57121
    # 求两项之和
    x = (x1 + x2) // i
    # 求总和
    he += x

# 求出π
pi = he * 4
# 舍掉后十位
pi //= 10 ** 10

# 输出圆周率π的值
pi_string = str(pi)
result = pi_string[0] + str('.') + pi_string[1:len(pi_string)]
print(result)

time2 = time()

print(u'耗时：' + str(time2 - time1) + 's')


# 使用chudnovsky算法计算
# 理解链接：https://www.craig-wood.com/nick/articles/pi-chudnovsky/

"""
Python3 program to calculate Pi using python long integers, BINARY
splitting and the Chudnovsky algorithm

"""

import math
from gmpy2 import mpz
from time import time

def pi_chudnovsky_bs(digits):
    """
    Compute int(pi * 10**digits)

    This is done using Chudnovsky's series with BINARY splitting
    """
    C = 640320
    C3_OVER_24 = C**3 // 24
    def bs(a, b):
        """
        Computes the terms for binary splitting the Chudnovsky infinite series

        a(a) = +/- (13591409 + 545140134*a)
        p(a) = (6*a-5)*(2*a-1)*(6*a-1)
        b(a) = 1
        q(a) = a*a*a*C3_OVER_24

        returns P(a,b), Q(a,b) and T(a,b)
        """
        if b - a == 1:
            # Directly compute P(a,a+1), Q(a,a+1) and T(a,a+1)
            if a == 0:
                Pab = Qab = mpz(1)
            else:
                Pab = mpz((6*a-5)*(2*a-1)*(6*a-1))
                Qab = mpz(a*a*a*C3_OVER_24)
            Tab = Pab * (13591409 + 545140134*a) # a(a) * p(a)
            if a & 1:
                Tab = -Tab
        else:
            # Recursively compute P(a,b), Q(a,b) and T(a,b)
            # m is the midpoint of a and b
            m = (a + b) // 2
            # Recursively calculate P(a,m), Q(a,m) and T(a,m)
            Pam, Qam, Tam = bs(a, m)
            # Recursively calculate P(m,b), Q(m,b) and T(m,b)
            Pmb, Qmb, Tmb = bs(m, b)
            # Now combine
            Pab = Pam * Pmb
            Qab = Qam * Qmb
            Tab = Qmb * Tam + Pam * Tmb
        return Pab, Qab, Tab
    # how many terms to compute
    DIGITS_PER_TERM = math.log10(C3_OVER_24/6/2/6)
    N = int(digits/DIGITS_PER_TERM + 1)
    # Calclate P(0,N) and Q(0,N)
    P, Q, T = bs(0, N)
    one_squared = mpz(10)**(2*digits)
    sqrtC = (10005*one_squared).sqrt()
    return (Q*426880*sqrtC) // T

# The last 5 digits or pi for various numbers of digits
check_digits = {
    100 : 70679,
    1000 :  1989,
    10000 : 75678,
    100000 : 24646,
    1000000 : 58151,
    10000000 : 55897,
}

if __name__ == "__main__":
    digits = 100
    pi = pi_chudnovsky_bs(digits)
    print(pi)
    #raise SystemExit
    for log10_digits in range(1,9):
        digits = 10**log10_digits
        start =time()
        pi = pi_chudnovsky_bs(digits)
        print("chudnovsky_gmpy_mpz_bs: digits",digits,"time",time()-start)
        if digits in check_digits:
            last_five_digits = pi % 100000
            if check_digits[digits] == last_five_digits:
                print("Last 5 digits %05d OK" % last_five_digits)
            else:
                print("Last 5 digits %05d wrong should be %05d" % (last_five_digits, check_digits[digits]))