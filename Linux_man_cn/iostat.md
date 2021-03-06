# **iostat**

## 说明

**iostat命令** 被用于监视系统输入输出设备和CPU的使用情况。它的特点是汇报磁盘活动统计情况，同时也会汇报出CPU使用情况
同vmstat一样，iostat也有一个弱点，就是它不能对某个进程进行深入分析，仅对系统的整体情况进行分析
[源码](http://github.com/sysstat/sysstat)

## 选项

```markdown
-c：仅显示CPU使用情况
-d：仅显示设备利用率
-k：显示状态以千字节每秒为单位，而不使用块每秒
-m：显示状态以兆字节每秒为单位
-p：仅显示块设备和所有被使用的其他分区的状态
-t：显示每个报告产生时的时间
-V：显示版号并退出
-x：显示扩展状态

*   间隔时间：每次报告的间隔时间（秒）
*   次数：显示报告的次数

配置文件目录：/etc/sysconfig
```

## 实例

```bash
iostat -x /dev/sda1 # 查看磁盘sda1的I/O详细情况
iostat -d -k 1 1 # 查看TPS(该设备每秒的传输次数)和吞吐量
iostat -d -x -k 1 1 # 查看设备使用率（%util）和响应时间（await）

: << comment
输出说明：
%iowait的值过高，表示硬盘存在I/O瓶颈
%util 接近100%，说明产生的I/O请求太多，I/O系统已经满负荷，该磁盘可能存在瓶颈
svctm 比较接近 await，说明 I/O 几乎没有等待时间
await 远大于 svctm，说明I/O 队列太长，io响应太慢，则需要进行必要优化
avgqu-sz比较大，也表示有大量io在等待
idble小于70%，I/O负荷过大，进程读取有过多的等待，用vmstat查看b参数(等待资源的进程数)和wa参数(I/O等待所占用的CPU时间
百分比，高于30%说明I/O压力较高)
comment
```

详细说明：第二行是系统信息和监测时间，第三行和第四行显示CPU使用情况（具体内容和mpstat命令相同）。这里主要关注后面I/O
输出的信息，如下所示：

| 标示 | 说明 |
| :------: | :------: |
| Device | 监测设备名称 |
| rrqm/s | 每秒需要读取需求的数量 |
| wrqm/s | 每秒需要写入需求的数量 |
| r/s  | 每秒实际读取需求的数量 |
| w/s | 每秒实际写入需求的数量 |
| rsec/s | 每秒读取区段的数量 |
| wsec/s | 每秒写入区段的数量 |
| rkB/s | 每秒实际读取的大小，单位为KB |
| wkB/s | 每秒实际写入的大小，单位为KB |
| avgrq-sz | 需求的平均大小区段 |
| avgqu-sz | 需求的平均队列长度 |
| await | 等待I/O平均的时间（milliseconds） |
| svctm | I/O需求完成的平均时间 |
| %util | 被I/O需求消耗的CPU百分比 |

如果 %util 接近 100%,说明产生的I/O请求太多,I/O系统已经满负荷,该磁盘可能存在瓶颈.

idle小于70% IO压力就较大了,一般读取速度有较多的wait.同时可以结合vmstat 查看查看b参数(等待资源的进程数)和wa参数(IO等待所
占用的CPU时间的百分比,高过30%时IO压力高);另外 await 的参数也要多和 svctm 来参考.差的过高就一定有 IO 的问题.一般地系统IO
响应时间(await)应该低于5ms，如果大于10ms就比较大

avgqu-sz 也是个做 IO 调优时需要注意的地方,这个就是直接每次操作的数据的大小,如果次数多,但数据拿的小的话,其实 IO 也会很小
如果数据拿的大,才IO 的数据会高.也可以通过 avgqu-sz × ( r/s or w/s ) = rsec/s or wsec/s.也就是讲,读定速度是这个来决定的

CPU属性值说明：
%user：  CPU处在用户模式下的时间百分比
%nice：  CPU处在带NICE值的用户模式下的时间百分比
%system：CPU处在系统模式下的时间百分比
%iowait：CPU等待输入输出完成时间的百分比
%steal： 管理程序维护另一个虚拟处理器时，虚拟CPU的无意识等待时间百分比
%idle：  CPU空闲时间百分比


