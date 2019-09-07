# **bc**

## 说明

**bc命令** 是一种支持任意精度的交互执行的计算器语言。bash内置了对整数四则运算的支持，但是并不支持浮点运算，而bc命令可以
很方便的进行浮点运算，当然整数运算也不再话下

## 选项

```markdown
-i  --interactive  强制进入交互式模式；输入quit后回车退出此模式
-l  --mathlib      定义使用的标准数学库
-q  --quiet        不打印初始化信息
-s  --standard     non-standard bc constructs are errors
-w  --warn         warn about non-standard bc constructs

```

## 实例

```bash
echo "1.212*3" | bc     # 算术操作高级运算bc命令它可以执行浮点运算和一些高级函数
echo "scale=2;3/8" | bc # 设定小数精度（数值范围)参数`scale=2`是将bc输出结果的小数位设置为2位
echo "obase=2;192" | bc    # 进制转换,将数字192转换为2进制，注意：只能对数字进行进制转换,对应的进制有2,8,16,64
echo "$((0x2dec))"   # 十六进制转十进制
echo "sqrt(1000/10) + 1" | bc -l

# 计算平方和平方根
echo "10^10" | bc
echo "sqrt(100)" | bc

```
