# **expr**

## 说明

**expr命令** 是一款表达式计算工具，使用它完成表达式的求值操作

## 选项

```markdown
将表达式的值列印到标准输出，分隔符下面的空行可提升算式优先级
可用的表达式有：

ARG1 | ARG2       若ARG1 的值不为0 或者为空，则返回ARG1，否则返回ARG2

ARG1 & ARG2       若两边的值都不为0 或为空，则返回ARG1，否则返回 0

ARG1 < ARG2       ARG1 小于ARG2
ARG1 <= ARG2      ARG1 小于或等于ARG2
ARG1 = ARG2       ARG1 等于ARG2
ARG1 != ARG2      ARG1 不等于ARG2
ARG1 >= ARG2      ARG1 大于或等于ARG2
ARG1 > ARG2       ARG1 大于ARG2

ARG1 + ARG2       计算 ARG1 与ARG2 相加之和
ARG1 - ARG2       计算 ARG1 与ARG2 相减之差

ARG1 * ARG2       计算 ARG1 与ARG2 相乘之积
ARG1 / ARG2       计算 ARG1 与ARG2 相除之商
ARG1 % ARG2       计算 ARG1 与ARG2 相除之余数

字符串 : 表达式               定位字符串中匹配表达式的模式

match 字符串 表达式           等于"字符串 :表达式"
substr 字符串 偏移量 长度     替换字符串的子串，偏移的数值从 1 起计
index 字符串 字符             在字符串中发现字符的地方建立下标，或者标0
length 字符串                 字符串的长度
+ TOKEN                    interpret TOKEN as a string, even if it is a
                             keyword like 'match' or an operator like '/'

( EXPRESSION )             value of EXPRESSION

请注意有许多运算操作符都可能需要由 shell 先实施转义
如果参与运算的 ARG 自变量都是数字，比较符就会被视作数学符号，否则就是多义的
模式匹配会返回"\"和"\"之间被匹配的子字符串或空(null)；如果未使用"\"和"\"
则会返回匹配字符数量或是 0

若表达式的值既不是空也不是 0，退出状态值为 0；若表达式的值为空或为 0
退出状态值为 1。如果表达式的句法无效，则会在出错时返回退出状态值 3

```

## 实例

```bash
expr dfa : '[a-zA-Z]*'  # expr也有正则匹配功能。通过指定冒号选项计算字符串中字符数，输出为3

result=`expr 2 + 3`
result=$(expr $no1 + 5)

```


