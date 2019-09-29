# **xargs**

## 说明

**xargs命令** 是给其他命令传递参数的一个过滤器，也是组合多个命令的一个工具。它擅长将标准输入数据转换成命令行参数，xargs能够处理管道或者
stdin并将其转换成特定命令的命令参数。xargs也可以将单行或多行文本输入转换为其他格式，例如多行变单行，单行变多行。xargs的默认命令是echo，
空格是默认定界符。这意味着通过管道传递给xargs的输入将会包含换行和空白，不过通过xargs的处理，换行和空白将被空格取代。xargs是构建单行命令
的重要组件之一

## 选项

```markdown
xargs [OPTION]... COMMAND INITIAL-ARGS...
Run COMMAND with arguments INITIAL-ARGS and more arguments read from input.

非强制性参数以[方括号]表示

-0, --null                   Items are separated by a null, not whitespace.
                             Disables quote and backslash processing
-a, --arg-file=FILE          Read arguments from FILE, not standard input
-d, --delimiter=CHARACTER    Input items are separated by CHARACTER, not by
                             blank space. Disables quote and backslash
                             processing
-E END                       If END occurs as a line of input, the rest of
                             the input is ignored.
-e [END], --eof[=END]        Equivalent to -E END if END is specified.
                             Otherwise, there is no end-of-file string
--help                       Print a summary of the options to xargs.
-I R                         same as --replace=R (R must be specified)
-i,--replace=[R]             Replace R in initial arguments with names
                             read from standard input. If R is
                             unspecified, assume {}
-L,-l, --max-lines=MAX-LINES Use at most MAX-LINES nonblank input lines per
                             command line
-l                           Use at most one nonblank input line per
                             command line
-n, --max-args=MAX-ARGS      Use at most MAX-ARGS arguments per command
                             line
-P, --max-procs=MAX-PROCS    Run up to max-procs processes at a time
-p, --interactive            Prompt before running commands
--process-slot-var=VAR       Set environment variable VAR in child
                             processes
-r, --no-run-if-empty        If there are no arguments, run no command.
                             If this option is not given, COMMAND will be
                             run at least once.
-s, --max-chars=MAX-CHARS    Limit commands to MAX-CHARS at most
--show-limits                Show limits on command-line length.
-t, --verbose                Print commands before executing them
--version                    Print the version number
-x, --exit                   Exit if the size (see -s) is exceeded

```

## 实例

```bash
cat test.txt | xargs -n3    # 多行输出
echo "nameXnameXnameXname" | xargs -dX  # -d选项自定义一个定界符
echo "nameXnameXnameXname" | xargs -dX -n2  # 读取stdin，将格式化后的参数传递给命令
ls *.jpg | xargs -n1 -I cp {} /data/images # 复制所有图片文件到 /data/images 目录
find . -type f -name "*.log" -print0 | xargs -0 rm -f
find . -type f -name "*.php" -print0 | xargs -0 wc -l   # 统计一个源代码目录中所有php文件的行数
find . -type f -name "*.jpg" -print | xargs tar -czvf images.tar.gz # 查找所有的jpg 文件，并且压缩它们
cat url-list.txt | xargs wget -c    # list.txt包含了很多下载的URL，使用xargs下载所有链接

```



