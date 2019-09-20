# **sar**

## 说明

**sar命令** System Activity Reporter是Linux下系统运行状态统计工具，它将指定的操作系统状态计数器显示到标准输出设备。sar工
具将对系统当前的状态进行取样，然后通过计算数据和比例来表达系统的当前运行状态。它的特点是可以连续对系统取样，获得大量的取
样数据。取样数据和分析的结果都可以存入文件，使用它时消耗的系统资源很小。[源码](http://github.com/sysstat/sysstat)

```markdown
sar命令常用格式
sar [options] [-A] [-o file] t [n]

-A  显示所有的报告信息
-b  显示I/O速率
-B  显示换页状态
-c  显示进程创建活动
-d  显示每个块设备的状态
-e  设置显示报告的结束时间
-f  从指定文件提取报告
-i  设状态信息刷新的间隔时间
-P  报告每个CPU的状态
-R  显示内存状态
-u  显示CPU利用率
-v  显示索引节点，文件和其他内核表的状态
-w  显示交换分区状态
-x  显示给定进程的状态

*   间隔时间：每次报告的间隔时间（秒）
*   次数：显示报告的次数

配置文件目录：/etc/sysconfig
```

## 实例

```bash
sar -r  # 查看内存和交换空间的使用率
: << comment
输出解释：
kbmemfree与kbmemused字段分别显示内存的未使用与已使用空间，后面跟着的是已使用空间的百分比（%memused字段）
kbbuffers与kbcached字段分别显示缓冲区与系统全域的数据存取量，单位为KB
comment

sar -o temp 60 10   # 观察系统部件10分钟，并对数据进行排序
sar -u 1 3  # 查看CPU利用率
: << comment
输出详解：
%user：  显示在用户级别(application)运行使用 CPU 总时间的百分比.
%nice：  显示在用户级别,用于nice操作,所占用CPU总时间的百分比.
%system：在核心级别(kernel)运行所使用 CPU 总时间的百分比.
%iowait：显示用于等待I/O操作占用CPU总时间的百分比.
%steal： 管理程序(hypervisor)为另一个虚拟进程提供服务而等待虚拟CPU的百分比.
%idle：  显示CPU空闲时间占用CPU总时间的百分比
comment

sar -v  1 3     # 查看inode、文件和其他内核表状态
: << comment
输出详解：
dentunusd: 目录缓存中未使用的缓存条目数
file-nr:   由系统使用的文件数
inode-nr： 由系统使用的inode数 
pty-nr：   系统所使用的伪终端数
comment

sar -q  # 查看平均负载
: << comment
输出详解：
runq-sz： 运行队列的长度（等待运行的进程数）
plist-sz：进程列表中进程（processes）和线程（threads）的数量
ldavg-1： 最后1分钟的系统平均负载 
ldavg-5： 过去5分钟的系统平均负载
ldavg-15：过去15分钟的系统平均负载
comment

sar -R 1 5  # 查看内存状态
: << comment
输出详解：
frmpg/s :每秒钟系统释放的内存页数. 如果是负值，表示每秒钟被系统分配的内存页数.
bufpg/s :每秒钟系统分配多少内存页作为buffer使用. 如果是负值，表示系统在回收一定的buffer空间.
campg/s :每秒钟系统分配多少内存页作为bcached使用. 如果是负值，表示系统在回收一定的cached空间.
comment

sar -W  # 查看页面交换情况
: << comment
输出详解：
pswpin/s    Total number of swap pages the system brought in per second.
pswpout/s   Total number of swap pages the system brought out per second.
comment

sar -w 1 5  # 任务创建和系统切换活动情况
: << comment
输出详解：
proc/s： 每秒创建的任务的总数.
cswch/s：每秒上下文切换的总数.
comment

sar -b 1 5  # I/O和传输速率统计
: << comment
输出详解：
tps：    每秒钟向物理设备发出请求(读与写)的总数
rtps:    每秒钟向物理设备发出读请求的总数
wtps:    每秒钟向物理设备发出写请求的总数
bread/s: 每秒从块设备中读取的数据总数
bwrtn/s: 每秒向块设备中写入的数据总数
comment

sar -B 1 5  # 输出paging信息
: << comment
输出详解：
pgpgin/s:  每秒从磁盘或SWAP置换到内存的字节数
pgpgout/s: 每秒从内存置换到磁盘或SWAP的字节数
fault/s:   每秒钟系统产生的缺页数,即主缺页与次缺页之和(major + minor)
majflt/s： 每秒钟产生的主缺页数
pgfree/s:  每秒被放入空闲队列中的页个数
pgscank/s: 每秒被kswapd扫描的页个数
pgscand/s: 每秒直接被扫描的页个数
pgsteal/s: 每秒钟从cache中被回收来满足内存需要的页个数
%vmeff:    每秒回收的页(pgsteal)占总扫描页(pgscank+pgscand)的百分比

缺页异常：
	major（内存中没有需要的数据）
	minor （内存中有这样的数据，单最先不是该进程的）
comment

sar -n DEV 1 1  # 此为查看lo、eth0接口网络信息，查看网络相关信息，可用参数为DEV、EDEV、SOCK、FULL
: << comment
输出详解：
IFACE：就是网络设备的名称；
rxpck/s：每秒钟接收到的包数
txpck/s：每秒钟发送出去的包数目
rxbyt/s：每秒钟接收到的字节数
txbyt/s：每秒钟发送出去的字节数
rxcmp/s：每秒钟接收到的压缩包数目
txcmp/s：每秒钟发送出去的压缩包数目
txmcst/s：每秒钟接收到的多播包的包数目

如果使用EDEV输出详解：
rxerr/s：每秒钟接收到的损坏的包的数目
txerr/s：当发送包时，每秒钟发生的错误数
coll/s： 当发送包时，每秒钟发生的冲撞(collisions)数（这个是在半双工模式下才有）
rxdrop/s：由于缓冲区满，网络设备接收端，每秒钟丢掉的网络包的数目
txdrop/s：由于缓冲区满，网络设备发送端，每秒钟丢掉的网络包的数目
txcarr/s：当发送数据包时，每秒钟载波错误发生的次数
rxfram/s：在接收数据包时，每秒钟发生的帧对齐错误的次数
rxfifo/s：在接收数据包时，每秒钟缓冲区溢出错误发生的次数
txfifo/s：在发送数据包时，每秒钟缓冲区溢出错误发生的次数

如果使用SOCK输出详解：
totsck：被使用的socket的总数目
tcpsck：当前正在被使用于TCP的socket数目
udpsck：当前正在被使用于UDP的socket数目
rawsck：当前正在被使用于RAW的socket数目
ip-frag：当前的IP分片的数目
comment
