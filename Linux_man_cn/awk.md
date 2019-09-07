# **awk**

## 说明

awk的基本功能是在文件中搜索包含一个或多个模式的行或其他文本单元。当一行与其中一个模式匹配时，将对该行执行特殊操作
awk中的程序与大多数其他语言中的程序不同，因为awk程序是“数据驱动的”：您描述要使用的数据，然后在找到时执行的操作。大多数
其他语言都是“程序性的”。您必须详细描述该计划要采取的每个步骤。使用过程语言时，通常很难清楚地描述程序将处理的数据。出于
这个原因，awk程序通常易于读写

## 选项

```markdown
Usage: awk [POSIX or GNU style options] -f progfile [--] file ...
Usage: awk [POSIX or GNU style options] [--] 'program' file ...

 -f progfile     --file=progfile       # 从脚本文件中读取awk命令
 -F fs           --field-separator=fs  # fs指定输入分隔符，fs可以是字符串或正则表达式
 -v var=val      --assign=var=val      # 赋值一个用户定义变量，将外部变量传递给awk

 -b          --characters-as-bytes
 -c          --traditional
 -C          --copyright
 -d[file]    --dump-variables[=file]
 -e 'program-text'   --source='program-text'
 -E file     --exec=file
 -g          --gen-pot
 -L [fatal]  --lint[=fatal]
 -n          --non-decimal-data
 -N          --use-lc-numeric
 -O          --optimize
 -p[file]    --profile[=file]
 -P          --posix
 -r          --re-interval
 -S          --sandbox
 -t          --lint-old

gawk is a pattern scanning and processing language.By default it reads standard input and writes standard output
```

## pattern

pattern可以是以下任意一个：

* /正则表达式/：使用通配符的扩展集。
* 关系表达式：使用运算符进行操作，可以是字符串或数字的比较测试。
* 模式匹配表达式：用运算符`~`（匹配）和`~!`（不匹配）。
* BEGIN语句块、pattern语句块、END语句块：参见awk的工作原理

## 操作

操作由一个或多个命令、函数、表达式组成，之间由换行符或分号隔开，并位于大括号内，主要部分是：

* 变量或数组赋值
* 输出命令
* 内置函数
* 控制流语句

## awk脚本基本结构

```bash
awk 'BEGIN{ commands } pattern{ commands } END{ commands }'
```

* 第一步：执行`BEGIN{ commands }`语句块中的语句；
* 第二步：从文件或标准输入(stdin)读取一行，然后执行`pattern{ commands }`语句块，它逐行扫描文件，从第一行到最后一行重复<br>这个过程，直到文件全部被读取完毕。
* 第三步：当读至输入流末尾时，执行`END{ commands }`语句块。

**BEGIN语句块** 在awk开始从输入流中读取行** 之前** 被执行，这是一个可选的语句块，比如变量初始化、打印输出表格的表头等
语句通常可以写在BEGIN语句块中

**END语句块** 在awk从输入流中读取完所有的行** 之后** 即被执行，比如打印所有行的分析结果这类信息汇总都是在END语句块中
完成，它也是一个可选语句块

**pattern语句块** 中的通用命令是最重要的部分，它也是可选的。如果没有提供pattern语句块，则默认执行`{ print }`，即打印
每一个读取到的行，awk读取的每一行都会执行该语句块

一个awk脚本通常由：BEGIN语句块、能够使用模式匹配的通用语句块、END语句块3部分组成，这三个部分是可选的。任意一个部分都
可以不出现在脚本中，脚本通常是被**单引号**或**双引号**中，例如：

```bash
awk 'BEGIN{ i=0 } { i++ } END{ print i }' filename
awk "BEGIN{ i=0 } { i++ } END{ print i }" filename
```

## 实例

```bash
echo -e "A line 1nA line 2" | awk 'BEGIN{ print "Start" } { print } END{ print "End" }'
# 输出如下
: << comment
Start
A line 1nA line 2
End

{ }类似一个循环体，会对文件中的每一行进行迭代，通常变量初始化语句（如：i=0）以及打印文件头部的语句放入BEGIN语句块中，
将打印的结果等语句放在END语句块中。
comment

# 当使用不带参数的`print`时，它就打印当前行，当`print`的参数是以逗号进行分隔时，打印时则以空格作为定界符。
# 在awk的print语句块中双引号是被当作拼接符使用，例如：
echo | awk '{ var1="v1"; var2="v2"; var3="v3"; print var1,var2,var3; }' # 输出：v1 v2 v3
echo | awk '{ var1="v1"; var2="v2"; var3="v3"; print var1"="var2"="var3; }' # 双引号使用例子，输出：v1=v2=v3
```

### awk内置变量（预定义变量）

说明：[A][N][P][G]表示第一个支持变量的工具，[A]=awk、[N]=nawk、[P]=POSIXawk、[G]=gawk

可自定义变量，变量可以是字符串或数值。输入字段的内容也可以分配给变量。为了更精确地控制输出格式而不是打印通常提供的
输出格式，请使用printf。 printf命令可用于指定每个项目使用的字段宽度，以及数字的各种格式选择（例如要使用的输出基数，
是否打印指数，是否打印标记以及数字位数在小数点后打印）。这是通过提供一个名为格式字符串的字符串来完成的，该字符串控
制打印其他参数的方式和位置

