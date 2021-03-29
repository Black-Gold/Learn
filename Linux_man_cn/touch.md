# **touch**

## 说明

**touch命令** 有两个功能：一是用于把已存在文件的时间标签更新为系统当前的时间（默认方式），它们的数据将原封不动地
保留下来；二是用来创建新的空文件

```markdown
用法：touch [选项]... 文件..

-a                      只更改访问时间
-c, --no-create         不创建任何文件
-d, --date=字符串        使用指定字符串表示时间而非当前时间
-f                      (忽略)
-h, --no-dereference    会影响符号链接本身，而非符号链接所指示的目的地，(当系统支持更改符号链接的所有者时，此选项才有用)
-m                      只更改修改时间
-r, --reference=FILE    用参考文件的时间取代当前时间
-t STAMP                使用指定的[[CC]YY]MMDDhhmm[.ss]时间取代当前时间
    --time=WORD         change the specified time:
                        WORD is access, atime, or use: equivalent to -a
                        WORD is modify or mtime: equivalent to -m
请注意，-d 和-t 选项可接受不同的时间/日期格式
```

## 实例

```bash
touch -c -t 0304050607 file # 改变文件file的时间
```
