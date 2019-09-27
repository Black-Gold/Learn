# **free**

## 说明

**free命令** 可以显示当前系统未使用的和已使用的内存数目，还可以显示被内核使用的内存缓冲区

## 选项

```bash
-b, --bytes     Bytes为单位显示内存使用
-k, --kilo      KB为单位显示内存使用(默认)
-m, --mega      MB为单位显示内存使用
-g, --giga      GB为单位显示内存使用
--tera          以TB为单位显示内存量
--peta          以PB为单位显示内存量
-h, --human     显示自动缩放到最短三位数单位的所有输出字段，并显示打印输出的单位。 使用以下单位
    B = bytes
    K = kilos
    M = megas
    G = gigas
    T = teras
    P = petas
-w, --wide          切换到宽屏模式。 宽模式生成超过80个字符的行。 在此模式下，缓冲区和缓存将在两个单独的列中报告
-c, --count count   显示结果计数次数。 需要-s选项
-l, --lohi          显示详细的高低内存统计信息
-s, --seconds seconds   间隔几秒显示结果，实际上可以指定任意浮点数
--si   Use power of 1000 not 1024
-t, --total 在一行以总和的形式显示内存的使用信息

```

## 实例

```bash
free -t    # 以总和的形式显示内存的使用信息
free -s 10 # 周期性的查询内存使用信息，每10s 执行一次命令
```

## free输出解释：

```markdown
total  安装的总内存 (MemTotal and SwapTotal in /proc/meminfo)
used   已用内存 (calculated as total - free - buffers - cache)
free   空闲内存 (MemFree and SwapFree in /proc/meminfo)
shared (大部分)被tmpfs使用的内存 (Shmem in /proc/meminfo, available on kernels 2.6.32, displayed as zero if not available)
buffers 被kernel buffers使用的内存 (Buffers in /proc/meminfo)
cache   被the page cache and slabs使用的内存 (Cached and Slab in /proc/meminfo)
buff/cache  buffers和cache的总和
available   估计可用于启动新应用程序的内存量，而无需交换。 与缓存或空闲字段提供的数据不同，此字段考虑了页面缓存，并且由于
正在使用的项目，并非所有可回收的内存块都将被回收（MemAvailable在/proc/meminfo中，在内核3.14上可用，模拟在内核2.6.27+，否则与免费相同）

关系：total = used + free

交换将通过三个途径来减少系统中使用的物理页面的个数：　
1. 减少缓冲与页面cache的大小
2. 将系统V类型的内存页面交换出去
3. 换出或者丢弃页面。(Application 占用的内存页，也就是物理内存不足）

事实上，少量地使用swap是不是影响到系统性能的。buffers和cached都是缓存，两者有什么区别呢？

为了提高磁盘存取效率, Linux做了一些精心的设计, 除了对dentry进行缓存(用于VFS,加速文件路径名到inode的转换), 还采取了两种主要Cache方式：

Buffer Cache和Page Cache。前者针对磁盘块的读写，后者针对文件inode的读写。这些Cache有效缩短了 I/O系统调用(比如read,write,getdents)的时间
磁盘的操作有逻辑级（文件系统）和物理级（磁盘块），这两种Cache就是分别缓存逻辑和物理级数据的

Page cache实际上是针对文件系统的，是文件的缓存，在文件层面上的数据会缓存到page cache。文件的逻辑层需要映射到实际的物理磁盘，这种映射关系由
文件系统来完成。当page cache的数据需要刷新时，page cache中的数据交给buffer cache，因为Buffer Cache就是缓存磁盘块的。但是这种处理在2.6版本的内核之后就变的很简单了，没有真正意义上的cache操作

Buffer cache是针对磁盘块的缓存，也就是在没有文件系统的情况下，直接对磁盘进行操作的数据会缓存到buffer cache中，例如，文件系统的元数据都会缓存到buffer cache中

简单说来，page cache用来缓存文件数据，buffer cache用来缓存磁盘数据。在有文件系统的情况下，对文件操作，那么数据会缓存到page cache，如果直接采用dd等工具对磁盘进行读写，那么数据会缓存到buffer cache

所以我们看linux,只要不用swap的交换空间,就不用担心自己的内存太少.如果常常swap用很多,可能你就要考虑加物理内存了.这也是linux看内存是否够用的标准.

如果是应用服务器的话，+buffers/cache,即对应用程序来说free的内存太少了，也是该考虑优化程序或加内存了

```