```markdown
$n  当前记录的第n个字段，比如n为1表示第一个字段，n为2表示第二个字段
$0  这个变量包含执行过程中当前行的文本内容
[N] ARGC                            命令行参数的数目
[G] ARGIND                          命令行中当前文件的位置（从0开始算）
[N] ARGV                            包含命令行参数的数组
[G] CONVFMT                         数字转换格式（默认值为%.6g）
[P] ENVIRON                         环境变量关联数组
[N] ERRNO                           最后一个系统错误的描述
[G] FIELDWIDTHS                     字段宽度列表（用空格键分隔）
[A] FILENAME                        当前输入文件的名
[P] FNR                             同NR，但相对于当前文件
[A] FS(fields separator)            字段分隔符（此变量预定义为一个或多个空格或制表符）
[G] IGNORECASE                      如果为真，则进行忽略大小写的匹配
[A] NF                              表示字段数，在执行过程中对应于当前的字段数
[A] NR(number of records)           表示记录数，在执行过程中对应于当前的行号
[A] OFMT                            数字的输出格式（默认值是%.6g）
[A] OFS(output fields separator)    输出字段分隔符（默认值是一个空格）
[A] ORS(output record separator)    输出记录分隔符（默认值是一个换行符）
[A] RS                              记录分隔符（默认是一个换行符）
[N] RSTART                          由match函数所匹配的字符串的第一个位置
[N] RLENGTH                         由match函数所匹配的字符串的长度
[N] SUBSEP                          数组下标分隔符（默认值是34）
```

###  FS示例

```bash
# awk FS变量用于设置每个记录的字段分割符，其可以设置为任何单个字符或者正则表达式
# 默认的字段定界符是空格，可以使用`-F "定界符"`明确指定一个定界符
# 在`BEGIN语句块`中则可以用`OFS=“定界符”`设置输出字段的定界符
# FS可以更改任意次数，会保留其值直到明确更改，如果想更改字段分割符，在阅读行之前更改，因此改变会影响阅读的内容

# 大致格式：awk -F 'FS' '命令' 文件名    或   awk 'BEGIN {FS="FS";}'
# 用于读取具有:作为字段分割符的/etc/passwd文件
awk 'BEGIN{ FS = ":"; print "\tUserID\tGroupID\tHomeDirectory"; } { print $1"\t"$3"\t"$4"\t"$6; } \
END{ print NR,"打印记录总数" }' /etc/passwd

# awk OFS是awk FS变量的输出，默认情况，awk OFS是单个空格字符
# 打印语句中的:,默认情况下两个参数连接为一个空间，该空间是awk OFS的值，固其值被插入到输出中的字段之间
awk -F ':' '{print $3,$4;}' /etc/passwd # 打印passwd文件第三第四个字段，-F设置定界符
awk -F ':' 'BEGIN{OFS ="=";}{print $3,$4;}' /etc/passwd
```

### RS示例：记录分割符变量

```bash
# awk RS定义了一条线，awk默认逐行读取。将信息存储在一个文件中，每个记录由两个新行隔开，每个字段用一个新行分割
awk 'BEGIN{ RS="\n\n"; FS="\n"; } { print $1,$2 }' student.txt  # 打印姓名和第二行数字,student.txt文件内容如下
: << comment
Jones
2143
78
84
77

Bob
2321
56
58
45
comment

# 使用`print $NF`可以打印出一行中的最后一个字段，使用`$(NF-1)`则打印倒数第二个字段，其他以此类推(超出数目则会全部输出)：
echo -e "line1 f2 f3n line2 f4 f5" | awk '{print $NF}'  # 输出f5
echo -e "line1 f2 f3n line2 f4 f5" | awk '{print $(NF-1)}'  # 输出f4

awk 'END{ print NR }' filename  # 统计文件中的行数,awk读取每一行会将NR更新为对应行号，读到最后一行则是文件行数

# file文件每一行中第一个字段值累加的例子
seq 5 | awk 'BEGIN{ sum=0; print "总和：" } { print $1"+"; sum+=$1 } END{ print "等于"; print sum }' file

for i in $(pip list -o | awk 'NR > 2 {print $1}'); do sudo pip install -U $i; done  # 批量升级所有过时的pip包
```

### 将外部变量值传递给awk

```bash
VAR=10000; echo | awk -v VARIABLE=$VAR '{ print VARIABLE }' # 借助-v选项，可以将外部值（并非来自stdin）传递给awk
var1="aaa"; var2="bbb"; echo | awk '{ print v1,v2 }' v1=$var1 v2=$var2  # 另一种传递外部变量方法
awk '{ print v1,v2 }' v1=$var1 v2=$var2 filename    # 当输入来自于文件时使用
netstat -antup | grep 7770 | awk '{ print $NF NR}' | awk '{ print $1}'  # 查找进程pid
```

### awk运算与判断

作为一种程序设计语言所应具有的特点之一，awk支持多种运算，这些运算与C语言提供的基本相同。awk还提供了一系列内置的运算
函数（如log、sqr、cos、sin等）和一些用于对字符串进行操作（运算）的函数（如length、substr等等）。这些函数的引用大大
的提高了awk的运算功能。作为对条件转移指令的一部分，关系判断是每种程序设计语言都具备的功能，awk也不例外，awk中允许进
行多种测试，作为样式匹配，还提供了模式匹配表达式~（匹配）和~!（不匹配）。作为对测试的一种扩充，awk也支持用逻辑运算符

#### 算术运算符

| 运算符 | 描述 |
| :-----: | :----: |
| + - | 加，减 |
| * / & | 乘，除与求余 |
| + - ! | 一元加，减和逻辑非 |
| ^** * | 求幂 |
| ++ -- | 增加或减少，作为前缀或后缀 |

