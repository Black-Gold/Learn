# **od**

## 说明

**od命令** 用于输出文件的八进制、十六进制或其它格式编码的字节，通常用于显示或查看文件中不能直接显示在终端的字符

常见的文件为文本文件和二进制文件。此命令主要用来查看保存在二进制文件中的值。比如，程序可能输出大量的数据记录，每个数据是
一个单精度浮点数。这些数据记录存放在一个文件中，如果想查看下这个数据，这时候od命令就派上用场了。在我看来，od命令主要用来
格式化输出文件数据，即对文件中数据进行无二义性的解释。不管是IEEE754格式浮点数还是ASCII码，od命令都能按照需求输出它们的值

## 选项

```markdown
-a：此参数的效果和同时指定“-ta”参数相同；
-A：<字码基数>：选择以何种基数计算字码；
-b：此参数的效果和同时指定“-toC”参数相同；
-c：此参数的效果和同时指定“-tC”参数相同；
-d：此参数的效果和同时指定“-tu2”参数相同；
-f：此参数的效果和同时指定“-tfF”参数相同；
-h：此参数的效果和同时指定“-tx2”参数相同；
-i：此参数的效果和同时指定“-td2”参数相同；
-j<字符数目>或--skip-bytes=<字符数目>：略过设置的字符数目；
-l：此参数的效果和同时指定“-td4”参数相同；
-N<字符数目>或--read-bytes=<字符数目>：到设置的字符树目为止；
-o：此参数的效果和同时指定“-to2”参数相同；
-s<字符串字符数>或--strings=<字符串字符数>：只显示符合指定的字符数目的字符串；
-t<输出格式>或--format=<输出格式>：设置输出格式；
-v或--output-duplicates：输出时不省略重复的数据；
-w<每列字符数>或--width=<每列字符数>：设置每列的最大字符数；
-x：此参数的效果和同时指定“-h”参数相同；


用法：od [选项]... [文件]...
　或：od [-abcdfilosx]... [文件] [[+]偏移量[.][b]]
　或：od --traditional [选项]... [文件] [[+]偏移量[.][b] [+][标签][.][b]]

将指定文件以八进制形式(默认)转储到标准输出。如果指定了多于一个的文件
参数，程序会自动将输入的内容整合为列表并以同样的形式输出。
如果没有指定文件，或指定文件为"-"，程序从标准输入读取数据。

If first and second call formats both apply, the second format is assumed
if the last operand begins with + or (if there are 2 operands) a digit.
An OFFSET operand means -j OFFSET.  LABEL is the pseudo-address
at first byte printed, incremented when dump is progressing.
For OFFSET and LABEL, a 0x or 0X prefix indicates hexadecimal;
suffixes may be . for octal and b for multiply by 512.

Mandatory arguments to long options are mandatory for short options too.
  -A, --address-radix=RADIX   output format for file offsets; RADIX is one
                                of [doxn], for Decimal, Octal, Hex or None
  -j, --skip-bytes=BYTES      skip BYTES input bytes first
  -N, --read-bytes=BYTES      limit dump to BYTES input bytes
  -S BYTES, --strings[=BYTES]  output strings of at least BYTES graphic chars;
                                3 is implied when BYTES is not specified
  -t, --format=TYPE           select output format or formats
  -v, --output-duplicates     do not use * to mark line suppression
  -w[BYTES], --width[=BYTES]  output BYTES bytes per output line;
                                32 is implied when BYTES is not specified
      --traditional           accept arguments in third form above
      --help		显示此帮助信息并退出
      --version		显示版本信息并退出


Traditional format specifications may be intermixed; they accumulate:
  -a   same as -t a,  select named characters, ignoring high-order bit
  -b   same as -t o1, select octal bytes
  -c   same as -t c,  select printable characters or backslash escapes
  -d   same as -t u2, select unsigned decimal 2-byte units
  -f	即 -t fF，指定浮点数对照输出格式
  -i	即 -t dl，指定十进制整数对照输出格式
  -l	即 -t dL，指定十进制长整数对照输出格式
  -o	即 -t o2，指定双字节单位八进制数的对照输出格式
  -s	即 -t d2，指定双字节单位十进制数的对照输出格式
  -x	即 -t x2，指定双字节单位十六进制数的对照输出格式


TYPE is made up of one or more of these specifications:
  a          named character, ignoring high-order bit
  c          printable character or backslash escape
  d[尺寸]	有符号十进制数，每个整形数占指定尺寸的字节
  f[尺寸]	浮点数，每个整形数占指定尺寸的字节
  o[尺寸]	八进制数，每个整形数占指定尺寸的字节
  u[尺寸]	无符号十进制数，每个整形数占指定尺寸的字节
  x[尺寸]	十六进制数，每个整形数占指定尺寸的字节

SIZE is a number.  For TYPE in [doux], SIZE may also be C for
sizeof(char), S for sizeof(short), I for sizeof(int) or L for
sizeof(long).  If TYPE is f, SIZE may also be F for sizeof(float), D
for sizeof(double) or L for sizeof(long double).

Adding a z suffix to any type displays printable characters at the end of
each output line.


BYTES is hex with 0x or 0X prefix, and may have a multiplier suffix:
  b    512
  KB   1000
  K    1024
  MB   1000*1000
  M    1024*1024
and so on for G, T, P, E, Z, Y.


```

### 参数  

文件：指定要显示的文件。

### 实例  

```
[linuxde@localhost ~]$ echo abcdef g > tmp
[linuxde@localhost ~]$ cat tmp
abcdef g
```

说明：先准备一个tmp文件

```
[linuxde@localhost ~]$ od -b tmp
0000000 141 142 143 144 145 146 040 147 012
0000011
```

说明：使用单字节八进制解释进行输出，注意左侧的默认地址格式为八字节

```
[linuxde@localhost ~]$ od -c tmp
0000000   a   b   c   d   e   f       g  \n
0000011
```

说明：使用ASCII码进行输出，注意其中包括转义字符

```
[linuxde@localhost ~]$ od -t d1 tmp
0000000   97   98   99  100  101  102   32  103   10
0000011
```

说明：使用单字节十进制进行解释

```
[linuxde@localhost ~]$ od -A d -c tmp
0000000   a   b   c   d   e   f       g  \n
0000009
```

说明：设置地址格式为十进制。

```
[linuxde@localhost ~]$ od -A x -c tmp
000000   a   b   c   d   e   f       g  \n
000009
```

说明：设置地址格式为十六进制

```
[linuxde@localhost ~]$ od -j 2 -c tmp
0000002   c   d   e   f       g  \n
0000011
```

说明：跳过开始的两个字节

```
[linuxde@localhost ~]$ od -N 2 -j 2 -c tmp
0000002   c   d
0000004
```

说明：跳过开始的两个字节，并且仅输出两个字节

```
[linuxde@localhost ~]$ od -w1 -c tmp
0000000   a
0000001   b
0000002   c
0000003   d
0000004   e
0000005   f
0000006   
0000007   g
0000010  \n
0000011
```

说明：每行仅输出1个字节

```
[linuxde@localhost ~]$ od -w2 -c tmp
0000000   a   b
0000002   c   d
0000004   e   f
0000006       g
0000010  \n
0000011
```

说明：每行输出两个字节

```
[linuxde@localhost ~]$ od -w3 -b tmp
0000000 141 142 143
0000003 144 145 146
0000006 040 147 012
0000011
```

说明：每行输出3个字节，并使用八进制单字节进行解释


