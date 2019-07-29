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

