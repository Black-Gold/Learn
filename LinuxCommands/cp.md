cp
===

将源文件或目录复制到目标文件或目录中

## 补充说明

**cp命令** 用来将一个或多个源文件或者目录复制到指定的目的文件或目录。它可以将单个源文件复制成一个指定文件名的具体的文件或一个已经存在的目录下。cp命令还支持同时复制多个文件，当一次复制多个文件时，目标文件参数必须是一个已经存在的目录，否则将出现错误。

### 语法  

```
cp(选项)(参数)
```

### 选项  

```
用法：cp [选项]... [-T] 源文件 目标文件
　或：cp [选项]... 源文件... 目录
　或：cp [选项]... -t 目录 源文件...
Copy SOURCE to DEST, or multiple SOURCE(s) to DIRECTORY.

必选参数对长短选项同时适用。
  -a, --archive                 等于-dR --preserve=all
      --attributes-only 仅复制属性而不复制数据      --backup[=CONTROL        为每个已存在的目标文件创建备份
  -b                            类似--backup 但不接受参数
      --copy-contents           在递归处理是复制特殊文件内容
  -d                            等于--no-dereference --preserve=links,当复制符号连接时，把目标文件或目录也建立为符号连接，并指向与源文件或目录连接的原始文件或目录；
  -f, --force                   强行复制文件或目录，不论目标文件或目录是否已存在强行复制文件或目录，不论目标文件或目录是否已存在
  -i, --interactive             覆盖既有文件之前先询问用户
  -H                           follow command-line symbolic links in SOURCE
  -l, --link                   对源文件建立硬连接，而非复制文件
  -L, --dereference            always follow symbolic links in SOURCE
  -n, --no-clobber              不要覆盖已存在的文件(使前面的 -i 选项失效)
  -P, --no-dereference          不跟随源文件中的符号链接
  -p                            等于--preserve=模式,所有权,时间戳
      --preserve[=属性列表      保持指定的属性(默认：模式,所有权,时间戳)，如 果
                                        可能保持附加属性：环境、链接、xattr  等
      --sno-preserve=属性列表   不保留指定的文件属性
      --parents                 复制前在目标目录创建来源文件路径中的所有目录
  -R, -r, --recursive           递归复制目录及其子目录内的所有内容
      --reflink[=WHEN]          控制克隆/CoW 副本。请查看下面的内如。
      --remove-destination      尝试打开目标文件前先删除已存在的目的地
                                        文件 (相对于 --force 选项)
      --sparse=WHEN             控制创建稀疏文件的方式
      --strip-trailing-slashes  删除参数中所有源文件/目录末端的斜杠
  -s, --symbolic-link           只创建符号链接而不复制文件
  -S, --suffix=后缀             自行指定备份文件的后缀
  -t,  --target-directory=目录  将所有参数指定的源文件/目录
                                           复制至目标目录
  -T, --no-target-directory     将目标目录视作普通文件
  -u, --update                  只在源文件比目标文件新，或目标文件
                                        不存在时才进行复制
  -v, --verbose         显示详细的进行步骤
  -x, --one-file-system 不跨越文件系统进行操作
  -Z                           set SELinux security context of destination
                                 file to default type
      --context[=CTX]          like -Z, or if CTX is specified then set the
                                 SELinux or SMACK security context to CTX
      --help            显示此帮助信息并退出
      --version         显示版本信息并退出

默认情况下，源文件的稀疏性仅仅通过简单的方法判断，对应的目标文件目标文件也
被为稀疏。这是因为默认情况下使用了--sparse=auto 参数。如果明确使用
--sparse=always 参数则不论源文件是否包含足够长的0 序列也将目标文件创文
建为稀疏件。
使用--sparse=never 参数禁止创建稀疏文件。

当指定了--reflink[=always] 参数时执行轻量化的复制，即只在数据块被修改的
情况下才复制。如果复制失败或者同时指定了--reflink=auto，则返回标准复制模式。

The backup suffix is '~', unless set with --suffix or SIMPLE_BACKUP_SUFFIX.
The version control method may be selected via the --backup option or through
the VERSION_CONTROL environment variable.  Here are the values:

  none, off       不进行备份(即使使用了--backup 选项)
  numbered, t     备份文件加上数字进行排序
  existing, nil   若有数字的备份文件已经存在则使用数字，否则使用普通方式备份
  simple, never   永远使用普通方式备份

有一个特别情况：如果同时指定--force 和--backup 选项，而源文件和目标文件
是同一个已存在的一般文件的话，cp 会将源文件备份。
```

### 参数  

*   源文件：制定源文件列表。默认情况下，cp命令不能复制目录，如果要复制目录，则必须使用`-R`选项；
*   目标文件：指定目标文件。当“源文件”为多个文件时，要求“目标文件”为指定的目录。

### 实例  

下面的第一行中是 cp 命令和具体的参数（-r 是“递归”， -u 是“更新”，-v 是“详细”）。接下来的三行显示被复制文件的信息，最后一行显示命令行提示符。这样，只拷贝新的文件到我的存储设备上，我就使用 cp 的“更新”和“详细”选项。

通常来说，参数 `-r` 也可用更详细的风格 `--recursive`。但是以简短的方式，也可以这么连用 `-ruv`。

```
cp -r -u -v /usr/men/tmp ~/men/tmp
```

版本备份 `--backup=numbered` 参数意思为“我要做个备份，而且是带编号的连续备份”。所以一个备份就是 1 号，第二个就是 2 号，等等。

```bash
$ cp --force --backup=numbered test1.py test1.py
$ ls
test1.py test1.py.~1~ test1.py.~2~
```

如果把一个文件复制到一个目标文件中，而目标文件已经存在，那么，该目标文件的内容将被破坏。此命令中所有参数既可以是绝对路径名，也可以是相对路径名。通常会用到点`.`或点点`..`的形式。例如，下面的命令将指定文件复制到当前目录下：

```
cp ../mary/homework/assign .
```

所有目标文件指定的目录必须是己经存在的，cp命令不能创建目录。如果没有文件复制的权限，则系统会显示出错信息。

将文件file复制到目录`/usr/men/tmp`下，并改名为file1

```
cp file /usr/men/tmp/file1
```

将目录`/usr/men`下的所有文件及其子目录复制到目录`/usr/zh`中

```
cp -r /usr/men /usr/zh
```

交互式地将目录`/usr/men`中的以m打头的所有.c文件复制到目录`/usr/zh`中

```
cp -i /usr/men m*.c /usr/zh
```

我们在Linux下使用cp命令复制文件时候，有时候会需要覆盖一些同名文件，覆盖文件的时候都会有提示：需要不停的按Y来确定执行覆盖。文件数量不多还好，但是要是几百个估计按Y都要吐血了，于是折腾来半天总结了一个方法：

```
cp aaa/* /bbb
复制目录aaa下所有到/bbb目录下，这时如果/bbb目录下有和aaa同名的文件，需要按Y来确认并且会略过aaa目录下的子目录。

cp -r aaa/* /bbb
这次依然需要按Y来确认操作，但是没有忽略子目录。

cp -r -a aaa/* /bbb
依然需要按Y来确认操作，并且把aaa目录以及子目录和文件属性也传递到了/bbb。

\cp -r -a aaa/* /bbb
成功，没有提示按Y、传递了目录属性、没有略过目录。
```


<!-- Linux命令行搜索引擎：https://jaywcjlove.github.io/linux-command/ -->
