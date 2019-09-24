# **echo**

## 说明

**echo命令** 用于在shell中打印shell变量的值，或者直接输出指定的字符串。linux的echo命令，在shell编程中极为常用, 在终端下
打印变量value的时候也是常常用到的，因此有必要了解下echo的用法echo命令的功能是在显示器上显示一段文字，一般起到一个提示的
作用

## 选项

echo [SHORT-OPTION] ... [STRING]
echo LONG-OPTION
-n      不换行输出内容
-e      若字符串中出现以下转义字符，则特别加以处理，而不会将它当成一般文字输出：

转义字符：
* \a 发出警告声
* \b 删除前一个字符
* \c 最后不加上换行符号
* \f 换行但光标仍旧停留在原来的位置
* \n 换行且光标移至行首
* \r 光标移至行首，但不换行
* \t 插入tab
* \v 与\f相同
* \\ 插入\字符
* \nnn 插入nnn（八进制）所代表的ASCII字符
* \e escape
* \0NNN 八进制值NNN(1-3位)的字节
* \xHH 十六进制值HH(1-2位)的字节
* -E 取消-e效果，默认就是这个

## 实例

```bash
echo "I live in `locale territory`"     # 从locale数据库中展开信息
echo "$((0x2dec))"   # 十六进制转十进制
for i in {0..255}; do echo -e "\e[38;05;${i}m${i}"; done | column -c 80 -s ' '; echo -e "\e[m"  # 输出256中全部色彩

# 获取8位随机字符串
echo $RANDOM | md5sum | cut -c 1-8  # 方法一
openssl rand -base64 4  # 方法二
cat /proc/sys/kernel/random/uuid | cut -c 1-8   # 方法三

# 获取8位随机数字
echo $RANDOM | cksum | cut -c 1-8   # 方法一
openssl rand -base64 4 | cksum | cut -c 1-8 # 方法二

# 用echo命令打印带有色彩的文字：
## 文字色：# 颜色码：重置=0，黑色=30，红色=31，绿色=32，黄色=33，蓝色=34，洋红=35，青色=36，白色=37
echo -e "\e[1;31mThis is red text\e[0m"

* `\e[1;31m` 将颜色设置为红色
* `\e[0m` 将颜色重新置回

## 背景色：# 颜色码：重置=0，黑色=40，红色=41，绿色=42，黄色=43，蓝色=44，洋红=45，青色=46，白色=47
echo -e "\e[1;42mGreed Background\e[0m"

## 文字闪动：# 红色数字处还有其他数字参数：0 关闭所有属性、1 设置高亮度（加粗）、4 下划线、5 闪烁、7 反显、8 消隐
echo -e "\033[37;31;5mMySQL Server Stop...\033[39;49;0m"

# 关于转义字符使用如下：
echo -e "\v\v\v"    # 用-e选项，echo会打印出转义字符
echo -e "\042"      # 根据"引号字符的八进制ASCII码打印出字符
echo $'\042'    # 版本2开始bash允许使用$'\nnn'结构，这里'\nnn'表示一个八进制的值
echo $'\x22'    # 使用$'\xnnn'结构也可以使用十六进制来转义
 
# 当使用像$'\x'的结构时，-e的选项是多余的
echo "NEW LINE and BEEP"
echo $'\n'  # 新行
echo $'\a'  # 警告(峰鸣)

# 用ASCII码值把字符赋给变量
quote=$'\042'   # 引号"被赋值给变量quote
echo "$quote 这是一个引号字符串"

# 用连串的ASCII码把一串字符赋给变量
triple_underline=$'\137\137\137'  # 137是字符'_'的ASCII码
echo "$triple_underline UNDERLINE $triple_underline"

ABC=$'\101\102\103\010' # 101, 102, 103分别是A, B, C字符的八进制ASCII码.
echo $ABC

escape=$'\033'  # 033是ESC的ASCII码的八进制值
echo "\"escape\" echoes as $escape" # 不可见的输出

: << comment
一个字符串赋给变量时里面的组成部分可能会被转义，但如果单独一个转义字符（\）是不能赋给变量的
转义一个空格可以防止一个字符串参数被分割成多个命令行参数
转义符也提供了写一个多行命令的手段。一般地，每个单独的行有一个不同的命令，而在一行末尾的转义符转义新行符，命令序列则由下
一行继续
comment
```