```bash
awk 'BEGIN{a="b";print a++,++a;}'   #  输出：0 2
# 注意：所有字符用作算术运算符进行操作，操作数自动转为数值，所有非数值都变为0
```

#### 赋值运算符

| 运算符 | 描述 |
| :-----: | :----: |
| = += -= *= /= %= ^=** = | 赋值语句 |

#### 逻辑运算符

```bash
: << comment
运算符       描述
  ||        逻辑或
  &&        逻辑与
comment

awk 'BEGIN{a=1;b=2;print (a>5 && b<=2),(a>5 || b<=2);}' # 输出：0 1
```

#### 正则运算符

| 运算符 | 描述 |
| ----- | ---- |
| ~ | 匹配正则表达式 |
| ~! | 不匹配正则表达式 |

```bash
awk 'BEGIN{a="100testa";if(a ~ /^100*/){print "ok";}}'  # 输出：ok
```

#### 关系运算符

| 运算符 | 描述 |
| ----- | ---- |
| < <= > >= != == | 关系运算符 |

```bash
awk 'BEGIN{a=11;if(a >= 9){print "ok";}}'   # 输出：ok
# 注意：> < 可以作为字符串比较，也可用作数值比较，关键看操作数
# 如果是字符串就会转换为字符串比较。两个都为数字才转为数值比较。字符串比较：按照ASCII码顺序比较
```

#### 其它运算符

| 运算符 | 描述 |
| ----- | ---- |
| $ | 字段引用 |
| 空格 | 字符串连接符 |
| ?: | C条件表达式 |
| in | 数组中是否存在某键值 |

```bash
awk 'BEGIN{a="b";print a=="b"?"ok":"err";}' # 输出：ok
awk 'BEGIN{a="b";arr[0]="b";arr[1]="c";print (a in arr);}'  # 输出：0
awk 'BEGIN{a="b";arr[0]="b";arr["b"]="c";print (a in arr);}'    # 输出：1
```

#### 运算级优先级表

* !级别越高越优先
* 级别越高越优先


## awk高级输入输出

```bash
# awk中next语句：在循环中逐行匹配遇到next，就会跳过当前行，直接忽略下面语句。而进行下一行匹配。next语句一般用于多行合并
# 打印student.txt偶数行，并打印出对应的行号。解析：当记录行号除以2余1，就跳过当前行。print NR,$0也不会执行。
awk 'NR%2==1{next}{print NR,$0;}' student.txt

# 匹配并跳过file文件以web行开头的行，然后将匹配到的行作为下面每行的开始并与下面每行合并为一行
awk '/^web/{T=$0;next;}{print T"\t"$0;}' file

# 简单地读取一条记录
: << comment
awk getline用法：输出重定向需用到getline函数。getline从标准输入、管道或者当前正在处理的文件之外的其他输入文件获得输入。
它负责从输入获得下一行的内容，并给NF,NR和FNR等内建变量赋值。如果得到一条记录，getline函数返回1，如果到达文件的末尾就
返回0，如果出现错误，例如打开文件失败，就返回-1

getline语法：getline var，变量var包含了特定行的内容。

awk getline从整体上来说，用法说明：
当其左右无重定向符 | 或 < 时：getline作用于当前文件，读入当前文件的第一行给其后跟的变量var或$0（无变量）,
应该注意到，由于awk在处理getline之前已经读入了一行，所以getline得到的返回结果是隔行的

当其左右有重定向符 | 或 < 时：getline则作用于定向输入文件，由于该文件是刚打开，并没有被awk读入一行，
只是getline读入，那么getline返回的是该文件的第一行，而不是隔行
comment

awk 'BEGIN{ "date" | getline out; print out }'  # 执行date并通过管道输出给getline，再把输出赋给自定义变量out

# 执行date并通过管道输出给getline，getline将输入赋值给out，split函数把变量out转为数组mon，再打印mon第二个元素
awk 'BEGIN{ "date" | getline out; split(out,mon); print mon[2] }'

# ls -l输出传递给geline，循环使getline读取每一行并只打印对应权限。因为BEGIN块在打开输入文件前执行，所以可以忽略输入文件
awk 'BEGIN{ while( "ls -l" | getline) print $1}'

echo | awk '{printf("hello word!n") > "datafile"}'  # awk中允许用如下方式将结果输出到一个文件

```

```bash
# 关闭文件
# awk中允许在程序中关闭一个输入或输出文件，方法是使用awk的close语句
# file可以是getline打开的文件，也可以是stdin，包含文件名的变量或者getline使用的确切命令。或一个输出文件，
# 可以是stdout，包含文件名的变量或使用管道的确切命令,例如

echo "21 2
3 52
17 23" | awk '{
first[NR]=$1
second[NR]=$2
}END{
print "======打印第1列并排序：===========" > "test.txt"
close("test.txt")
for(i in first)
  print first[i] |"sort -n >> test.txt"
close("sort -n >> test.txt")

print "======打印第2列并排序：===========" >> "test.txt"
close("test.txt")
for(i in second)
  print second[i] |"sort -n >> test.txt"
}
close("sort -n >> test.txt")
'
: << comment
# 以上命令输出为,任何一个close都不能去掉，因为awk管道使用时，若不关闭将会被一致使用。
======打印第1列并排序：===========
3
17
21
======打印第2列并排序：===========
2
23
52
comment

: << comment
# close去掉后输出
======打印第1列并排序：===========
======打印第2列并排序：===========
2
3
17
21
23
52
comment
```

## 流程控制语句

