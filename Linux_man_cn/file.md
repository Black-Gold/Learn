# **file**

## 说明

**file命令** 用来探测给定文件的类型。file命令对文件的检查分为文件系统、魔法幻数检查和语言检查3个过程

## 选项

```markdown
Usage: file [OPTION...] [FILE...]

-m, --magic-file LIST      使用LIST作为冒号分隔的幻数文件列表,即指定魔法数字文件
-z, --uncompress           尝试去解读压缩文件的内容
-b, --brief                列出辨识结果时，不显示文件名称
-c, --checking-printout    打印魔术文件的解析形式，与-m一起使用以在安装之前调试新的魔术文件
-e, --exclude TEST         从要对文件执行的测试列表中排除TEST
                有效的测试是：ascii，apptype，compress，elf，soft，tar，tokens，troff
-f, --files-from FILE      指定名称文件，其内容有一个或多个文件名称时，让file依序辨识这些文件，格式为每列一个文件名称
-F, --separator STRING     use string as separator instead of `:'
-i, --mime                 output MIME type strings (--mime-type and
                             --mime-encoding)
    --apple                output the Apple CREATOR/TYPE
    --mime-type            output the MIME type
    --mime-encoding        output the MIME encoding
-k, --keep-going           don't stop at the first match
-l, --list                 list magic strength
-L, --dereference          follow symlinks (default),即直接显示符号连接所指向的文件类别
-h, --no-dereference       don't follow symlinks
-n, --no-buffer            do not buffer output
-N, --no-pad               do not pad output
-0, --print0               terminate filenames with ASCII NUL
-p, --preserve-date        preserve access times on files
-r, --raw                  don't translate unprintable chars to \ooo
-s, --special-files        treat special (block/char devices) files as
                           ordinary ones
-C, --compile              compile file specified by -m
-d, --debug                print debugging messages

```

## 实例

```bash
file install.log        # 显示文件类型
file -i install.log     # 显示MIME类别

```
