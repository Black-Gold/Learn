# **netstat**

## 说明

**netstat命令** 用来打印Linux中网络系统的状态信息，可让你得知整个Linux系统的网络情况。



```sh
-a或--all：显示所有连线中的Socket；
-A<网络类型>或--<网络类型>：列出该网络类型连线中的相关地址；
-c或--continuous：持续列出网络状态；
-C或--cache：显示路由器配置的快取信息；
-e或--extend：显示网络其他相关信息；
-F或--fib：显示FIB；
-g或--groups：显示多重广播功能群组组员名单；
-h或--help：在线帮助；
-i或--interfaces：显示网络界面信息表单；
-l或--listening：显示监控中的服务器的Socket；
-M或--masquerade：显示伪装的网络连线；
-n或--numeric：直接使用ip地址，而不通过域名服务器；
-N或--netlink或--symbolic：显示网络硬件外围设备的符号连接名称；
-o或--timers：显示计时器；
-p或--programs：显示正在使用Socket的程序识别码和程序名称；
-r或--route：显示Routing Table；
-s或--statistice：显示网络工作信息统计表；
-t或--tcp：显示TCP传输协议的连线状况；
-u或--udp：显示UDP传输协议的连线状况；
-v或--verbose：显示指令执行过程；
-V或--version：显示版本信息；
-w或--raw：显示RAW传输协议的连线状况；
-x或--unix：此参数的效果和指定"-A unix"参数相同；
--ip或--inet：此参数的效果和指定"-A inet"参数相同。

usage: netstat [-vWeenNcCF] [<Af>] -r         netstat {-V|--version|-h|--help}
       netstat [-vWnNcaeol] [<Socket> ...]
       netstat { [-vWeenNac] -I[<Iface>] | [-veenNac] -i | [-cnNe] -M | -s [-6tuw] } [delay]

        -r, --route              display routing table
        -I, --interfaces=<Iface> display interface table for <Iface>
        -i, --interfaces         display interface table
        -g, --groups             display multicast group memberships
        -s, --statistics         display networking statistics (like SNMP)
        -M, --masquerade         display masqueraded connections

        -v, --verbose            be verbose
        -W, --wide               don't truncate IP addresses
        -n, --numeric            don't resolve names
        --numeric-hosts          don't resolve host names
        --numeric-ports          don't resolve port names
        --numeric-users          don't resolve user names
        -N, --symbolic           resolve hardware names
        -e, --extend             display other/more information
        -p, --programs           display PID/Program name for sockets
        -o, --timers             display timers
        -c, --continuous         continuous listing

        -l, --listening          display listening server sockets
        -a, --all                display all sockets (default: connected)
        -F, --fib                display Forwarding Information Base (default)
        -C, --cache              display routing cache instead of FIB
        -Z, --context            display SELinux security context for sockets



```

### 实例

#### 列出所有端口 (包括监听和未监听的)

```sh
netstat -a     #列出所有端口
netstat -at    #列出所有tcp端口
netstat -au    #列出所有udp端口
netstat -ng    #查看组播情况
```

#### 列出所有处于监听状态的 Sockets

```sh
netstat -l        #只显示监听端口
netstat -lt       #只列出所有监听 tcp 端口
netstat -lu       #只列出所有监听 udp 端口
netstat -lx       #只列出所有监听 UNIX 端口
```

#### 显示每个协议的统计信息

```sh
netstat -s   显示所有端口的统计信息
netstat -st   显示TCP端口的统计信息
netstat -su   显示UDP端口的统计信息

```

#### 在netstat输出中显示 PID 和进程名称

```sh
netstat -pt
```

`netstat -p`可以与其它开关一起使用，就可以添加“PID/进程名称”到netstat输出中，这样debugging的时候可以很方便的发现特定端口运行的程序。

#### 在netstat输出中不显示主机，端口和用户名(host, port or user)

当你不想让主机，端口和用户名显示，使用`netstat -n`。将会使用数字代替那些名称。同样可以加速输出，因为不用进行比对查询。

```sh
netstat -an
```

如果只是不想让这三个名称中的一个被显示，使用以下命令:

```sh
netsat -a --numeric-ports
netsat -a --numeric-hosts
netsat -a --numeric-users
```

#### 持续输出netstat信息

```sh
netstat -c   #每隔一秒输出网络信息
```

#### 显示系统不支持的地址族(Address Families)

```sh
netstat --verbose
```

在输出的末尾，会有如下的信息：

```sh
netstat: no support for `AF IPX' on this system.
netstat: no support for `AF AX25' on this system.
netstat: no support for `AF X25' on this system.
netstat: no support for `AF NETROM' on this system.
```

#### 显示核心路由信息

```sh
netstat -r
```

使用`netstat -rn`显示数字格式，不查询主机名称。

#### 找出程序运行的端口

并不是所有的进程都能找到，没有权限的会不显示，使用 root 权限查看所有的信息。

```sh
netstat -ap | grep ssh
```

找出运行在指定端口的进程：

```sh
netstat -an | grep ':80'
```

#### 显示网络接口列表

```sh
netstat -i
```

显示详细信息，像是ifconfig使用`netstat -ie`。

#### IP和TCP分析

查看连接某服务端口最多的的IP地址：

```sh
netstat -ntu | grep :80 | awk '{print $5}' | cut -d: -f1 | awk '{++ip[$1]} END {for(i in ip) print ip[i],"\t",i}' | sort -nr
```

