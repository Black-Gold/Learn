# **read命令说明**

**read命令** 从键盘读取变量的值，通常用在shell脚本中与用户进行交互的场合。该命令可以一次读取多个变量的值，变量和输入的值都需要使用空格隔开。在read命令后面，如果没有指定变量名，读取的数据将被自动赋值给特定的变量REPLY

```sh
read: read [-ers] [-a 数组] [-d 分隔符] [-i 缓冲区文字] [-n 读取字符数] [-N 读取字符数] [-p 提示符] [-t 超时] [-u 文件描述符] [名称 ...]

从标准输入读取一行并将其分为不同的域。

从标准输入读取单独的一行，或者如果使用了 -u 选项，从文件描述符 FD 中读取。

该行被分割成域，如同词语分割一样，并且第一个词被赋值给第一个 NAME 变量，第二

个词被赋值给第二个 NAME 变量，如此继续，直到剩下所有的词被赋值给最后一个 NAME

变量。只有 $IFS 变量中的字符被认作是词语分隔符。

如果没有提供 NAME 变量，则读取的行被存放在 REPLY 变量中。
```

  

```sh
选项：
-a array 将词语赋值给 ARRAY 数组变量的序列下标成员，从零开始。
-d delim 持续读取直到读入 DELIM 变量中的第一个字符，而不是换行符
-e 在一个交互式 shell 中使用 Readline 获取行
-i text 使用 TEXT 文本作为 Readline 的初始文字
-n nchars 读取 nchars 个字符之后返回，而不是等到读取换行符。但是分隔符仍然有效，如果遇到分隔符之前读取了不足 nchars 个字符。
-N nchars 在准确读取了 nchars 个字符之后返回，除非遇到文件结束符或者读超时，任何的分隔符都被忽略
-p prompt 在尝试读取之前输出 PROMPT 提示符并且不带换行符
-r 不允许反斜杠转义任何字符
-s 不显示终端的任何输入
-t timeout 如果在 TIMEOUT 秒内没有读取一个完整的行则超时并且返回失败。TMOUT 变量的值是默认的超时时间。TIMEOUT 可以是小数。如果 TIMEOUT 是 0，那么仅当在指定的文件描述符上输入有效的时候，read 才返回成功。如果超过了超时时间，则返回状态码大于 128
-u fd 从文件描述符 FD 中读取，而不是标准输入

退出状态：

返回码为零，除非遇到了文件结束符，读超时，或者无效的文

件描述符作为参数传递给了 -u 选项。
```

## read命令示例  

```sh
# 从标准输入读取输入并赋值给变量1987name。
# 等待读取输入，直到回车后表示输入完毕，并将输入赋值给变量answer
read 1987name

# 控制台输入Hello
HelloWorld

# 打印变量
echo $1987name
HelloWorld
```

等待一组输入，每个单词之间使用空格隔开，直到回车结束，并分别将单词依次赋值给这三个读入变量。

```
#read one two three
1 2 3                   #在控制台输入1 2 3，它们之间用空格隔开。

#echo "one = $one, two = $two, three = $three"
one = 1, two = 2, three = 3
```

REPLY示例

```
#read                  #等待控制台输入，并将结果赋值给特定内置变量REPLY。
This is REPLY          #在控制台输入该行。 

#echo $REPLY           #打印输出特定内置变量REPLY，以确认是否被正确赋值。

This is REPLY
```

-p选项示例

```
#read -p "Enter your name: "            #输出文本提示，同时等待输入，并将结果赋值给REPLY。
Enter you name: stephen                 #在提示文本之后输入stephen

#echo $REPLY
stephen
```

等待控制台输入，并将输入信息视为数组，赋值给数组变量friends，输入信息用空格隔开数组的每个元素。

```
#read -a friends
Tim Tom Helen

#echo "They are ${friends[0]}, ${friends[1]} and ${friends[2]}."
They are Tim, Tom and Helen.
```

 **补充一个终端输入密码时候，不让密码显示出来的例子。** 

方法1：

```
#!/bin/bash
read -p "输入密码：" -s pwd
echo
echo password read, is "$pwd"
```

方法2：

```
#!/bin/bash
stty -echo
read -p "输入密码：" pwd
stty echo
echo
echo 输入完毕。
```

其中，选项`-echo`禁止将输出发送到终端，而选项`echo`则允许发送输出。

使用read命令从键盘读取变量值，并且将值赋给指定的变量，输入如下命令：

```
read v1 v3          #读取变量值
```

执行上面的指令以后，要求键入两个数据，如下所示：

```
Linux c+            #输入数据
```

完成之后，可以使用echo命令将指定的变量值输出查看，输入如下命令：

```
echo $v1 $v3       #输出变量的值
```

执行输出变量值的命令以后，将显示用户所输入的数据值，如下所示：

```
Linux c+           #输出变量值
```

注意：使用echo命令输出变量值时，必须在变量名前添加符号`$`。否则，echo将直接输出变量名。