```bash
# awk的while、do-while和for语句中允许使用break,continue语句来控制流程走向，也允许使用exit这样的语句来退出。
# break中断当前正在执行的循环并跳到循环外执行下一条语句。if 是流程选择用法。awk中，流程控制语句，语法结构，与c语言类型。
# 有了这些语句，其实很多shell程序都可以交给awk，而且性能是非常快的。下面是各个语句用法

# if条件判断语句，示例判断数字大小进行对应的输出,输出：very good
awk 'BEGIN{
test=100;
if(test>90){
print "very good";
}
else if(test>60){
print "good";
}
else{
print "no pass";
}
}'

# while循环语句，示例：求1到100和,输出：5050
awk 'BEGIN{
test=100;
total=0;
while(i<=test){
total+=i;
i++;
}
print total;
}'

# for循环语句，for循环有两种格式：
# 格式1示例：以行的形式打印每个环境变量及其对应值。注：ENVIRON是awk常量，是子典型数组
awk 'BEGIN{
for(k in ENVIRON){
print k"="ENVIRON[k];
}
}'

# 格式2示例：同样以求1到100和
awk 'BEGIN{
total=0;
for(i=0;i<=100;i++){
total+=i;
}
print total;
}'

# do循环语句,示例：求1到100和
awk 'BEGIN{ total=0; i=0; do {total+=i;i++;} while(i<=100); print total }'

: << comment
# 其他语句
break       当break 语句用于 while 或 for 语句时，导致退出程序循环
continue    当continue 语句用于 while 或 for 语句时，使程序循环移动到下一个迭代
next        能能够导致读入下一个输入行，并返回到脚本的顶部。这可以避免对当前输入行执行其他的操作过程
exit        语句使主输入循环退出并将控制转移到END,若END存在。若没有定义END规则，或在END中应用exit语句，则终止脚本执行
comment
```

## 数组应用

数组是awk的灵魂，处理文本中最不能少的就是它的数组处理。因为数组索引（下标）可以是数字和字符串在awk中数组叫做关联数组
(associative arrays)。awk 中的数组不必提前声明，也不必声明大小。数组元素用0或空字符串来初始化，这根据上下文而定

```bash
# 数组的定义,数字做数组索引（下标）：
Array[1]="sun"
Array[2]="kai"

# 字符串做数组索引（下标）：使用print Array[1]会打印出sun；使用print Array[2]会打印出kai；使用print["birth"]会得到1987
Array["first"]="www"
Array"[last"]="name"
Array["birth"]="1987"

# 读取数组的值,格式示例如下：
{ for(item in array) {print array[item]}; } # 输出的顺序是随机的
{ for(i=1;i<=len;i++) {print array[i]}; } # Len是数组的长度
```

### 数组相关函数

```bash
# length返回字符串以及数组长度，split进行分割字符串为数组，也会返回分割得到数组长度,asort对数组进行排序，返回数组长度
awk 'BEGIN{info="it is a test";split(info,tA," ");print asort(tA);}'    # 输出：4

awk 'BEGIN{info="it is a test";lens=split(info,tA," ");print length(tA),lens;}' # 得到数组长度,输出：4 4

awk 'BEGIN{info="it is a test";split(info,tA," ");for(k in tA){print k,tA[k];}}'    # 输出数组内容（无序，有序输出）

# for ... in 输出，因为数组是关联数组，默认是无序的。固通过`for…in`得到是无序数组。如果需得到有序数组，需要通过下标获得
# 注意：数组下标是从1开始，与C数组不一样
awk 'BEGIN{info="it is a test";tlen=split(info,tA," ");for(k=1;k<=tlen;k++){print k,tA[k];}}'

# 判断键值存在以及删除键值，以下为错误的判断方法
# tB[“c”]没有定义，但循环时已存在该键值且值为空，注意：awk数组是关联数组，只要通过数组引用它的key就会自动创建改序列
awk 'BEGIN{tB["a"]="a1";tB["b"]="b1";if(tB["c"]!="1"){print "no found";};for(k in tB){print k,tB[k];}}' # 错误判断方法
awk 'BEGIN{tB["a"]="a1";tB["b"]="b1";if( "c" in tB){print "ok";};for(k in tB){print k,tB[k];}}'         # 正确判断方法

# if(key in array)通过这种方法判断数组中是否包含`key`键值
awk 'BEGIN{tB["a"]="a1";tB["b"]="b1";delete tB["a"];for(k in tB){print k,tB[k];}}'  # 删除键值

# delete array[key]可以删除，对应数组`key`的，序列值
```

### 二维、多维数组使用

awk的多维数组在本质上是一维数组，更确切一点，awk在存储上并不支持多维数组。awk提供了逻辑上模拟二维数组的访问方式。
例如，`array[2,4]=1`这样的访问是允许的。awk使用一个特殊的字符串`SUBSEP(34)`作为分割字段，在上面的例子中，关联数组
array存储的键值实际上是2344(此处存疑，暂未实际验证)

类似一维数组的成员测试，多维数组可以使用`if ( (i,j) in array)`这样的语法，但是下标必须放置在圆括号中。类似一维数组
的循环访问，多维数组使用`for ( item in array )`这样的语法遍历数组。与一维数组不同的是，多维数组必须使用`split()`函数
来访问单独的下标分量

```bash
# 打印99乘法表
awk 'BEGIN{
for(i=1;i<=9;i++){
for(j=1;j<=9;j++){
tarr[i,j]=i*j; print i,"*",j,"=",tarr[i,j];}}}'

# 可以通过array[k,k2]引用获得数组内容,另一种方法：
awk 'BEGIN{
for(i=1;i<=9;i++){
for(j=1;j<=9;j++){
tarr[i,j]=i*j;}}
for(m in tarr){
split(m,tarr2,SUBSEP); print tarr2[1],"*",tarr2[2],"=",tarr[m];}}'
```

