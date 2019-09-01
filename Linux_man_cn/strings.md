# strings

## 说明

**strings命令** 在对象文件或二进制文件中查找可打印的字符串。字符串是4个或更多可打印字符的任意序列，以换行符或空字符结束,
strings命令对识别随机对象文件很有用

## 选项

```markdown
用法：strings [选项] [文件]
 打印 [文件] (默认为标准输入) 中可打印的字符串

-a - --all                扫描整个文件而不是只扫描目标文件初始化和装载段 [default]
-d --data                 Only scan the data sections in the file
-f --print-file-name      在显示字符串前先显示文件名
-n --bytes=[number]       找到并且输出所有NUL终止符序列
-<number>                 设置显示的最少的字符数，默认是4个字符(default 4).
-t --radix={o,d,x}        输出字符的位置，基于八进制，十进制或者十六进制
-w --include-all-whitespace Include all whitespace as valid string characters
-o                        An alias for --radix=o
-T --target=<BFDNAME>     指定二进制文件格式
-e --encoding={s,S,b,l,B,L}     选择字符大小和排列顺序:s = 7-bit, S = 8-bit, {b,l} = 16-bit, {B,L} = 32-bit
-s --output-separator=<string> String used to separate strings in output.
@<file>                   从<file>读取选项

strings：支持的目标： elf64-x86-64 elf32-i386 elf32-iamcu elf32-x86-64 a.out-i386-linux pei-i386 pei-x86-64 elf64-l1om
elf64-k1om elf64-little elf64-big elf32-little elf32-big plugin srec symbolsrec verilog tekhex binary ihex

```

## 实例

```bash
# 列出ls中所有的ASCII文本
strings /bin/ls     
cat /bin/ls strings

strings /bin/ls | grep -i libc  # 查找ls中包含libc的字符串，不区分大小写

```
