# **iperf**

## 说明

iperf可以测试TCP和UDP带宽质量。iperf可以测量最大TCP带宽，具有多种参数和UDP特性。iperf可以报告带宽，延迟抖动和数据包丢失
利用iperf这一特性，可以用来测试一些网络设备如路由器，防火墙，交换机等的性能

* [iperf3 github](https://github.com/esnet/iperf)
* [perfsonar文档](http://docs.perfsonar.net)
* [public iperf3 server地址](https://iperf.fr)
* [internet2](http://software.internet2.edu)

## 各安装包区别

![figure](http://docs.perfsonar.net/_images/install_options-bundle_tree.png)

```bash
# 通过perfSONAR安装,最好设置tcp拥塞算法为net.ipv4.tcp_congestion_control = htcp
yum install -y http://software.internet2.edu/rpms/el7/x86_64/latest/packages/perfSONAR-repo-0.9-1.noarch.rpm
yum install -y perfsonar-tools  # 仅包含运行按需测量所需的命令行客户端，owamp twamp nuttcp iperf3 iperf

: << comment
包括perfsonar-tools包中的所有内容以及以下所需的软件：
* 定期自动运行测试
* 参与集中管理的测试
* 发布测量节点的存在
comment
yum install -y perfsonar-testpoint

: << comment
perfsonar-core bundle install包括perfsonar-testpoint bundle install中的所有内容以及用于存储结果的esmond测量存档。这对于希望在
本地存储结果但不希望安装perfSONAR Toolkit的专用测量主机来说非常理想。换句话说，他们不想使用Web界面，并希望灵活地选择默认安全性和调整设置
comment
yum install -y perfsonar-core

: << comment
包含perfsonar-core bundle中的所有内容：
用于管理测试的Web界面
脚本用于应用系统范围的默认调整和安全设置
此捆绑包适用于那些希望安装perfSONAR Toolkit ISO中包含的全套工具但在现有Linux系统上的工具包
comment
yum install -y perfsonar-toolkit

: << comment
perfsonar-centralmanagement捆绑包独立于上面的捆绑包，并安装集中管理大量主机并显示其结果所需的工具。这包括esmond测量存档，用于发布
任务模板的工具和用于显示结果的仪表板软件(MaDDash)
comment
yum install -y perfsonar-centralmanagement
```

## 网络吞吐量工具比较

* [iperf2](https://sourceforge.net/projects/iperf2/)
* [iperf3](https://software.es.net/iperf)
* [nuttcp](http://nuttcp.net/)

建议使用iperf3，而不要使用较早版本的iperf2，因为TCP重传和CWND报告对于故障排除非常有用。iperf2.0.8及更高版本现在通过'-e'标志支持此功能

注意：三个工具都在开发阶段，此处有可能随着时间推移有所变动未及时修改

|  |  | 工具特征比较 |  |  |
| :------: | :------: | :------: | :------: | :------: |
| 版本 | iperf2.0.5 | iperf2.0.8 + | iperf3.1.5 + | nuttcp 8.x |
| 多线程 | -P | -P |  |  |
| JSON输出 |  |  | --json |  |
| CSV输出 | -y | -y |  |  |
| FQ-based pacing |  |  | --fq-rate |  |
| 多播支持 | --ttl | --ttl |  | -m |
| 双向测试 | --dualtest | --dualtest |  |  |
| 转发和CWND报告 |  | -e | 默认开启 | -br/-bc  |
| 跳过TCP慢启动 |  |  | --omit |  |
| 设置TCP拥塞控制alg | -Z | -Z | --congestion |  |
| 零拷贝(sendfile) |  |  | --zerocopy |  |
| UDP burst模式 |  |  |  | -Ri#/# |
| MS Windows支持 | 是 | 是 | 没有 | 没有 |

### 用途建议如下

* 将iperf2用于并行流，双向或基于MS Windows的测试
* 使用nuttcp进行高速UDP测试
* 否则使用iperf3。特别是如果你想要详细的JSON输出

### iperf2和iperf3常见问题

```markdown
# iperf2
对于800Mbps以上的UDP，iperf 2.0.5结果不一致。此问题已在iperf2.0.8中修复。此版本包括新的“ -e”选项，以输出TCP重传和CWND信息

# iperf3
iperf3是单线程的，而iperf2是多线程的。建议将iperf2用于并行流，将iperf3用于并行流参考：
https://fasterdata.es.net/performance-testing/network-troubleshooting-tools/iperf/multi-stream-iperf3/

UDP速率低于100Kbps时，需要减少默认数据包长度，使用-l100选项
使用-fq-rate选项时，需要内核配置修改net.core.default_qdisc = fq

```

## iperf选项

```markdown
客户端与服务器共用选项
-f, --format [bkmaBKMA]	格式化带宽数输出。支持的格式有： 'b' = bits/sec 'B' = Bytes/sec 'k' = Kbits/sec 'K' = KBytes/sec 'm' = Mbits/sec 'M' = MBytes/sec 'g' = Gbits/sec 'G' = GBytes/sec 'a' = adaptive bits/sec 'A' = adaptive Bytes/sec 自适应格式是kilo-和mega-二者之一。除了带宽之外的字段都输出为字节，除非指定输出的格式，默认的参数是a。 注意：在计算字节byte时，Kilo = 1024， Mega = 1024^2，Giga = 1024^3。通常，在网络中，Kilo = 1000， Mega = 1000^2， and Giga = 1000^3，所以，Iperf也按此来计算比特（位）。如果这些困扰了你，那么请使用-f b参数，然后亲自计算一下
-i, --interval #	设置每次报告之间的时间间隔，单位为秒。如果设置为非零值，就会按照此时间间隔输出测试报告。默认值为零
-l, --len #[KM]	设置读写缓冲区的长度。TCP方式默认为8KB，UDP方式默认为1470字节
-m, --print_mss	输出TCP MSS值（通过TCP_MAXSEG支持）。MSS值一般比MTU值小40字节。通常情况
-p, --port #	设置端口，与服务器端的监听端口一致。默认是5001端口，与ttcp的一样
-u, --udp	使用UDP方式而不是TCP方式。参看-b选项
-w, --window #[KM]	设置套接字缓冲区为指定大小。对于TCP方式，此设置为TCP窗口大小。对于UDP方式，此设置为接受UDP数据包的缓冲区大小，限制可以接受数据包的最大值
-B, --bind host	绑定到主机的多个地址中的一个。对于客户端来说，这个参数设置了出栈接口。对于服务器端来说，这个参数设置入栈接口。这个参数只用于具有多网络接口的主机。在Iperf的UDP模式下，此参数用于绑定和加入一个多播组。使用范围在224.0.0.0至239.255.255.255的多播地址。参考-T参数
-C, --compatibility	与低版本的Iperf使用时，可以使用兼容模式。不需要两端同时使用兼容模式，但是强烈推荐两端同时使用兼容模式。某些情况下，使用某些数据流可以引起1.7版本的服务器端崩溃或引起非预期的连接尝试
-M, --mss #ip头减去40字节。在以太网中，MSS值 为1460字节（MTU1500字节）。许多操作系统不支持此选项
-N, --nodelay	设置TCP无延迟选项，禁用Nagle's运算法则。通常情况此选项对于交互程序，例如telnet，是禁用的
-V (from v1.6 or higher)	绑定一个IPv6地址。 服务端：$ iperf -s –V 客户端：$ iperf -c -V 注意：在1.6.3或更高版本中，指定IPv6地址不需要使用-B参数绑定，在1.6之前的版本则需要。在大多数操作系统中，将响应IPv4客户端映射的IPv4地址
服务器端专用选项
-s, --server	Iperf服务器模式
-D (v1.2或更高版本)	Unix平台下Iperf作为后台守护进程运行。在Win32平台下，Iperf将作为服务运行
-R(v1.2或更高版本，仅用于Windows)	卸载Iperf服务（如果它在运行）
-o(v1.2或更高版本，仅用于Windows)	重定向输出到指定文件
-c, --client host	如果Iperf运行在服务器模式，并且用-c参数指定一个主机，那么Iperf将只接受指定主机的连接。此参数不能工作于UDP模式
-P, --parallel #	服务器关闭之前保持的连接数。默认是0，这意味着永远接受连接
客户端专用选项
-b, --bandwidth #[KM]	UDP模式使用的带宽，单位bits/sec。此选项与-u选项相关。默认值是1 Mbit/sec
-c, --client host	运行Iperf的客户端模式，连接到指定的Iperf服务器端
-d, --dualtest	运行双测试模式。这将使服务器端反向连接到客户端，使用-L 参数中指定的端口（或默认使用客户端连接到服务器端的端口）。这些在操作的同时就立即完成了。如果你想要一个交互的测试，请尝试-r参数
-n, --num #[KM]	传送的缓冲器数量。通常情况，Iperf按照10秒钟发送数据。-n参数跨越此限制，按照指定次数发送指定长度的数据，而不论该操作耗费多少时间。参考-l与-t选项
-r, --tradeoff	往复测试模式。当客户端到服务器端的测试结束时，服务器端通过-l选项指定的端口（或默认为客户端连接到服务器端的端口），反向连接至客户端。当客户端连接终止时，反向连接随即开始。如果需要同时进行双向测试，请尝试-d参数
-t, --time #	设置传输的总时间。Iperf在指定的时间内，重复的发送指定长度的数据包。默认是10秒钟。参考-l与-n选项
-L, --listenport #	指定服务端反向连接到客户端时使用的端口。默认使用客户端连接至服务端的端口
-P, --parallel #	线程数。指定客户端与服务端之间使用的线程数。默认是1线程。需要客户端与服务器端同时使用此参数
-S, --tos #	出栈数据包的服务类型。许多路由器忽略TOS字段。你可以指定这个值，使用以"0x"开始的16进制数，或以"0"开始的8进制数或10进制数。 例如，16进制'0x10' = 8进制'020' = 十进制'16'。TOS值1349就是： IPTOS_LOWDELAY minimize delay 0x10 IPTOS_THROUGHPUT maximize throughput 0x08 IPTOS_RELIABILITY maximize reliability 0x04 IPTOS_LOWCOST minimize cost 0x02
-T, --ttl #	出栈多播数据包的TTL值。这本质上就是数据通过路由器的跳数。默认是1，链接本地
-F (from v1.2 or higher)	使用特定的数据流测量带宽，例如指定的文件。 $ iperf -c -F
-I (from v1.2 or higher)	与-F一样，由标准输入输出文件输入数据
```

## iperf3选项

```markdown

```

## iperf和iperf3基本命令对比

|  |  |
| :------: | :------: |
| 服务器端 |  |
| iperf -s / iperf3 -s | 在默认端口上启动服务器 |
| iperf -s -w 32M -D / iperf3 -s -D | 使用较大的TCP窗口并以守护程序模式启动服务器 |
| iperf -i1 -u -s -p 5003 / iperf3 -s -p 5003 | 在端口5003上启动UDP服务器，并给出1秒的间隔报告。<br>请注意，对于iperf3，-u选项从客户端传递到服务器 |
| 客户端 |  |
| iperf/iperf3 -c remotehost -i 1 -t 30 | 运行30秒测试，每1秒给出一次结果 |
| iperf/iperf3 -c remotehost -i 1 -t 20 -r | 从remotehost到localhost运行测试 |
| iperf/iperf3 -c remotehost -i 1 -t 20 -w 32M -P 4 | 使用4个并行流和32M TCP缓冲区运行测试 |
| iperf/iperf3 -c remotehost -u -i 1 -b 200M | 运行200 Mbps UDP测试 |

iperf3添加了许多其他功能。例如：-i模式现在报告TCP重传信息（默认情况下处于启用状态），而详细模式提供了大量有关CPU使用率的有用信息等
新选项包括如下：

|  |  |
| :------: | :------: |
| 客户端 | 新iperf3选项命令 |
| iperf3 -c remotehost -i.5 -0 2 | 收集结果之前，请运行测试2秒钟，以完成TCP慢启动。（省略模式） |
| iperf3 -Z -c remotehost | 将sendfile（）系统调用用于“零复制”模式。这会在较旧的硬件上使用更少的CPU |
| iperf3 -c 192.168.12.12 -T s1 & iperf3 -c 192.168.12.13 -T s2 | 一次对多个接口运行测试，并标记行以指示哪个测试是哪个 |
| iperf3 -c remotehost -J | 以JSON格式输出结果，以便于分析 |
| iperf3 -A 4,4 -c remotehost | 设置发送方和接收方的CPU关联性(核心从0开始编号)，<br>这与在客户端和服务器上执行“numactl -C 4 iperf3”具有相同的影响 |
| iperf3 -c 10.20.1.20 -A2,2 -T "1" & ; iperf3 -c 10.20.1.20 -p 5400 -A3,3 -T "2" & | 在2个不同的内核上运行2个流，<br>并使用“ -T”标志标记每个流 |

iperf3通常用于衡量内存对内存的性能，但是您也可以使用最新版iperf3的-F选项来确定网络或磁盘是否是瓶颈

```bash
iperf3 -s   # server端执行此命令
iperf3 -c testhost -i1  # 测试内存到内存(客户端)[传输带宽测试]

iperf3 -s   # server端执行此命令
iperf3 -c testhost -i1 -F filename   # 磁盘到内存(客户端)[磁盘读取测试，当吞吐量比上门测试慢时说明受磁盘限制而不是网络瓶颈]

iperf3 -s -F filename  # server端执行此命令
iperf3 -c testhost -i1 -t 40 # 测试内存到磁盘(客户端)[磁盘写入测试，对于磁盘写测试，利用-t选项运行更长的测试来排除网络缓冲问题]

# 最慢的测试结果将显示瓶颈，值得注意的是：第二次运行时，文件已经被缓存，需要以root用户执行以下命令
sync;echo 3> /proc/sys/vm/drop_caches

: << comment
# 在40Gbps及以上的高速主机使用iperf3测试
iperf3 -s -p 5101&; iperf3 -s -p 5102&; iperf3 -s -p 5103 & # 服务端开启多个进程
# 然后运行多个客户端，使用-T选项标记输出
iperf3 -c hostname -T s1 -p 5101 &;  
iperf3 -c hostname -T s2 -p 5102 &; 
iperf3 -c hostname -T s3 -p 5103 &;

# 40或100G主机参考Linux主机调整部分，TCP默认自动调整参数可能不能容纳40G，并且尝试使用-w选项将窗口设置的更大(如128M),必须检查IRQ设置
# 详细参考：https://fasterdata.es.net/host-tuning/linux/100g-tuning/
comment

# iperf3使用--logfile选项时，实时查看文件输出，使用--forceflush标志
```

## nuttcp

```bash
nuttcp -S   # 服务器端执行此命令
nuttcp -i1 server_hostname  # 客户端

nuttcp -i1 -r server_hostname   # 测试相反的方向

# UDP突发模式，从6.2.8开始支持udp的突发模式，对于查找没有足够缓冲的受网络设备约束的路径很有用
nuttcp -u -Ri300m/20 -i 1 -T5 nettest.lbl.gov # 20个数据包的突发发送300 Mbps UDP，持续5秒

nuttcp -l8972 -T30 -u -w4m -Ri300m/100 -i1 server_hostname

```

## 其他网络性能测试工具

```markdown
# Scamper是结合了路由跟踪和MTU发现
https://www.caida.org/tools/measurement/scamper/

# owing是一种检查由于拥塞或不良光纤造成的数据包丢失的简单工具(包含在perfsonar-tools中)
owping -c 10000 -i .01 hostname # 10 ms的间隔发送10000个测试数据包

https://fasterdata.es.net/performance-testing/network-troubleshooting-tools/tcpdump-tcptrace/

```

## 实例

```bash
# 网络性能故障排除参考：https://fasterdata.es.net/performance-testing/troubleshooting/

iperf -u -s # 带宽测试通常采用UDP模式，因为能测出极限带宽、时延抖动、丢包率。在进行测试时，首先以链路理论带宽作为数据发送速率进行测试
# 例如，从客户端到服务器之间的链路的理论带宽为100Mbps，先用`-b 100M`进行测试，然后根据测试结果（包括实际带宽，时延抖动和丢包率），再以
# 实际带宽作为数据发送速率进行测试，会发现时延抖动和丢包率比第一次好很多，重复测试几次，就能得出稳定的实际带宽

iperf -u -c 192.168.1.1 -b 100M -t 60   # udp模式下，以100Mbps数据发送速率，客户端到服务器192.168.1.1上传带宽测试，测试时间60秒
iperf -u -c 192.168.1.1 -b 5M -P 30 -t 60   # 客户端同时向服务器端发起30个连接线程，以5Mbps为数据发送速率
iperf -u -c 192.168.1.1 -b 100M -d -t 60    # 以100M为数据发送速率，进行上下行带宽测试

iperf -c 192.168.1.1 -t 60  # 在tcp模式下，客户端到服务器192.168.1.1上传带宽测试，测试时间为60秒
iperf -c 192.168.1.1 -p 80 -P 30 -t 60   # -P客户端同时向服务器端发起30个连接线程,-p代表端口
iperf -c 192.168.1.1  -d -t 60  # 进行上下行带宽测试
```