## 内置函数

awk内置函数，主要分以下3种类似：算数函数、字符串函数、其它一般函数、时间函数。

### 算术函数

| 格式 | 描述 |
| ---- | ---- |
| atan2( y, x ) | 返回 y/x 的反正切 |
| cos( x ) | 返回 x 的余弦；x 是弧度 |
| sin( x ) | 返回 x 的正弦；x 是弧度 |
| exp( x ) | 返回 x 幂函数 |
| log( x ) | 返回 x 的自然对数 |
| sqrt( x ) | 返回 x 平方根 |
| int( x ) | 返回 x 的截断至整数的值 |
| rand( ) | 返回任意数字 n，其中 0 <= n < 1 |
| srand( [expr] ) | 将 rand 函数的种子值设置为 Expr 参数的值，或如果省略 Expr 参数则使用某天的时间返回先前的种子值 |

```bash
# 示例：OFMT 设置输出数据格式是保留3位小数
awk 'BEGIN{OFMT="%.3f";fs=sin(1);fe=exp(10);fl=log(10);fi=int(3.1415);print fs,fe,fl,fi;}'  # 0.841 22026.466 2.303 3

awk 'BEGIN{srand();fr=int(100*rand());print fr;}'   # 获得随机数
```

### 字符串函数

| 格式 | 描述 |
| ---- | ---- |
| gsub( Ere, Repl, [ In ] ) | 除了正则表达式所有具体值被替代这点，它和 sub 函数完全一样地执行。 |
| sub( Ere, Repl, [ In ] ) | 用 Repl 参数指定的字符串替换 In 参数指定的字符串中的由 Ere 参数指定的扩展正则表达式的第一个具体值。sub 函数返回替换的数量。出现在 Repl 参数指定的字符串中的 &（和符号）由 In 参数指定的与 Ere 参数的指定的扩展正则表达式匹配的字符串替换。如果未指定 In 参数，缺省值是整个记录（$0 记录变量）。 |
| index( String1, String2 ) | 在由 String1 参数指定的字符串（其中有出现 String2 指定的参数）中，返回位置，从 1 开始编号。如果 String2 参数不在 String1 参数中出现，则返回 0（零）。 |
| length [(String)] | 返回 String 参数指定的字符串的长度（字符形式）。如果未给出 String 参数，则返回整个记录的长度（$0 记录变量）。 |
| blength [(String)] | 返回 String 参数指定的字符串的长度（以字节为单位）。如果未给出 String 参数，则返回整个记录的长度（$0 记录变量）。 |
| substr( String, M, [ N ] ) | 返回具有 N 参数指定的字符数量子串。子串从 String 参数指定的字符串取得，其字符以 M 参数指定的位置开始。M 参数指定为将 String 参数中的第一个字符作为编号 1。如果未指定 N 参数，则子串的长度将是 M 参数指定的位置到 String 参数的末尾 的长度。 |
| match( String, Ere ) | 在 String 参数指定的字符串（Ere 参数指定的扩展正则表达式出现在其中）中返回位置（字符形式），从 1 开始编号，或如果 Ere 参数不出现，则返回 0（零）。RSTART 特殊变量设置为返回值。RLENGTH 特殊变量设置为匹配的字符串的长度，或如果未找到任何匹配，则设置为 -1（负一）。|
| split( String, A, [Ere] ) | 将 String 参数指定的参数分割为数组元素 A[1], A[2], . . ., A[n]，并返回 n 变量的值。此分隔可以通过 Ere 参数指定的扩展正则表达式进行，或用当前字段分隔符（FS 特殊变量）来进行（如果没有给出 Ere 参数）。除非上下文指明特定的元素还应具有一个数字值，否则 A 数组中的元素用字符串值来创建。 |
| tolower( String ) | 返回 String 参数指定的字符串，字符串中每个大写字符将更改为小写。大写和小写的映射由当前语言环境的 LC_CTYPE 范畴定义。 |
| toupper( String ) | 返回 String 参数指定的字符串，字符串中每个小写字符将更改为大写。大写和小写的映射由当前语言环境的 LC_CTYPE 范畴定义。 |
| sprintf(Format, Expr, Expr, . . . ) | 根据 Format 参数指定的 printf 子例程格式字符串来格式化 Expr 参数指定的表达式并返回最后生成的字符串。 |

```bash
# 注：Ere都可以是正则表达式。gsub,sub使用
# 在 info中查找满足正则表达式，`/[0-9]+/` 用`””`替换，并且替换后的值，赋值给info 未给info值，默认是`$0`
awk 'BEGIN{info="this is a test2010test!";gsub(/[0-9]+/,"!",info);print info}'  # 输出：this is a test!test!

# 查找字符串（index使用），找到返回ok，未找到，返回0
awk 'BEGIN{info="this is a test2010test!";print index(info,"test")?"ok":"no found";}'

# 正则表达式匹配查找(match使用）
awk 'BEGIN{info="this is a test2010test!";print match(info,/[0-9]+/)?"ok":"no found";}'

# 截取字符串(substr使用）。从第 4个 字符开始，截取10个长度字符串
awk 'BEGIN{info="this is a test2010test!";print substr(info,4,10);}'    # 输出：s is a tes

# 字符串分割（split使用）
# 分割info,动态创建数组tA，awk for … in循环是一个无序的循环。并不是从数组下标1到n ，因此使用时候需要注意
awk 'BEGIN{info="this is a test";split(info,tA," ");print length(tA);for(k in tA){print k,tA[k];}}'
```

