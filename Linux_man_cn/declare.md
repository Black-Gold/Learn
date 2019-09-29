# **declare**

## 说明

**declare命令** 用于声明和显示已存在的shell变量。当不提供变量名参数时显示所有shell变量。declare命令若不带任何参数选项，则会显示所有
shell变量及其值。declare的功能与typeset命令的功能是相同的

## 选项

```markdown
+/-："-"可用来指定变量的属性，"+"则是取消变量所设的属性
-f：仅显示函数
r：将变量设置为只读
x：指定的变量会成为环境变量，可供shell以外的程序来使用
i：[设置值]可以是数值，字符串或运算式
shell变量：声明shell变量，格式为“变量名=值”
```

## 实例

```bash
declare test='man.linuxde.net'    # 定义并初始化test变量
```

