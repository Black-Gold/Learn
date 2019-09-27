# **printf**

## 说明

**printf命令** 格式化并输出结果到标准输出

## 选项

```markdown

和C语言printf一样，FORMAT控制输出，转义序列如下：

\"              双引号
\\              反斜杠
\a              警告字符，通常是ASCII的(BEL)字符
\b              后退
\c              抑制（不显示）输出结果中任何结尾的换行字符（只在%b格式指示符控制下的参数字符串中有效）
\e              escape
\f              换页(form feed)
\n              换行
\r              回车(carriage return)
\t              水平制表符
\v              垂直制表符
\NNN            byte with octal value NNN (1 to 3 digits)
\xHH            byte with hexadecimal value HH (1 to 2 digits)
\uHHHH          Unicode (ISO/IEC 10646) character with hex value HHHH (4 digits)
\UHHHHHHHH      Unicode character with hex value HHHHHHHH (8 digits)

%%     a single %
%b     ARGUMENT as a string with '\' escapes interpreted, except that octal escapes are of the form \0 or \0NNN

```

 **格式替代符** 

*   %b 相对应的参数被视为含有要被处理的转义序列之字符串
*   %c ASCII字符。显示相对应参数的第一个字符
*   %d, %i 十进制整数
*   %e, %E, %f 浮点格式
*   %g %e或%f转换，看哪一个较短，则删除结尾的零
*   %G %E或%f转换，看哪一个较短，则删除结尾的零
*   %o 不带正负号的八进制值
*   %s 字符串
*   %u 不带正负号的十进制值
*   %x 不带正负号的十六进制值，使用a至f表示10至15
*   %X 不带正负号的十六进制值，使用A至F表示10至15
*   %% 字面意义的%

## 实例

```bash
# %-5s 格式为左对齐且宽度为5的字符串代替（-表示左对齐），不使用则是又对齐
# %-4.2f 格式为左对齐宽度为4，保留两位小数
printf "%-5s %-10s %-4s\n" NO Name Mark
printf "%-5s %-10s %-4.2f\n" 01 Tom 90.3456
printf "%-5s %-10s %-4.2f\n" 02 Jack 89.2345
printf "%-5s %-10s %-4.2f\n" 03 Jeff 98.4323

```
