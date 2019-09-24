# **dd**

## 说明

**dd命令** 用于复制文件并对原文件的内容进行转换和格式化处理。dd命令功能很强大的，对于一些比较底层的问题，使用dd命令往往
可以得到出人意料的效果。用的比较多的还是用dd来备份裸设备。但是不推荐，如果需要备份oracle裸设备，可以使用rman备份，或使用
第三方软件备份，使用dd的话，管理起来不太方便

建议在有需要的时候使用dd 对物理磁盘操作，如果是文件系统的话还是使用tar backup cpio等其他命令更加方便。另外，使用dd对磁盘
操作时，最好使用块设备文件

其次，dd命令可以创建一个固定大小的文件如下：
dd if=/dev/zero of=/var/swap/file.swap bs=1024K count=64（ linux支持K单位，unix不支持；）

## 选项

```markdown
bs=BYTES        一次读写BYTES字节数
cbs=BYTES       一次转换BYTES字节数,即指定转换缓冲区大小
conv=CONVS      以逗号分隔的参数列表转换文件,具体参数见下面详述
count=N         仅复制N个输入块,块大小等于ibs指定的字节数
ibs=BYTES       一次读取BYTES字节 (default: 512)
if=FILE         从文件读取而不是从标准输入读取
iflag=FLAGS     按逗号分隔的参数列表读取
obs=BYTES       一次写入BYTES字节 (default: 512)
of=FILE         从文件写入而不是从标准输出
oflag=FLAGS     按逗号分隔的参数列表写入
seek=N          在输出开始时跳过N个obs-sized的块
skip=N          在输入开始时跳过N个ibs-sized的块
status=LEVEL    要打印到stderr的信息的级别; 'none'除了错误消息之外禁止其他所有输出，'noxfer'禁止最终传输统计信息，
                'progress'显示定期传输统计信息

N和BYTES之后可以跟随以下乘法后缀:
c =1, w =2, b =512, kB =1000, K =1024, MB =1000*1000, M =1024*1024, xM =M
GB =1000*1000*1000, G =1024*1024*1024, and so on for T, P, E, Z, Y.

每个CONV符号可以是:
ascii     from EBCDIC to ASCII
ebcdic    from ASCII to EBCDIC
ibm       from ASCII to alternate EBCDIC
block     pad newline-terminated records with spaces to cbs-size
unblock   replace trailing spaces in cbs-size records with newline
lcase     change upper case to lower case
ucase     change lower case to upper case
sparse    try to seek rather than write the output for NUL input blocks
swab      swap every pair of input bytes
sync      pad every input block with NULs to ibs-size; when used with block or unblock, pad with spaces rather than NULs
excl      fail if the output file already exists
nocreat   do not create the output file
notrunc   不截断输出文件
noerror   读取数据发生错误后仍然继续
fdatasync 结束前将输出文件数据写入磁盘
fsync     类似上面，但是元数据也一同写入

FLAG 符号可以是：

append       追加模式(仅对输出有意义；隐含了conv=notrunc)
directory    使用直接I/O 存取模式
directory    除非是目录，否则 directory 失败
dsync        使用同步I/O 存取模式
sync         与上者类似，但同时也对元数据生效
fullblock    为输入积累完整块(仅iflag)
nonblock     使用无阻塞I/O 存取模式
noatime      不更新存取时间
nocache      丢弃缓存数据
noctty       不根据文件指派控制终端
nofollow     不跟随链接文件
count_bytes  treat 'count=N' as a byte count (iflag only)
skip_bytes   treat 'skip=N' as a byte count (iflag only)
seek_bytes   treat 'seek=N' as a byte count (oflag only)

Sending a USR1 signal to a running 'dd' process makes it
print I/O statistics to standard error and then resume copying.

  $ dd if=/dev/zero of=/dev/null& pid=$!
  $ kill -USR1 $pid; sleep 1; kill $pid
  18335302+0 records in
  18335302+0 records out
  9387674624 bytes (9.4 GB) copied, 34.6279 seconds, 271 MB/s

```

## 实例

```bash
dd if=/dev/zero of=sun.txt bs=1M count=1    # 可以看出dd命令来测试内存操作速度
```

该命令创建了一个1M大小的文件sun.txt，其中参数解释：

* **if**  代表输入文件。如果不指定if，默认就会从stdin中读取输入。
* **of**  代表输出文件。如果不指定of，默认就会将stdout作为默认输出。
* **bs**  代表字节为单位的块大小。
* **count**  代表被复制的块数。
* **/dev/zero**  是一个字符设备，会不断返回0值字节（\0）

块大小可以使用的计量单位表

| 单元大小 | 代码 |
| :------: | :------: |
| 字节(1B) | c |
| 字节(2B) | w |
| 块(512B) | b |
| 千字节（1024B） | k |
| 兆字节（1024KB） | M |
| 吉字节（1024MB） | G |

```bash
## 用dd命令备份磁盘
dd if=/dev/sda of=/deb/sdb  # if表示inputfile，of表示outputfile。参数conv=noerror，如果存在读取错误，它仍将继续复制
dd if=/dev/hda of=~/hdadisk.img     # 创建硬盘镜像
dd if=hdadisk.img of=/dev/hdb   # 从硬盘镜像恢复
dd if=/dev/hda1 of=~/partition1.img     # 备份分区
dd if=/dev/cdrom of=tgsservice.iso bs=2048  # 备份CDROM
dd bs=1M if=/dev/sda | gzip | ssh user@remote 'dd of=sda.gz'   # 将硬盘sda压缩并备份到远程机器上
dd bs=1 seek=2TB if=/dev/null of=ext4.test # 建立一个大的测试文件（不占用空间）
time dd if=/dev/zero bs=1024 count=1000000 of=/1Gb.file # 测试所在磁盘的写入速度
dd if=/root/1Gb.file bs=64k | dd of=/dev/null   # 测试磁盘的读取速度

# 确定硬盘的最佳块大小
dd if=/dev/zero bs=1024 count=1000000 of=/root/1Gb.filedd if=/dev/zero bs=2048 count=500000 of=/root/1Gb.filedd \
if=/dev/zero bs=4096 count=250000 of=/root/1Gb.filedd if=/dev/zero bs=8192 count=125000 of=/root/1Gb.file

```