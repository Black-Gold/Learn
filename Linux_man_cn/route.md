# route

## 说明

**route命令** 用来显示并设置Linux内核中的网络路由表，route命令设置的路由主要是静态路由。要实现两个不同的子网之间的通信，需要一台连接
两个网络的路由器，或者同时位于两个网络的网关来实现

在Linux系统中设置路由通常是为了解决以下问题：该Linux系统在一个局域网中，局域网中有一个网关，能够让机器访问Internet，那么就需要将这台
机器的ip地址设置为Linux机器的默认路由。要注意的是，直接在命令行下执行route命令来添加路由，不会永久保存，当网卡重启或者机器重启之后，该
路由就失效了；可以在`/etc/rc.local`中添加route命令来保证该路由设置永久有效

## 选项

```markdown
-v, --verbose            be verbose
-n, --numeric            不执行DNS反向查找，直接显示数字形式的IP地址
-e, --extend             display other/more information
-F, --fib                display Forwarding Information Base (default)
-C, --cache              display routing cache instead of FIB

Add     增加指定的路由记录
Del     删除指定的路由记录
Target  目的网络或目的主机
gw      设置默认网关
mss     设置TCP的最大区块长度（MSS），单位MB
window  指定通过路由表的TCP连接的TCP窗口大小
dev     路由记录所表示的网络接口
```

## 实例

输出详解：其中Flags为路由标志，标记当前网络节点的状态，Flags标志说明：

*   U Up表示此路由当前为启动状态
*   H Host，表示此网关为一主机
*   G Gateway，表示此网关为一路由器
*   R Reinstate Route，使用动态路由重新初始化的路由
*   D Dynamically,此路由是动态性地写入
*   M Modified，此路由是由路由守护程序或导向器动态修改
*   ! 表示此路由当前为关闭状态

```bash
route   # 显示当前路由
route -n
route add -net 224.0.0.0 netmask 240.0.0.0 dev eth0     # 添加网关/设置网关,增加一条到达244.0.0.0的路由
route add -net 224.0.0.0 netmask 240.0.0.0 reject       # 屏蔽一条路由,增加一条屏蔽的路由，目的地址为224.x.x.x将被拒绝

# 删除路由记录
route del -net 224.0.0.0 netmask 240.0.0.0
route del -net 224.0.0.0 netmask 240.0.0.0 reject

# 删除和添加设置默认网关
route del default gw 192.168.120.240
route add default gw 192.168.120.240
```


