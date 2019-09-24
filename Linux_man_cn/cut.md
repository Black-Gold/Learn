# **cut**

## 说明

**cut命令** 用来显示行中的指定部分，删除文件中指定字段。cut经常用来显示文件的内容，类似于type命令;该命令有两项功能，其一
是用来显示文件的内容，它依次读取由参数file所指 明的文件，将它们的内容输出到标准输出上；其二是连接两个或多个文件
如`cut fl f2 > f3`将把文件fl和几的内容合并起来，然后通过输出重定向符“>”的作用，将它们放入文件f3中

当文件较大时，文本在屏幕上迅速闪过（滚屏），用户往往看不清所显示的内容。因此，一般用more等命令分屏显示。为了控制滚屏，可
以按Ctrl+S键，停止滚屏；按Ctrl+Q键可以恢复滚屏。按Ctrl+C（中断）键可以终止该命令的执行，并且返回Shell提示符状态

## 选项

```markdown
Print selected parts of lines from each FILE to standard output.

Mandatory arguments to long options are mandatory for short options too.
-b, --bytes=列表		    只选中指定的这些字节
-c, --characters=列表		只选中指定的这些字符
-d, --delimiter=分界符	    使用指定分界符代替制表符作为区域分界
-f, --fields=LIST           只选择这些字段; 除非指定了-s选项，否则还会打印任何不包含分隔符的行,即显示指定字段的内容
-n                          与-b选项连用，不分割多字节字符
    --complement		    补全选中的字节、字符或域
-s, --only-delimited		不打印没有包含分界符的行
    --output-delimiter=字符串	使用指定的字符串作为输出分界符，默认采用输入的分界符

仅使用f -b, -c 或-f 中的一个。每一个列表都是专门为一个类别作出的，或者您可以用逗号隔
开要同时显示的不同类别。您的输入顺序将作为读取顺序，每个仅能输入一次。
每种参数格式表示范围如下：
    N	从第1 个开始数的第N 个字节、字符或域
    N-	从第N 个开始到所在行结束的所有字符、字节或域
    N-M	从第N 个开始到第M 个之间(包括第M 个)的所有字符、字节或域
    -M	从第1 个开始到第M 个之间(包括第M 个)的所有字符、字节或域

当没有文件参数，或者文件不存在时，从标准输入读取

```

## 实例

```bash
grep "model name" /proc/cpuinfo | uniq | cut -f2 -d :   # 显示CPU信息;-f截取,-d以:字符分界
cut -f2 --complement test.txt   # --complement选项提取指定字段之外的列（打印除了第二列之外的列）
cut -f2 -d";" test2.txt     # 使用-d选项指定字段分隔符
pip3 list -o --format columns | cut -d ' ' -f1 | xargs -n1 pip install -U   # 一次性升级所有pip包
ls /etc/rc3.d/S* | cut -c 15-   # 显示运行级别为3开启的服务

### 指定字段的字符或者字节范围  

: << comment
cut命令可以将一串字符作为列来显示，字符字段的记法：
*    **N-** ：从第N个字节、字符、字段到结尾
*    **N-M** ：从第N个字节、字符、字段到第M个（包括M在内）字节、字符、字段
*    **-M** ：从第1个字节、字符、字段到第M个（包括M在内）字节、字符、字段

上面是记法，结合下面选项将摸个范围的字节、字符指定为字段：
*    **-b**  表示字节
*    **-c**  表示字符
*    **-f**  表示定义字段
comment

cut -c1-3 test.txt  # 打印第1个到第3个字符
cut -c-2 test.txt   # 打印前2个字符
cut -c5- test.txt   # 打印从第5个字符开始到结尾

```