### 格式化字符串输出（sprintf使用）

格式化字符串格式：其中格式化字符串包括两部分内容：一部分是正常字符，这些字符将按原样输出; 另一部分是格式化规定字符，
以`"%"`开始，后跟一个或几个规定字符,用来确定输出内容格式

| 格式 | 描述 | 格式 | 描述 |
| ---- | ---- | ---- | ---- |
| %d | 十进制有符号整数 | %u | 十进制无符号整数 |
| %f | 浮点数 | %s | 字符串 |
| %c | 单个字符 | %p | 指针的值 |
| %e | 指数形式的浮点数 | %x | %X 无符号以十六进制表示的整数 |
| %o | 无符号以八进制表示的整数 | %g | 自动选择合适的表示法 |

```bash
awk 'BEGIN{n1=124.113;n2=-1.224;n3=1.2345; printf("%.2f,%.2u,%.2g,%X,%on",n1,n2,n3,n1,n1);}'
# 输出：124.11,18446744073709551615,1.2,7C,174
```

### 一般函数

| 格式 | 描述|
| ---- | ---- |
| close( Expression ) | 用同一个带字符串值的 Expression 参数来关闭由 print 或 printf 语句打开的或调用 getline 函数<br>打开的文件或管道。如果文件或管道成功关闭，则返回 0；其它情况下返回非零值。如果打算写一个文件，并稍后在同一个程序中<br>读取文件，则 close 语句是必需的 |
| system(command ) | 执行 Command 参数指定的命令，并返回退出状态。等同于 system 子例程 |
| Expression `\|` getline [ Variable ] | 从来自 Expression 参数指定的命令的输出中通过管道传送的流中读取一个输入记录<br>并将该记录的值指定给 Variable 参数指定的变量。如果当前未打开将 Expression 参数的值作为其命令名称的流，则创建流。创建<br>的流等同于调用 popen 子例程，此时 Command 参数取 Expression 参数的值且 Mode 参数设置为一个是 r 的值。只要流保留打开<br>且Expression 参数求得同一个字符串，则对 getline 函数的每次后续调用读取另一个记录。如果未指定 Variable 参数，<br>则 $0 记录变量和 NF 特殊变量设置为从流读取的记录 |
| getline [ Variable ] < Expression | 从 Expression 参数指定的文件读取输入的下一个记录，并将 Variable 参数指定的变<br>量设置为该记录的值。只要流保留打开且 Expression 参数对同一个字符串求值，则对 getline 函数的每次后续调用读取另一个记录<br>如果未指定 Variable 参数，则 $0 记录变量和 NF 特殊变量设置为从流读取的记录 |
| getline [ Variable ] | 将 Variable 参数指定的变量设置为从当前输入文件读取的下一个输入记录。如果未指定 Variable 参数<br>则 $0 记录变量设置为该记录的值，还将设置 NF、NR 和 FNR 特殊变量 |

```bash
# 打开外部文件（close用法）
awk 'BEGIN{while("cat /etc/passwd"|getline){print $0;};close("/etc/passwd");}'

# 逐行读取外部文件(getline使用方法）
awk 'BEGIN{while(getline < "/etc/passwd"){print $0;};close("/etc/passwd");}'

awk 'BEGIN{print "Enter your name:";getline name;print name;}'

# 调用外部应用程序(system使用方法）
awk 'BEGIN{b=system("ls -al");print b;}'    # b返回值，是执行结果
```

### 时间函数

| 格式 | 描述|
| ---- | ---- |
| 函数名 | 说明 |
| mktime( YYYY MM dd HH MM ss[ DST]) | 生成时间格式 |
| strftime([format [, timestamp]]) | 格式化时间输出，将时间戳转为时间字符串具体格式，见下表。 |
| systime() | 得到时间戳，返回从1970年1月1日开始到当前时间(不计闰年)的整秒数 |

```bash
# 指定时间(mktime使用）
awk 'BEGIN{tstamp=mktime("2001 01 01 12 12 12");print strftime("%c",tstamp);}'
awk 'BEGIN{tstamp1=mktime("2001 01 01 12 12 12");tstamp2=mktime("2001 02 01 0 0 0");print tstamp2-tstamp1;}'

# 求2个时间段中间时间差，介绍了strftime使用方法
awk 'BEGIN{tstamp1=mktime("2001 01 01 12 12 12");tstamp2=systime();print tstamp2-tstamp1;}'
```

strftime日期和时间格式说明符

| 格式 | 描述|
| ---- | ---- |
| %a | 星期几的缩写(Sun) |
| %A | 星期几的完整写法(Sunday) |
| %b | 月名的缩写(Oct) |
| %B | 月名的完整写法(October) |
| %c | 本地日期和时间 |
| %d | 十进制日期 |
| %D | 日期 08/20/99 |
| %e | 日期，如果只有一位会补上一个空格 |
| %H | 用十进制表示24小时格式的小时 |
| %I | 用十进制表示12小时格式的小时 |
| %j | 从1月1日起一年中的第几天 |
| %m | 十进制表示的月份 |
| %M | 十进制表示的分钟 |
| %p | 12小时表示法(AM/PM) |
| %S | 十进制表示的秒 |
| %U | 十进制表示的一年中的第几个星期(星期天作为一个星期的开始) |
| %w | 十进制表示的星期几(星期天是0) |
| %W | 十进制表示的一年中的第几个星期(星期一作为一个星期的开始) |
| %x | 重新设置本地日期(08/20/99) |
| %X | 重新设置本地时间(12:00:00) |
| %y | 两位数字表示的年(99) |
| %Y | 当前月份 |
| %% | 百分号(%) |

