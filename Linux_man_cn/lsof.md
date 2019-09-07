# **lsof**

## 说明

**lsof命令** 用于查看你进程开打的文件，打开文件的进程，进程打开的端口(TCP、UDP)。找回/恢复删除的文件。是十分方便的系统监
视工具，因为lsof命令需要访问核心内存和各种文件，所以需要root用户执行

在linux环境下，任何事物都以文件的形式存在，通过文件不仅仅可以访问常规数据，还可以访问网络连接和硬件。所以如传输控制协议
(TCP) 和用户数据报协议 (UDP) 套接字等，系统在后台都为该应用程序分配了一个文件描述符，无论这个文件的本质如何，该文件描
述符为应用程序与基础操作系统之间的交互提供了通用接口。因为应用程序打开文件的描述符列表提供了大量关于这个应用程序本身的信
息，因此通过lsof工具能够查看这个列表对系统监测以及排错将是很有帮助的

```markdown
-a：列出打开文件存在的进程
-c<进程名>：列出指定进程所打开的文件
-g：列出GID号进程详情
-d<文件号>：列出占用该文件号的进程
+d<目录>：列出目录下被打开的文件
+D<目录>：递归列出目录下被打开的文件
-n<目录>：列出使用NFS的文件
-i<条件>：列出符合条件的进程。（4、6、协议、:端口、 @ip ）
-p<进程号>：列出指定进程号所打开的文件
-u：列出UID号进程详情

 usage: [-?abhKlnNoOPRtUvVX] [+|-c c] [+|-d s] [+D D] [+|-f[gG]] [+|-e s]
 [-F [f]] [-g [s]] [-i [i]] [+|-L [l]] [+m [m]] [+|-M] [-o [o]] [-p s]
[+|-r [t]] [-s [p:s]] [-S [t]] [-T [t]] [-u s] [+|-w] [-x [fl]] [--] [names]
Defaults in parentheses; comma-separated set (s) items; dash-separated ranges.
  -?|-h list help          -a AND selections (OR)     -b avoid kernel blocks
  -c c  cmd c ^c /c/[bix]  +c w  COMMAND width (9)    +d s  dir s files
  -d s  select by FD set   +D D  dir D tree *SLOW?*   +|-e s  exempt s *RISKY*
  -i select IPv[46] files  -K list tasKs (threads)    -l list UID numbers
  -n no host names         -N select NFS files        -o list file offset
  -O no overhead *RISKY*   -P no port names           -R list paRent PID
  -s list file size        -t terse listing           -T disable TCP/TPI info
  -U select Unix socket    -v list version info       -V verbose search
  +|-w  Warnings (+)       -X skip TCP&UDP* files     -Z Z  context [Z]
  -- end option scan     
  +f|-f  +filesystem or -file names     +|-f[gG] flaGs 
  -F [f] select fields; -F? for help  
  +|-L [l] list (+) suppress (-) link counts < l (0 = all; default = 0)
                                        +m [m] use|create mount supplement
  +|-M   portMap registration (-)       -o o   o 0t offset digits (8)
  -p s   exclude(^)|select PIDs         -S [t] t second stat timeout (15)
  -T qs TCP/TPI Q,St (s) info
  -g [s] exclude(^)|select and print process group IDs
  -i i   select by IPv[46] address: [46][proto][@host|addr][:svc_list|port_list]
  +|-r [t[m<fmt>]] repeat every t seconds (15);  + until no files, - forever.
       An optional suffix to t is m<fmt>; m must separate t from <fmt> and
      <fmt> is an strftime(3) format for the marker line.
  -s p:s  exclude(^)|select protocol (p = TCP|UDP) states by name(s).
  -u s   exclude(^)|select login|UID set s
  -x [fl] cross over +d|+D File systems or symbolic Links
  names  select named files or files on named file systems
Anyone can list all files; /dev warnings disabled; kernel ID check disabled.


```

## 详解

lsof输出各列信息的意义如下:

* COMMAND：进程的名称
* PID：进程标识符
* PPID：父进程标识符（需要指定-R参数）
* USER：进程所有者
* PGID：进程所属组
* FD：文件描述符，应用程序通过文件描述符识别该文件。

文件描述符列表：

* cwd：表示current work dirctory，即：应用程序的当前工作目录，这是该应用程序启动的目录，除非它本身对这个目录进行更改
* txt：该类型的文件是程序代码，如应用程序二进制文件本身或共享库，如上列表中显示的 /sbin/init 程序
* lnn：library references (AIX);
* er：FD information error (see NAME column);
* jld：jail directory (FreeBSD);
* ltx：shared library text (code and data);
* mxx ：hex memory-mapped type number xx.
* m86：DOS Merge mapped file;
* mem：memory-mapped file;
* mmap：memory-mapped device;
* pd：parent directory;
* rtd：root directory;
* tr：kernel trace file (OpenBSD);
* v86  VP/ix mapped file;
* 0：表示标准输出
* 1：表示标准输入
* 2：表示标准错误

一般在标准输出、标准错误、标准输入后还跟着文件状态模式：

* u：表示该文件被打开并处于读取/写入模式。
* r：表示该文件被打开并处于只读模式。
* w：表示该文件被打开并处于。
* 空格：表示该文件的状态模式为unknow，且没有锁定。
* -：表示该文件的状态模式为unknow，且被锁定。

同时在文件状态模式后面，还跟着相关的锁：

* N：for a Solaris NFS lock of unknown type;
* r：for read lock on part of the file;
* R：for a read lock on the entire file;
* w：for a write lock on part of the file;（文件的部分写锁）
* W：for a write lock on the entire file;（整个文件的写锁）
* u：for a read and write lock of any length;
* U：for a lock of unknown type;
* x：for an SCO OpenServer Xenix lock on part      of the file;
* X：for an SCO OpenServer Xenix lock on the      entire file;
* space：if there is no lock.

文件类型：

* DIR：表示目录。
* CHR：表示字符类型。
* BLK：块设备类型。
* UNIX： UNIX 域套接字。
* FIFO：先进先出 (FIFO) 队列。
* IPv4：网际协议 (IP) 套接字。
* DEVICE：指定磁盘的名称
* SIZE：文件的大小
* NODE：索引节点（文件在磁盘上的标识）
* NAME：打开文件的确切名称

## 实例

```bash
lsof -i     # 列出所有的网络连接或端口
lsof ~      # 查看打开用户目录的进程
```
