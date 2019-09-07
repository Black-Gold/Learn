# **touch**

## 说明

**touch命令** 有两个功能：一是用于把已存在文件的时间标签更新为系统当前的时间（默认方式），它们的数据将原封不动地
保留下来；二是用来创建新的空文件

## 选项

```markdown
-a：或--time=atime或--time=access或--time=use  只更改存取时间；
-c：或--no-create  不建立任何文件；
-d：<时间日期> 使用指定的日期时间，而非现在的时间；
-f：此参数将忽略不予处理，仅负责解决BSD版本touch指令的兼容性问题；
-m：或--time=mtime或--time=modify  只更该变动时间；
-r：<参考文件或目录>  把指定文件或目录的日期时间，统统设成和参考文件或目录的日期时间相同；
-t：<日期时间>  使用指定的日期时间，而非现在的时间；

用法：touch [选项]... 文件...
Update the access and modification times of each FILE to the current time.

A FILE argument that does not exist is created empty, unless -c or -h
is supplied.

A FILE argument string of - is handled specially and causes touch to
change the times of the file associated with standard output.

Mandatory arguments to long options are mandatory for short options too.
  -a			只更改访问时间
  -c, --no-create	不创建任何文件
  -d, --date=字符串	使用指定字符串表示时间而非当前时间
  -f			(忽略)
  -h, --no-dereference		会影响符号链接本身，而非符号链接所指示的目的地
				(当系统支持更改符号链接的所有者时，此选项才有用)
  -m			只更改修改时间
  -r, --reference=FILE   use this file's times instead of current time
  -t STAMP               use [[CC]YY]MMDDhhmm[.ss] instead of current time
      --time=WORD        change the specified time:
                           WORD is access, atime, or use: equivalent to -a
                           WORD is modify or mtime: equivalent to -m
请注意，-d 和-t 选项可接受不同的时间/日期格式
```

## 实例

```bash
touch -c -t 0304050607 file # 改变文件file的时间标签
```
