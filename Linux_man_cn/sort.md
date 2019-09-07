# **sort**

## 说明

**sort命令** 是在Linux里非常有用，它将文件进行排序，并将排序结果标准输出。sort命令既可以从特定的文件，也可以从stdin中获
取输入awk 'EXPRESSION { PROGRAM }' file(s)

```markdown
用法：sort [选项]... [文件]...
　或：sort [选项]... --files0-from=F
Write sorted concatenation of all FILE(s) to standard output.

Mandatory arguments to long options are mandatory for short options too.
排序选项：

-b, --ignore-leading-blanks	 忽略每行前面开始出的空格字符
-d, --dictionary-order	     只考虑空白区域和字母字符
-f, --ignore-case		     忽略字母大小写
-g, --general-numeric-sort  compare according to general numerical value
-i, --ignore-nonprinting    consider only printable characters
-M, --month-sort            compare (unknown) < 'JAN' < ... < 'DEC'
-h, --human-numeric-sort    使用易读性数字(例如： 2K 1G)
-n, --numeric-sort		    根据字符串数值比较
-R, --random-sort		    根据随机hash 排序
    --random-source=文件	从指定文件中获得随机字节
-r, --reverse			    逆序输出排序结果
    --sort=WORD		        按照WORD 指定的格式排序：一般数字-g，高可读性-h，月份-M，数字-n，随机-R，版本-V
-V, --version-sort		在文本内进行自然版本排序

其他选项：

    --batch-size=NMERGE	            一次最多合并NMERGE 个输入；如果输入更多则使用临时文件
-c, --check, --check=diagnose-first	检查输入是否已排序，若已有序则不进行操作
-C, --check=quiet, --check=silent	类似-c，但不报告第一个无序行
    --compress-program=程序	        使用指定程序压缩临时文件；使用该程序的-d 参数解压缩文件
    --debug			                为用于排序的行添加注释，并将有可能有问题的用法输出到标准错误输出
    --files0-from=文件	            从指定文件读取以NUL 终止的名称，如果该文件被指定为"-"则从标准输入读文件名
-k, --key=KEYDEF                    sort via a key; KEYDEF gives location and type
-m, --merge                         merge already sorted files; do not sort
-o, --output=文件		            将结果写入到文件而非标准输出
-s, --stable			            禁用last-resort 比较以稳定比较算法
-S, --buffer-size=大小	            指定主内存缓存大小
-t, --field-separator=分隔符	    使用指定的分隔符代替非空格到空格的转换
-T, --temporary-directory=目录	    使用指定目录而非$TMPDIR或/tmp作为临时目录，可用多个选项指定多个目录
    --parallel=N		            将同时运行的排序数改变为N
-u, --unique		                配合-c，严格校验排序；不配合-c，则只输出一次排序结果
-z, --zero-terminated	            以0 字节而非新行作为行尾标志

KEYDEF is F[.C][OPTS][,F[.C][OPTS]] for start and stop position, where F is a
field number and C a character position in the field; both are origin 1, and
the stop position defaults to the line's end.  If neither -t nor -b is in
effect, characters in a field are counted from the beginning of the preceding
whitespace.  OPTS is one or more single-letter ordering options [bdfgiMhnRrV],
which override global ordering options for that key.  If no key is given, use
the entire line as the key.

SIZE may be followed by the following multiplicative suffixes:
内存使用率% 1%，b 1、K 1024 (默认)，M、G、T、P、E、Z、Y 等依此类推。

如果不指定文件，或者文件为"-"，则从标准输入读取数据。

*** 警告 ***
本地环境变量会影响排序结果。如果希望以字节的自然值获得最传统的排序结果，请设置LC_ALL=C

```

## 实例

```bash
# sort将文件/文本的每一行作为一个单位，相互比较，比较原则是从首字符向后，依次按ASCII码值进行比较，最后默认按按升序输出
sort -t. -k1,1n -k2,2n -k3,3n -k4,4n    # 排序IPV4地址

# 以下命令如果是英文文本的话export LANG=C可以提高速度
sort -u file1 file2                 # 两个未排序文件的并集
sort file1 file2 | uniq -d          # 两个未排序文件的交集
sort file1 file1 file2 | uniq -u    # 两个未排序文件的差集
sort file1 file2 | uniq -u          # 两个未排序文件的对称差集

# 忽略相同行使用-u选项或者uniq
sort -u sort.txt 
uniq sort.txt

sort -nk 2 -t: sort.txt   # 将:字符作为分隔符，按其后的第二个字符的数字从小到大排序
# -n是按照数字大小排序，-r是以相反顺序，-k是指定需要爱排序的栏位，-t指定栏位分隔符为冒号

: << comment
-k选项的语法格式：
FStart.CStart Modifie,FEnd.CEnd Modifier
-------Start--------,-------End--------
 FStart.CStart 选项  ,  FEnd.CEnd 选项

这个语法格式可以被其中的逗号`,`分为两大部分， **Start** 部分和 **End** 部分。Start部分也由三部分组成，其中的Modifier部分
就是我们之前说过的类似n和r的选项部分。我们重点说说`Start`部分的`FStart`和`C.Start`。`C.Start`也是可以省略的，省略的话就
表示从本域的开头部分开始。`FStart.CStart`，其中`FStart`就是表示使用的域，而`CStart`则表示在`FStart`域中从第几个字符开始
算“排序首字符”。同理，在End部分中，你可以设定`FEnd.CEnd`，如果你省略`.CEnd`，则表示结尾到“域尾”，即本域的最后一个字
符。或者，如果你将CEnd设定为0(零)，也是表示结尾到“域尾”
comment

```

