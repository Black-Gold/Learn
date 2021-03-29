# **tail**

## 说明

**tail命令** 用于输入文件中的尾部内容。tail命令默认在屏幕上显示指定文件的末尾10行。如果给定的文件不止一个，则在显示的每个文件前面加
一个文件名标题。如果没有指定文件或者文件名为“-”，则读取标准输入

注意：如果表示bytes或lines的K值之前有一个”+”号，则从文件开头的第K项开始显示
K值后缀：b表示512，b 512, kB 1000, K 1024, MB 1000*1000, M 1024*1024,GB 1000*1000*1000,
G 1024*1024*1024, and so on for T, P, E, Z, Y

```markdown
-c, --bytes=K            输出最后K个字节；或使用-c + K输出从每个文件的第K个字节开始的字节
-f, --follow[={name|descriptor}]    随着文件的增长输出附加的数据；缺少的选项参数意味着“描述符”与--follow = name --retry相同
-n, --lines=K            output the last K lines, instead of the last 10;or use -n +K to output starting with the Kth
    --max-unchanged-stats=N     with --follow=name, reopen a FILE which has not changed size after N (default 5)
                                iterations to see if it has been unlinked or renamed (this is the usual case of
                                rotated log files);with inotify, this option is rarely useful
    --pid=PID            with -f, terminate after process ID, PID dies
-q, --quiet, --silent    never output headers giving file names
    --retry              keep trying to open a file if it is inaccessible
-s, --sleep-interval=N   with -f, sleep for approximately N seconds (default 1.0) between iterations;
                         with inotify and --pid=P, check process P at least once every N seconds

```

## 实例

```bash
tail file           # 显示文件file的最后10行
tail -n +20 file    # 显示文件file的内容，从第20行至文件末尾
tail -c 10 file     # 显示文件file的最后10个字符）
tail -5 file        # 显示file倒数第五行

```