## 文件间隔

```bash
# 双空间文件
awk'1; {print“”}'
awk'BEGIN {ORS =“\ n \ n”}; 1'

# 双空间的文件已经有空行。输出文件,在文本行之间应该包含不超过一个空白行。
# 注意：在Unix系统上，只有CRLF（\ r \ n）的DOS行是经常被视为非空白，因此仅'NF'将返回TRUE
awk'NF {print $ 0“\ n”}'

# 三重空间文件
awk'1; {print“\ n”}'
```

## 编号和计算

```bash

# 在每行的前面加上行号为该文件（左对齐）,使用\t而不是空格将保留页边距
awk'{print FNR "\t" $0}'文件

# 在每行的前面加上行号FOR ALL FILES TOGETHER，并带有制表符
awk'{print NR \t $0}'文件

# 编号文件的每一行（左边的数字，右对齐）,如果从DOS命令提示符处键入，则将符号加倍
awk '{printf("%5d：%s \ n",NR,$0)}'

# 为文件的每一行编号，但如果行不是空白，则只打印数字。记住关于\ r的Unix处理的注意事项（如上所述）
awk 'NF { $0=++a ":" $0}; 1'
awk '{ print(NF?++a ":") $0}'

awk'END {print NR}' # 计数行（模拟“wc -l”）
awk '{s = 0; for(i = 1; i <= NF; i ++)s = s + $ i; print s}'  # 打印每行的字段总和
awk'{for（i = 1; i <= NF; i ++）s = s + $ i}; END {print s}'  # 添加所有行中的所有字段并打印总和

#在用绝对值替换每个字段后，每行打印一行
awk'{for（i = 1; i <= NF; i ++）if（$ i <0）$ i =-$ i; 打印}'
awk'{for（i = 1; i <= NF; i ++）$ i =（$ i <0）？ -$ i：$ i; 打印}'

#在所有行中打印字段总数（“字数”）
awk'{total = total + NF}; END {打印总计}'文件

#打印包含“Beth”的总行数
awk'/ Beth / {n ++}; END {print n + 0}'文件

#打印最大的第一个字段和包含它的行
#旨在查找字段#1中最长的字符串
awk'$ 1> max {max = $ 1; MAXLINE = $ 0}; END {print max，maxline}'

#打印每行中的字段数，然后是行
awk'{print NF'：“$ 0}'

#打印每行的最后一个字段
awk'{print $ NF}'

#打印最后一行的最后一个字段
awk'{field = $ NF}; END {打印字段}'

#打印每行超过4个字段
awk'NF> 4'

#打印最后一个字段值大于4的每一行
awk'$ NF> 4'

创建字符串：

#创建一个特定长度的字符串（例如，生成513个空格）
awk'BEGIN {while（a ++ <513）s = s“”; 打印s}'

#在特定字符位置插入特定长度的字符串
#示例：在每个输入行的#6列之后插入49个空格。
gawk --re-interval'BEGIN {while（a ++ <49）s = s“”}; {sub（/ ^。{6} /，“＆”s）}; 1'
```

## 阵列创作

```sh

#接下来的2个条目不是单行脚本，而是技术
#非常方便，因此在这里值得一试。

#创建一个名为“月”的数组，索引数字，以便该月[1]
#是'Jan'，月份[2]是'Feb'，月份[3]是'Mar'等等。
拆分（“1月2月3月4月5月6月7月8月9月10月11月12月”，月，“”）

#创建一个名为“mdigit”的数组，用字符串索引，这样
#mdigit [“Jan”]是1，mdigit [“Feb”]是2等等。需要“月”数组
for（i = 1; i <= 12; i ++）mdigit [month [i]] = i

```

## 文本转换和替换：

