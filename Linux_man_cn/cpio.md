# cpio

## 说明

**cpio命令** 将归档文件及从包中提取文件，cpio命令可以复制文件到归档包中，或者从归档包中复制文件

```markdown
cpio [OPTION...] [目标目录]

 主操作模式
  -i, --extract              从包中提取文件 (运行 copy-in 模式)
  -o, --create               创建包 (运行 copy-out 模式)
  -p, --pass-through         运行 copy-pass 模式
  -t, --list                 打印输入内容列表

 应用于所有模式的选项:

      --block-size=BLOCK-SIZE   设置 I/O 块大小为 BLOCK-SIZE * 512
                             字节
  -B                         设置 I/O 块大小为 5120 字节
  -c                         Identical to "-H newc", use the new (SVR4)
                             portable format.If you wish the old portable
                             (ASCII) archive format, use "-H odc" instead.
  -C, --io-size=NUMBER       设置 I/O 块大小为指定的 NUMBER 字节
      --force-local
                             包文件是本地的，尽管名字中含有冒号
  -f, --nonmatching          仅拷贝不匹配任意给定的模式的文件
  -F, --file=[[用户@]主机:]文件名
                             用“文件名”来替代标准输入和输出。如果是非本地的文件，则用可选的“用户”和“主机”来指定用户名和主机名
  -H, --format=格式        使用指定的包格式
  -M, --message=STRING       当到达备份介质的尾部的时候打印
                             STRING
  -n, --numeric-uid-gid      在内容列表的详表中，显示数字的 UID
                             和 GID
      --quiet                不要打印已拷贝的块数
      --rsh-command=COMMAND  用 COMMAND 替代 rsh
  -v, --verbose              详细列出已处理的文件
  -V, --dot                  每处理一个文件就打印一个“.”
  -W, --warning=FLAG         控制警告信息显示。当前 FLAG
                             可为“none”、“truncate”或“all”。多个选项可以累积

 命令修饰仅在 copy-in 模式中有效:

  -b, --swap
                             交换数据中每个字的两个半字以及每个半字中的两个字节。等价于
                             -sS
  -r, --rename               交互式重命名文件
  -s, --swap-bytes           交换文件中每个半字中的两个字节
  -S, --swap-halfwords
                             交换文件中每个字(4个字节)中的两个半字
      --to-stdout            提取文件到标准输出

  -E, --pattern-file=FILE    从 FILE
                             中读取额外的用于指定提取或列表的文件名的模式
      --only-verify-crc      When reading a CRC format archive, only verify the
                             checksum of each file in the archive, don't
                             actually extract the files

 应用于 copy-out 模式的选项

  -A, --append               追加到已存在的归档文件
      --device-independent, --reproducible
                             Create device-independent (reproducible) archives
      --ignore-devno         Don't store device numbers
  -O [[用户@]主机:]文件名
                             使用包文件名而不是标准输出。如果文件在远程机器上，则可指定用户和主机
      --renumber-inodes      Renumber inodes

 应用于 copy-pass 模式的选项:

  -l, --link                 在可行时链接文件而不是拷贝文件

 应用于 copy-in 及 copy-out 模式的选项:

      --absolute-filenames   文件名不去除文件系统前缀
      --no-absolute-filenames   相对于当前目录来创建所有文件

 应用于 copy-out 及 copy-pass 模式的选项:

-0, --null                 文件名列表采用 NULL
                           而不是换行作为分割符
-a, --reset-access-time    文件读取后恢复文件的访问时间
-I [[用户@]主机:]文件名
                           从文件读入而不是从标准输入读入
                           如果文件在远程机器上
                           则可指定用户和主机
-L, --dereference          跟随符号链接
                           (拷贝符号链接指向的文件而不是拷贝链接本身)
-R, --owner=[用户][:.][组]
                             设置所有文件的所有权信息到指定的用户和/或组

应用于 copy-in 和 copy-pass 模式的选项:
-d, --make-directories     需要时创建目录
-m, --preserve-modification-time
                           创建文件时保留以前文件的修改时间
    --no-preserve-owner    不改变文件的所有权
    --sparse
                           把含有大块零的文件以稀疏文件方式写出
-u, --unconditional        无条件覆盖所有文件

```

## 实例

```bash
cpio -o name-list > archive # 归档 name-list 中的文件到 archive
cpio -i < archive # 从 archive 中提取文件
cpio -p destination-directory < name-list   # 拷贝 name-list 中的文件到目标目录(destination-directory)
find / -print | cpio -covB > /dev/st0   # 将系统上所有资料备份到磁带机内，/dev/st0是磁带的设备名，代表SCSI磁带机
cpio -icdvt < /dev/st0 > /tmp/st_content    # 查看上例磁带机上备份的文件

find /etc -type f | cpio -ocvB >/opt/etc.cpio   # 将/etc下的所有普通文件都备份到/opt/etc.cpio
cpio -icduv < /opt/etc.cpio # 备份包etc.cpio还原到相应的位置，如果有相同文件进行覆盖
: << comment
注意，cpio恢复的路径，如果cpio在打包备份的时候用的是绝对路径，那么在恢复的时候会自动恢复到这些绝对路径下，本例就会将备份文件全部还原
到/etc路径下对应的目录中。同理，如果在打包备份用的是相对路径，还原时也将恢复到相对路径下
示例可以看出，cpio无法直接读取文件，它需要每个文件或者目录的完整路径名才能识别读取，而find命令的输出刚好做到了这点，因此，cpio命令一般
和find命令配合使用
comment