TCP各种状态列表：

```sh
netstat -nt | grep -e 127.0.0.1 -e 0.0.0.0 -e ::: -v | awk '/^tcp/ {++state[$NF]} END {for(i in state) print i,"\t",state[i]}'
```

查看phpcgi进程数，如果接近预设值，说明不够用，需要增加：

```sh
netstat -anpo | grep "php-cgi" | wc -l
```

获取连接数的命令

```sh
netstat -n |awk '/^tcp/ {++S[$NF]} END {for(a in S) print a, S[a]}'

```

| 命令拆分 | 详解 |
| ----- | ---- |
| /^tcp/ | 过滤出以tcp开头的行，“^”为正则表达式用法，以...开头，这里是过滤出以tcp开头的行。 |
| S[] | 定义了一个名叫S的数组，在awk中，数组下标通常从 1 开始，而不是 0。 |
| NF | 当前记录里域个数，默认以空格分隔，如上所示的记录，NF域个数等于6 |
| $NF | 表示一行的最后一个域的值，如上所示的记录，$NF也就是$6，表示第6个字段的值，也就是SYN_RECV或TIME_WAIT等。 |
| S[$NF] | 表示数组元素的值，如上所示的记录，就是S[TIME_WAIT]状态的连接数 |
| ++S[$NF] | 表示把某个数加一，如上所示的记录，就是把S[TIME_WAIT]状态的连接数加一 |
| END | 结束 |
| forkey in S | 遍历S[]数组 |
| print key,”\t”,S[key] | 打印数组的键和值，中间用\t制表符分割，显示好一些。 |

统计服务器当前单IP连接数最大的IP地址前十

```sh
netstat -an|awk-F '[ :]+' '{++S[$6]} END {for (a in S) print a ,S[a]}'|sort -rn -k2

netstat -an|grep EST|awk-F '[ :]+' '{++S[$6]} END {for (key in S) print "ip:"key"----->",S[key]}'|sort -rn -k2
```

tcp连接状态的描述说明(netstat输出)

```sh
Active Internet connections (w/o servers)

Proto Recv-Q Send-Q Local AddressForeign AddressState

Proto

The protocol (tcp, udp, raw) used by the socket.

第一列为socket使用的协议。

Recv-Q

The count of bytes not copied by the user program connected to this socket.

第二列为接到的但是还没处理的字节数。

Send-Q

The count of bytes not acknowledged by the remote host.

第三列为已经发送的但是没有被远程主机确认收到的字节数。

Local Address

Address and port number of the local end of the socket.Unless the --numeric(-n)

optionisspecified,thesocketaddress is resolved to its canonical host name

(FQDN), and the port number is translated into the corresponding service name.

第四列为 本地的地址及端口。

Foreign Address

Address and port number of the remote endofthesocket.Analogousto"Local Address."

第五列为外部的地址及端口。

State

Thestateofthesocket.Sincethere are no states in raw mode and usually no

states used in UDP, this column may be left blank. Normally this can be one of sev-

eral values:

第六列为socket的状态，通常仅仅有tcp的状态，状态值可能有ESTABLISHED，SYN_SENT，SYN_RECV FIN_WAIT1，FIN_WAIT2，TIME_WAIT等，详见下文。其中，最重要的是第六列。

```

netstat第六列State的状态信息

```sh

State

Thestateofthesocket.Sincethere are no states in raw mode and usually no

states used in UDP, this column may be left blank. Normally this can be one of sev-

eral values:

第六列为socket的状态，通常仅仅有tcp的状态，状态值可能有ESTABLISHED，SYN_SENT，SYN_RECV FIN_WAIT1，FIN_WAIT2，TIME_WAIT等，详见下文。其中，最重要的是第六列。

ESTABLISHED

The socket has an established connection.

socket已经建立连接，表示处于连接的状态，一般认为有一个ESTABLISHED认为是一个服务的并发连接。这个连接状态在生产场景很重要，要重点关注。

SYN_SENT

The socket is actively attempting to establish a connection.

socket正在积极尝试建立一个连接，即处于发送后连接前的一个等待但未匹配进入连接的状态。

SYN_RECV

A connection request has been received from the network.

已经从网络上收到一个连接请求。

FIN_WAIT1

The socket is closed, and the connection is shutting down.

socket已关闭，连接正在或正要关闭。

FIN_WAIT2

Connectionisclosed,andthesocket is waiting for a shutdown from the remote end.

连接已关闭，并且socket正在等待远端结束。

TIME_WAIT

The socket is waiting after close to handle packets still in the network.

socket正在等待关闭处理仍在网络上的数据包，这个连接状态在生产场景很重要，要重点关注。

CLOSED The socket is not being used.| socket不在被占用了。

CLOSE_WAIT

The remote end has shutdown, waiting for the socket to close.

远端已经结束，等待socket关闭。

LAST_ACK

The remote end has shut down, and the socket is closed. Waiting for acknowl-edgement.|

远端已经结束，并且socket也已关闭，等待acknowl-edgement。

LISTEN Thesocketislisteningforincoming connections.Such sockets are not

included in the output unless you specify the --listening (-l) or --all (-a)

option.

socket正在监听连接请求。

CLOSING

Both sockets are shut down but we still don’t have all our data sent.

sockets关闭，但是我们仍旧没有发送数据。

UNKNOWN

The state of the socket is unknown

未知的状态。

```