```sh

#在UNIX环境中：将DOS换行符（CR / LF）转换为Unix格式
awk'{sub（/ \ r $ /，“”）}; 1'#假设每行都以Ctrl-M结尾

#在UNIX环境中：将Unix换行符（LF）转换为DOS格式
awk'{sub（/ $ /，“\ r”）}; 1'

#在DOS环境下：将Unix换行符（LF）转换为DOS格式
awk 1

#在DOS环境下：将DOS换行符（CR / LF）转换为Unix格式
#不能用DOS版本的awk完成，除了gawk：
gawk -v BINMODE =“w”'1'infile> outfile

#使用“tr”代替。
tr -d \ r <infile> outfile#GNU tr版本1.22或更高

#从每行前面删除前导空格（空格，制表符）
#左对齐所有文本
awk'{sub（/ ^ [\ t] + /，“”）}; 1'

#从每行末尾删除尾随空格（空格，制表符）
awk'{sub（/ [\ t] + $ /，“”）}; 1'

#删除每行的前导和尾随空白
awk'{gsub（/ ^ [\ t] + | [\ t] + $ /，“”）}; 1'
awk'{$ 1 = $ 1}; 1'#也会删除字段之间的额外空间

#在每行的开头插入5个空格（使页面偏移）
awk'{sub（/ ^ /，“”）}; 1'

#将所有文本均匀对齐到79列宽度
awk'{printf'％79s \ n“，$ 0}'文件*

#将所有文字放在79个字符的宽度上
awk'{l = length（）; s = int（（79-1）/ 2）; printf“％”（s + l）“s \ n”，$ 0}'文件*

#在每行上用“bar”代替（查找并替换）“foo”
awk'{sub（/ foo /，“bar”）}; 1'#只替换第一个实例
gawk'{$ 0 = gensub（/ foo /，“bar”，4）}; 1'#只替换第四个实例
awk'{gsub（/ foo /，“bar”）}; 1'#将所有实例替换成一行

#将“foo”替换为“bar”，仅用于包含“baz”
awk'/ baz / {gsub（/ foo /，“bar”）}; 1'

#将“foo”替换为“bar”除了包含“baz”的行以外
awk'！/ baz / {gsub（/ foo /，“bar”）}; 1'

#将“猩红”或“红宝石”或“puce”改为“红色”
awk'{gsub（/ scarlet | ruby​​ | puce /，“red”）}; 1'

#行的反向顺序（模拟“tac”）
awk'{a [i ++] = $ 0} END {for（j = i-1; j> = 0;）print a [j--]}'file *

#如果一行以反斜杠结尾，则将下一行追加到它（如果失败，则失败
#有多行以反斜杠结尾......）
awk'/ \\ $ / {sub（/ \\ $ /，“”）; getline t; 打印$ 0 t; 下一个}; 1'文件*

#打印并排序所有用户的登录名
awk -F“：”'{print $ 1 | “sort”}'/ etc / passwd

#按每行的相反顺序打印前两个字段
awk'{print $ 2，$ 1}'文件

#切换每行的前两个字段
awk'{temp = $ 1; $ 1 = $ 2; $ 2 = temp}'文件

#打印每一行，删除该行的第二个字段
awk'{$ 2 =“”; 打印}'

#按相反顺序打印每行的字段
awk'{for（i = NF; i> 0; i--）printf（“％s”，$ i）; print“”}'file

#使用逗号分隔符连接每5行输入
#字段之间
awk'ORS = NR％5？“，”：“\ n”'文件

```

## 选择性印刷某些线条

```sh

#打印前10行文件（模拟“head”的行为）
awk'NR <11'

#打印文件的第一行（模拟“head -1”）
awk'NR> 1 {exit}; 1'

 #打印文件的最后两行（模拟“tail -2”）
awk'{y = x“\ n”$ 0; x = $ 0}; END {print y}'

#打印文件的最后一行（模拟“tail -1”）
awk'END {print}'

#只打印符合正则表达式的行（模拟“grep”）
awk'/ regex /'

#只打印与正则表达式不匹配的行（模拟“grep -v”）
awk'！/ regex /'

#打印字段#5等于“abc123”的任何行
awk'$ 5 ==“abc123”'

#仅打印字段#5不等于“abc123”的行
#这也将打印少于5个字段的行。
awk'$ 5！=“abc123”'
awk'！（$ 5 ==“abc123”）'

#将字段与正则表达式匹配
awk'$ 7〜/ ^ [af] /'#print line if field#7 matches regex
awk'$ 7！〜/ ^ [af] /'#print line if field#7 does not match regex

#在正则表达式之前立即打印行，但不是行
#包含正则表达式
awk'/ regex / {print x}; {x = $ 0}'
awk'/ regex / {print（NR == 1？“match line 1：x）}; {x = $ 0}'

#在正则表达式之后立即打印行，但不是行
#包含正则表达式
awk'/ regex / {getline; print}'

#grep for AAA和BBB和CCC（在同一行上以任意顺序）
awk'/ AAA / && / BBB / && / CCC /'

#grep用于AAA和BBB和CCC（按此顺序）
awk'/AAA.*BBB.*CCC/'

#只能打印65个字符或更长的行
awk'长度> 64'

#仅打印少于65个字符的行
awk'长度<64'

#从正则表达式到文件结束的文件的打印部分
awk'/ regex /，0'
awk'/ regex /，EOF'

#根据行号打印文件部分（第8-12行，含）
awk'NR == 8，NR == 12'

#打印行号52
awk'NR == 52'
awk'NR == 52 {print; exit}'#在大文件上效率更高

#打印两个正则表达式之间的文件部分（含）
awk'/爱荷华州/，/蒙大拿州/'#区分大小写

```

## 选择性删除某些行

```sh

# 删除文件中的所有空白行（与“grep”。'相同）
awk NF
awk'/./'

# 删除重复的连续行（模拟“uniq”）
awk'a！〜$ 0; {A = $ 0}”

# 删除重复的，不连续的行
awk'！a [$ 0] ++'＃最简洁的脚本
awk'！（$ a中）{a [$ 0]; print}'＃最高效的脚本

# 删除重复的行
awk '!($0 in array) { array[$0]; print }' temp

```

## 统计apache日志单ip访问请求数排名（常用，解答方法10多种）

```sh

方法一：
awk '{++S[$1]} END {for (variable in S) print variable ,S[variable]}' access.log |sort -rn -k2
$1为第一个域的内容。-k2 为对第二个字段排序，即对数量排序。

方法二：
awk '{print $1}' access.log|sort|uniq -c |sort -rn -k1

方法三：
sed's/- -.*$//g' access.log|sort|uniq -c|sort -rn -k1

```

## 打印行号和内容：

```sh

awk '{print NR":"$0}'

输出：偶数行和奇数行到文件

awk '{print $0.txt > NR%2.txt}'  file

打印出奇数行内容：（三者等价）

awk 'NR%2==1' file  

awk 'NR%2' all_file.txt

awk 'i=!i' file

打印出偶数行的内容：（三者等价）

awk 'NR%2==0' file

awk '!(NR%2)' file

awk '!(i=!i)' file

```


