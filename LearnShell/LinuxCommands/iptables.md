iptables
===

Linux上常用的防火墙软件

## 补充说明

**iptables命令** 是Linux上常用的防火墙软件，是netfilter项目的一部分。可以直接配置，也可以通过许多前端和图形界面配置。

<!-- TOC -->

- [补充说明](#补充说明)
  - [语法](#语法)
  - [选项](#选项)
    - [命令选项输入顺序](#命令选项输入顺序)
    - [工作机制](#工作机制)
    - [防火墙的策略](#防火墙的策略)
    - [防火墙的策略](#防火墙的策略-1)
  - [实例](#实例)
    - [列出已设置的规则](#列出已设置的规则)
    - [清除已有规则](#清除已有规则)
    - [删除已添加的规则](#删除已添加的规则)
    - [开放指定的端口](#开放指定的端口)
    - [屏蔽IP](#屏蔽ip)
    - [指定数据包出去的网络接口](#指定数据包出去的网络接口)
    - [查看已添加的规则](#查看已添加的规则)
    - [启动网络转发规则](#启动网络转发规则)
    - [端口映射](#端口映射)
    - [字符串匹配](#字符串匹配)
    - [阻止Windows蠕虫的攻击](#阻止windows蠕虫的攻击)
    - [防止SYN洪水攻击](#防止syn洪水攻击)

Usage: iptables -[ACD] chain rule-specification [options]
       iptables -I chain [rulenum] rule-specification [options]
       iptables -R chain rulenum rule-specification [options]
       iptables -D chain rulenum [options]
       iptables -[LS] [chain [rulenum]] [options]
       iptables -[FZ] [chain] [options]
       iptables -[NX] chain
       iptables -E old-chain-name new-chain-name
       iptables -P chain target [options]
       iptables -h (print this help information)

Commands:
Either long or short options are allowed.
  --append  -A chain            Append to chain
  --check   -C chain            Check for the existence of a rule
  --delete  -D chain            Delete matching rule from chain
  --delete  -D chain rulenum
                                Delete rule rulenum (1 = first) from chain
  --insert  -I chain [rulenum]
                                Insert in chain as rulenum (default 1=first)
  --replace -R chain rulenum
                                Replace rule rulenum (1 = first) in chain
  --list    -L [chain [rulenum]]
                                List the rules in a chain or all chains
  --list-rules -S [chain [rulenum]]
                                Print the rules in a chain or all chains
  --flush   -F [chain]          Delete all rules in  chain or all chains
  --zero    -Z [chain [rulenum]]
                                Zero counters in chain or all chains
  --new     -N chain            Create a new user-defined chain
  --delete-chain
            -X [chain]          Delete a user-defined chain
  --policy  -P chain target
                                Change policy on chain to target
  --rename-chain
            -E old-chain new-chain
                                Change chain name, (moving any references)
Options:
    --ipv4      -4              Nothing (line is ignored by ip6tables-restore)
    --ipv6      -6              Error (line is ignored by iptables-restore)
[!] --protocol  -p proto        protocol: by number or name, eg. `tcp'
[!] --source    -s address[/mask][...]
                                source specification
[!] --destination -d address[/mask][...]
                                destination specification
[!] --in-interface -i input name[+]
                                network interface name ([+] for wildcard)
 --jump -j target
                                target for rule (may load target extension)
  --goto      -g chain
                              jump to chain with no return
  --match       -m match
                                extended match (may load extension)
  --numeric     -n              numeric output of addresses and ports
[!] --out-interface -o output name[+]
                                network interface name ([+] for wildcard)
  --table       -t table        table to manipulate (default: `filter')
  --verbose     -v              verbose mode
  --wait        -w [seconds]    maximum wait to acquire xtables lock before give up
  --wait-interval -W [usecs]    wait time to try to acquire xtables lock
                                default is 1 second
  --line-numbers                print line numbers when listing
  --exact       -x              expand numbers (display exact values)
[!] --fragment  -f              match second or further fragments only
  --modprobe=<command>          try to insert modules using this command
  --set-counters PKTS BYTES     set the counter during insert/append
[!] --version   -V              print package version.


<!-- /TOC -->

### 语法  

```
iptables(选项)(参数)
```

### 选项  

```bash
-t, --table table 对指定的表 table 进行操作， table 必须是 raw， nat，filter，mangle 中的一个。如果不指定此选项，默认的是 filter 表。

# 通用匹配：源地址目标地址的匹配
-p：指定要匹配的数据包协议类型；
-s, --source [!] address[/mask] ：把指定的一个／一组地址作为源地址，按此规则进行过滤。当后面没有 mask 时，address 是一个地址，比如：192.168.1.1；当 mask 指定时，可以表示一组范围内的地址，比如：192.168.1.0/255.255.255.0。
-d, --destination [!] address[/mask] ：地址格式同上，但这里是指定地址为目的地址，按此进行过滤。
-i, --in-interface [!] <网络接口name> ：指定数据包的来自来自网络接口，比如最常见的 eth0 。注意：它只对 INPUT，FORWARD，PREROUTING 这三个链起作用。如果没有指定此选项， 说明可以来自任何一个网络接口。同前面类似，"!" 表示取反。
-o, --out-interface [!] <网络接口name> ：指定数据包出去的网络接口。只对 OUTPUT，FORWARD，POSTROUTING 三个链起作用。

# 查看管理命令
-L, --list [chain] 列出链 chain 上面的所有规则，如果没有指定链，列出表上所有链的所有规则。

# 规则管理命令
-A, --append chain rule-specification 在指定链 chain 的末尾插入指定的规则，也就是说，这条规则会被放到最后，最后才会被执行。规则是由后面的匹配来指定。
-I, --insert chain [rulenum] rule-specification 在链 chain 中的指定位置插入一条或多条规则。如果指定的规则号是1，则在链的头部插入。这也是默认的情况，如果没有指定规则号。
-D, --delete chain rule-specification -D, --delete chain rulenum 在指定的链 chain 中删除一个或多个指定规则。
-R num：Replays替换/修改第几条规则

# 链管理命令（这都是立即生效的）
-P, --policy chain target ：为指定的链 chain 设置策略 target。注意，只有内置的链才允许有策略，用户自定义的是不允许的。
-F, --flush [chain] 清空指定链 chain 上面的所有规则。如果没有指定链，清空该表上所有链的所有规则。
-N, --new-chain chain 用指定的名字创建一个新的链。
-X, --delete-chain [chain] ：删除指定的链，这个链必须没有被其它任何规则引用，而且这条上必须没有任何规则。如果没有指定链名，则会删除该表中所有非内置的链。
-E, --rename-chain old-chain new-chain ：用指定的新名字去重命名指定的链。这并不会对链内部照成任何影响。
-Z, --zero [chain] ：把指定链，或者表中的所有链上的所有计数器清零。

-j, --jump target <指定目标> ：即满足某条件时该执行什么样的动作。target 可以是内置的目标，比如 ACCEPT，也可以是用户自定义的链。
-h：显示帮助信息；
```

#### 命令选项输入顺序

```
iptables -t 表名 <-A/I/D/R> 规则链名 [规则号] <-i/o 网卡名> -p 协议名 <-s 源IP/源子网> --sport 源端口 <-d 目标IP/目标子网> --dport 目标端口 -j 动作
```

#### 工作机制

规则链名包括(也被称为五个钩子函数（hook functions）)：

- **INPUT链** ：处理输入数据包。
- **OUTPUT链** ：处理输出数据包。
- **PORWARD链** ：处理转发数据包。
- **PREROUTING链** ：用于目标地址转换（DNAT）。
- **POSTOUTING链** ：用于源地址转换（SNAT）。

#### 防火墙的策略

防火墙策略一般分为两种，一种叫`通`策略，一种叫`堵`策略，通策略，默认门是关着的，必须要定义谁能进。堵策略则是，大门是洞开的，但是你必须有身份认证，否则不能进。所以我们要定义，让进来的进来，让出去的出去，`所以通，是要全通，而堵，则是要选择`。当我们定义的策略的时候，要分别定义多条功能，其中：定义数据包中允许或者不允许的策略，filter过滤的功能，而定义地址转换的功能的则是nat选项。为了让这些功能交替工作，我们制定出了“表”这个定义，来定义、区分各种不同的工作功能和处理方式。

防火墙规则表：

1. filter表：(主要对数据包进行过滤) 定义允许或者不允许的，只能做在3个链上：INPUT ，FORWARD ，OUTPUT
2. nat表：(主要用于修改数据包的IP地址、端口号等) 定义地址转换的，也只能做在3个链上：PREROUTING ，OUTPUT ，POSTROUTING
3.mangle表：
修改报文原数据，是5个链都可以做：PREROUTING，INPUT，FORWARD，OUTPUT，POSTROUTING

我们修改报文原数据就是来修改TTL的。能够实现将数据包的元数据拆开，在里面做标记/修改内容的。而防火墙标记，其实就是靠mangle来实现的。
4.Raw表：(主要用于决定数据包是否被状态跟踪机制处理，在匹配raw表时优先于其他表)

小扩展:

- 对于filter来讲一般只能做在3个链上：INPUT ，FORWARD ，OUTPUT
- 对于nat来讲一般也只能做在3个链上：PREROUTING ，OUTPUT ，POSTROUTING
- 而mangle则是5个链都可以做：PREROUTING，INPUT，FORWARD，OUTPUT，POSTROUTING
 
iptables/netfilter（这款软件）是工作在用户空间的，它可以让规则进行生效的，本身不是一种服务，而且规则是立即生效的。而我们iptables现在被做成了一个服务，可以进行启动，停止的。启动，则将规则直接生效，停止，则将规则撤销。 

iptables还支持自己定义链。但是自己定义的链，必须是跟某种特定的链关联起来的。在一个关卡设定，指定当有数据的时候专门去找某个特定的链来处理，当那个链处理完之后，再返回。接着在特定的链中继续检查。

注意：规则的次序非常关键，`谁的规则越严格，应该放的越靠前`，而检查规则的时候，是按照从上往下的方式进行检查的。

#### 防火墙的策略

防火墙策略一般分为两种，一种叫`通`策略，一种叫`堵`策略，通策略，默认门是关着的，必须要定义谁能进。堵策略则是，大门是洞开的，但是你必须有身份认证，否则不能进，`所以通，是要全通，而堵，则是要选择`。

表名包括：

- **raw** ：高级功能，如：网址过滤。
- **mangle** ：数据包修改（QOS），用于实现服务质量。
- **net** ：地址转换，用于网关路由器。
- **filter** ：包过滤，用于防火墙规则。

动作包括：

- **ACCEPT** ：接收数据包。
- **DROP** ：丢弃数据包。
- **REDIRECT** ：重定向、映射、透明代理。
- **SNAT** ：源地址转换。
- **DNAT** ：目标地址转换。
- **MASQUERADE** ：IP伪装（NAT），用于ADSL。
- **LOG** ：日志记录。

```bash
                             ┏╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍┓                         
 ┌───────────────┐           ┃    Network    ┃                         
 │ table: filter │           ┗━━━━━━━┳━━━━━━━┛                         
 │ chain: INPUT  │◀────┐             │                                 
 └───────┬───────┘     │             ▼                                 
         │             │   ┌───────────────────┐                       
  ┌      ▼      ┐      │   │ table: nat        │                       
  │local process│      │   │ chain: PREROUTING │                       
  └             ┘      │   └─────────┬─────────┘                       
         │             │             │                                 
         ▼             │             ▼              ┌─────────────────┐
┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅    │     ┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅      │table: nat       │
 Routing decision      └───── outing decision ─────▶│chain: PREROUTING│
┅┅┅┅┅┅┅┅┅┳┅┅┅┅┅┅┅┅┅          ┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅      └────────┬────────┘
         │                                                   │         
         ▼                                                   │         
 ┌───────────────┐                                           │         
 │ table: nat    │           ┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅┅               │         
 │ chain: OUTPUT │    ┌─────▶ outing decision ◀──────────────┘         
 └───────┬───────┘    │      ┅┅┅┅┅┅┅┅┳┅┅┅┅┅┅┅┅                         
         │            │              │                                 
         ▼            │              ▼                                 
 ┌───────────────┐    │   ┌────────────────────┐                       
 │ table: filter │    │   │ chain: POSTROUTING │                       
 │ chain: OUTPUT ├────┘   └──────────┬─────────┘                       
 └───────────────┘                   │                                 
                                     ▼                                 
                             ┏╍╍╍╍╍╍╍╍╍╍╍╍╍╍╍┓                         
                             ┃    Network    ┃                         
                             ┗━━━━━━━━━━━━━━━┛                         
```


### 实例  

#### 列出已设置的规则

> iptables -L [-t 表名] [链名]

- 四个表名 `raw`，`nat`，`filter`，`mangle`
- 五个规则链名 `INPUT`、`OUTPUT`、`FORWARD`、`PREROUTING`、`POSTROUTING`
- filter表包含`INPUT`、`OUTPUT`、`FORWARD`三个规则链

```bash
iptables -L -t nat                  # 列出 nat 上面的所有规则
#            ^ -t 参数指定，必须是 raw， nat，filter，mangle 中的一个
iptables -L -t nat  --line-numbers  # 规则带编号
iptables -L INPUT

iptables -L -nv  # 查看，这个列表看起来更详细
```

#### 清除已有规则

```bash
iptables -F INPUT  # 清空指定链 INPUT 上面的所有规则
iptables -X INPUT  # 删除指定的链，这个链必须没有被其它任何规则引用，而且这条上必须没有任何规则。
                   # 如果没有指定链名，则会删除该表中所有非内置的链。
iptables -Z INPUT  # 把指定链，或者表中的所有链上的所有计数器清零。
```

#### 删除已添加的规则

```bash
# 添加一条规则
iptables -A INPUT -s 192.168.1.5 -j DROP
```

将所有iptables以序号标记显示，执行：

```
iptables -L -n --line-numbers
```

比如要删除INPUT里序号为8的规则，执行：

```bash
iptables -D INPUT 8
```

#### 开放指定的端口

```
iptables -A INPUT -s 127.0.0.1 -d 127.0.0.1 -j ACCEPT               #允许本地回环接口(即运行本机访问本机)
iptables -A INPUT -m state --state ESTABLISHED,RELATED -j ACCEPT    #允许已建立的或相关连的通行
iptables -A OUTPUT -j ACCEPT         #允许所有本机向外的访问
iptables -A INPUT -p tcp --dport 22 -j ACCEPT    #允许访问22端口
iptables -A INPUT -p tcp --dport 80 -j ACCEPT    #允许访问80端口
iptables -A INPUT -p tcp --dport 21 -j ACCEPT    #允许ftp服务的21端口
iptables -A INPUT -p tcp --dport 20 -j ACCEPT    #允许FTP服务的20端口
iptables -A INPUT -j reject       #禁止其他未允许的规则访问
iptables -A FORWARD -j REJECT     #禁止其他未允许的规则访问
```

#### 屏蔽IP

```
iptables -A INPUT -p tcp -m tcp -s 192.168.0.8 -j DROP  # 屏蔽恶意主机（比如，192.168.0.8
iptables -I INPUT -s 123.45.6.7 -j DROP       #屏蔽单个IP的命令
iptables -I INPUT -s 123.0.0.0/8 -j DROP      #封整个段即从123.0.0.1到123.255.255.254的命令
iptables -I INPUT -s 124.45.0.0/16 -j DROP    #封IP段即从123.45.0.1到123.45.255.254的命令
iptables -I INPUT -s 123.45.6.0/24 -j DROP    #封IP段即从123.45.6.1到123.45.6.254的命令是
```

#### 指定数据包出去的网络接口

只对 OUTPUT，FORWARD，POSTROUTING 三个链起作用。

```bash
iptables -A FORWARD -o eth0
```

#### 查看已添加的规则

```
iptables -L -n -v
Chain INPUT (policy DROP 48106 packets, 2690K bytes)
 pkts bytes target     prot opt in     out     source               destination         
 5075  589K ACCEPT     all  --  lo     *       0.0.0.0/0            0.0.0.0/0           
 191K   90M ACCEPT     tcp  --  *      *       0.0.0.0/0            0.0.0.0/0           tcp dpt:22
1499K  133M ACCEPT     tcp  --  *      *       0.0.0.0/0            0.0.0.0/0           tcp dpt:80
4364K 6351M ACCEPT     all  --  *      *       0.0.0.0/0            0.0.0.0/0           state RELATED,ESTABLISHED
 6256  327K ACCEPT     icmp --  *      *       0.0.0.0/0            0.0.0.0/0           

Chain FORWARD (policy ACCEPT 0 packets, 0 bytes)
 pkts bytes target     prot opt in     out     source               destination         

Chain OUTPUT (policy ACCEPT 3382K packets, 1819M bytes)
 pkts bytes target     prot opt in     out     source               destination         
 5075  589K ACCEPT     all  --  *      lo      0.0.0.0/0            0.0.0.0/0  
```

#### 启动网络转发规则

公网`210.14.67.7`让内网`192.168.188.0/24`上网

```bash
iptables -t nat -A POSTROUTING -s 192.168.188.0/24 -j SNAT --to-source 210.14.67.127
```

#### 端口映射

本机的 2222 端口映射到内网 虚拟机的22 端口

```bash
iptables -t nat -A PREROUTING -d 210.14.67.127 -p tcp --dport 2222  -j DNAT --to-dest 192.168.188.115:22
```

#### 字符串匹配

比如，我们要过滤所有TCP连接中的字符串`test`，一旦出现它我们就终止这个连接，我们可以这么做：

```bash
iptables -A INPUT -p tcp -m string --algo kmp --string "test" -j REJECT --reject-with tcp-reset
iptables -L

# Chain INPUT (policy ACCEPT)
# target     prot opt source               destination        
# REJECT     tcp  --  anywhere             anywhere            STRING match "test" ALGO name kmp TO 65535 reject-with tcp-reset
#  
# Chain FORWARD (policy ACCEPT)
# target     prot opt source               destination        
#  
# Chain OUTPUT (policy ACCEPT)
# target     prot opt source               destination  
```

#### 阻止Windows蠕虫的攻击

```bash
iptables -I INPUT -j DROP -p tcp -s 0.0.0.0/0 -m string --algo kmp --string "cmd.exe"
```

#### 防止SYN洪水攻击

```bash
iptables -A INPUT -p tcp --syn -m limit --limit 5/second -j ACCEPT
```

```sh
iptables实现内外网隔离
#!/bin/bash

#赋值IPTABLES：
IPT="/sbin/iptables"

#赋值外网IP:
FW_INET= 202.96.???.???

#赋值内网网卡和外网网卡，及vpn网卡
IF_INET="eth0"
IF_LOCAL="eth1"
IF_OVPN="tun+"

#赋值内部vlan:
LAN_1="192.168.1.0/24"
LAN_2="192.168.2.0/24"
LAN_3="192.168.3.0/24"

#赋值总部与分公司的VPN 外网IP.
OVPN_HEADER="202.96.???.???" 本机防火墙外部IP
OVPN_SUBCOMPANY="202:128.???.???"  子公司防火墙外部IP

#赋值服务器IP
DNS/DHCP=192.168.1.???
EMAIL_LOCAL= 192.168.1.???
DOMAIN_SERVER=192.168.1.???
ANTIVIRUS_SERVER=192.168.1.???
FILE_SERVER=192.168.1.???
DATABASE_SERVER=192.168.1.???

#赋值VLAN网段可出外网
INTERNET1_FULL_ACCESS_1="192.168.1.100-192.168.1.160"
INTERNET2_FULL_ACCESS_2="192.168.2.50-192.168.2.70"
INTERNET3_FULL_ACCESS_3="192.168.3.40-192.168.3.99"
USERS_FULL_ACCESS=
SKYPE_USERS=" 192.168.1.200 192.168.2.200 192.168.3.200"
BLOCKED_HOSTS=""

#装载IPTABLES模块
modprobe nf_nat_ftp

#清空所有的防火墙设置
$IPT -F INPUT
$IPT -F FORWARD
$IPT -F FORWARD -t mangle
$IPT -F OUTPUT
$IPT -t nat -F OUTPUT
$IPT -t nat -F POSTROUTING
$IPT -t nat -F PREROUTING

#设置默认拒绝所有输入和转发数据包
$IPT -P INPUT DROP
$IPT -P FORWARD DROP

#允许所有数据包通过OPENVPN网络接口
$IPT -A INPUT -i lo        -j ACCEPT
$IPT -A INPUT -i $IF_LOCAL -j ACCEPT
$IPT -A INPUT -i $IF_OVPN  -j ACCEPT

#打开SSH端口访问
$IPT -A INPUT -p tcp --dport  22 -j ACCEPT

#充许OPENPN访问
$IPT -A INPUT -p tcp -s $OVPN_SUBCOMPANY -d $OVPN_HEADER --dport 55001 -j ACCEPT

#拒绝访问的IP：
$IPT -I INPUT   -s $BLOCKED_IPS -j DROP
$IPT -I FORWARD -s $BLOCKED_IPS -j DROP

#邮件服务器端口设置：
$IPT -A FORWARD -s $EMAIL_LOCAL -j ACCEPT
$IPT -A FORWARD -d $EMAIL_LOCAL -j ACCEPT
$IPT -t nat -A POSTROUTING -s $EMAIL_LOCAL -j MASQUERADE
$IPT -t nat -A PREROUTING -i $IF_INET -p tcp -d $FW_INET --dport   25 -j DNAT --to $EMAIL_LOCAL
$IPT -t nat -A PREROUTING -i $IF_INET -p tcp -d $FW_INET --dport   80 -j DNAT --to $EMAIL_LOCAL
$IPT -t nat -A PREROUTING -i $IF_INET -p tcp -d $FW_INET --dport  110 -j DNAT --to $EMAIL_LOCAL
$IPT -t nat -A PREROUTING -i $IF_INET -p tcp -d $FW_INET --dport  143 -j DNAT --to $EMAIL_LOCAL
$IPT -t nat -A PREROUTING -i $IF_INET -p tcp -d $FW_INET --dport  587 -j DNAT --to $EMAIL_LOCAL
$IPT -t nat -A PREROUTING -i $IF_INET -p tcp -d $FW_INET --dport  993 -j DNAT --to $EMAIL_LOCAL
$IPT -t nat -A PREROUTING -i $IF_INET -p tcp -d $FW_INET --dport  995 -j DNAT --to $EMAIL_LOCAL
$IPT -t nat -A PREROUTING -i $IF_INET -p tcp -d $FW_INET --dport 1925 -j DNAT --to-destination $EMAIL_LOCAL:25

#DNS服务器：
$IPT -A FORWARD            -p tcp --sport 1024: -s $DNS/DHCP --dport 53 -j ACCEPT
$IPT -t nat -A POSTROUTING -p tcp --sport 1024: -s $DNS/DHCP --dport 53 -j MASQUERADE
$IPT -A FORWARD            -p udp --sport 1024: -s $DNS/DHCP --dport 53 -j ACCEPT
$IPT -t nat -A POSTROUTING -p udp --sport 1024: -s $DNS/DHCP --dport 53 -j MASQUERADE
$IPT -A FORWARD            -p tcp --sport 1024: -s $DNS/DHCP --dport 80 -j ACCEPT      #允许服务器更新
$IPT -t nat -A POSTROUTING -p tcp --sport 1024: -s $DNS/DHCP --dport 80 -j MASQUERADE

#域服务器内外转发
$IPT -A FORWARD -s $DOMAIN_SERVER -j ACCEPT
$IPT -t nat -A POSTROUTING -s $DOMAIN_SERVER -j MASQUERADE

#抗病毒服务器内外转发
$IPT -A FORWARD -s $PA_NETFLOW -j ACCEPT
$IPT -t nat -A POSTROUTING -s $PA_NETFLOW -j MASQUERADE

#内外网隔离,VLAN IP段可访问外网设置
$IPT -A FORWARD -m iprange --src-range $INTERNET1_FULL_ACCESS -j ACCEPT
$IPT -t nat -A POSTROUTING -m iprange --src-range $INTERNET1_FULL_ACCESS ! -d 192.168.0.0/16 -j MASQUERADE
$IPT -A FORWARD -m iprange --src-range $INTERNET2_FULL_ACCESS  -j ACCEPT
$IPT -t nat -A POSTROUTING -m iprange --src-range $INTERNET2_FULL_ACCESS  ! -d 192.168.0.0/16 -j MASQUERADE
$IPT -A FORWARD -m iprange --src-range $INTERNET3_FULL_ACCESS  -j ACCEPT
$IPT -t nat -A POSTROUTING -m iprange --src-range $INTERNET3_FULL_ACCESS  ! -d 192.168.0.0/16 -j MASQUERADE

#外网代理端口
$IPT -A FORWARD            -p tcp -s $LAN_1 --dport 443 -j ACCEPT
$IPT -t nat -A POSTROUTING -p tcp -s $LAN_1 --dport 443 -j MASQUERADE
$IPT -A FORWARD            -p tcp -s $LAN_2 --dport 443 -j ACCEPT
$IPT -t nat -A POSTROUTING -p tcp -s $LAN_2 --dport 443 -j MASQUERADE
$IPT -A FORWARD            -p tcp -s $LAN_3 --dport 443 -j ACCEPT
$IPT -t nat -A POSTROUTING -p tcp -s $LAN_3 --dport 443 -j MASQUERADE

```

### Netfilter/Iptables Layer7 应用层过滤策略

```sh
iptables安装
wget http://download.clearfoundation.com/l7-filter/netfilter-layer7-v2.23.tar.gz
wget https://www.kernel.org/pub/linux/kernel/v2.6/linux-2.6.35.9.tar.bz2
wget http://download.clearfoundation.com/l7-filter/l7-protocols-2009-05-28.tar.gz
wget http://ftp.redhat.com/redhat/linux/enterprise/6Server/en/os/SRPMS/iptables-1.4.7-11.el6.src.rpm

Netfilter/Iptables 作为一个典型的包过滤防火墙体系，对于网络层，传输层的数据包过滤具有非常优秀的性能和效率，然而，对于一些面向局域网上网用户的Linux网关服务器，有时候还需要对QQ，MSN等聊天，使用BT下载工具等现象进行封锁。下面将介绍如何为Netfilter/Iptables 增加应用层过滤。

QQ，MSN等聊天，使用BT下载工具均使用了相对固定的应用层协议。使用L7-filter项目的补丁文件包可以为linux内核增加相应的应用层过滤功能，结合其提供的l7-protocols第7层协议定义包，能够识别不同应用层的数据特征

L7-filter项目站点：http://l7-filter.sourceforge.net/  下载最新的补丁包及协议包内核站点:http://www.kernel.org   下载内核，iptables的源码包

将netfilter-layer7 源码包中的对应补丁文件添加到内核源码中，对内核进行重新编译，安装，安装后使用新内核启动Linux操作系统。

注意：L7-filter补丁包内的数据，要与内核及iptables源码版本相匹配
注意：源码目录所在分区至少保持有2.5G的剩余磁盘空间。

========编译安装内核========

1.解压释放netfilter-layer7 和内核源码包，使用patch工具合并补丁文件
  tar xf linux-2.6.35.9.tar.bz2 -C /usr/src/    
  tar xf netfilter-layer7-v2.23.tar.gz     
  cd /usr/src     
  ln -sn linux-2.6.35.9/ linux     
  ll linux* -d     
     lrwxrwxrwx  1 root root   15 Aug 26 10:55 linux -> linux-2.6.35.9/     
     drwxrwxr-x 23 root root 4096 Nov 23  2010 linux-2.6.35.9
 
  cd linux 
  patch -p1 < /root/netfilter-layer7-v2.23/kernel-2.6.35-layer7-2.23.patch    
     patching file include/linux/netfilter/xt_layer7.h     
     patching file include/net/netfilter/nf_conntrack.h     
     patching file net/netfilter/Kconfig     
     patching file net/netfilter/Makefile     
     patching file net/netfilter/nf_conntrack_core.c     
     patching file net/netfilter/nf_conntrack_standalone.c     
     patching file net/netfilter/regexp/regexp.c     
     patching file net/netfilter/regexp/regexp.h     
     patching file net/netfilter/regexp/regmagic.h     
     patching file net/netfilter/regexp/regsub.c     
     patching file net/netfilter/xt_layer7.c
   注意：【patch -p1 】 中“1” 是数字 1，不是小写字母 L
   
2.重新配置内核编译参数，添加state机制及layer7支持【仍在内核编译目录】
   cp /boot/config-2.6.32-431.el6.x86_64 .config
   yum -y install gcc ncurses-devel 
   make menuconfig

   在配置界面中，方向键用于定位需要配置的项目
    select      进入子配置菜单
    exit	       返回上一层
    help	       查看帮助信息
    空格	        切换所选项目的编译类型
  三种状态：
    []		表示不需要该功能
    [M]		将功能编译成模块
    [*]		将功能直接编入内核

  Networking support ---> Networking options ---> Network packet filtering framework (Netfilter)
  ---> Core Netfilter Configuration --->
  <M> Netfilter connection tracking support
   <M>   "layer7" match support
   <M>   "string" match support
   <M>   "time" match support
   <M>   "iprange" address range match support
   <M>   "connlimit" match support"
   <M>   "state" match support
   <M>   "conntrack" connection match support
   <M>   "mac" address match support
   <M>   "multiport" Multiple port match support

  Networking support ---> Networking options ---> Network packet filtering framework (Netfilter)
   ---> IP: Netfilter Configuration --->
  <M> IPv4 connection tracking support (required for NAT)
   <M>   Full NAT
   <M>     MASQUERADE target support
   <M>     NETMAP target support
   <M>     REDIRECT target support

  使用Exit返回 最后当提示保存时，使用Yes确认保存，修改将保存到源码目录中的.config文件中。

3.编译新内核，并安装新内核文件
  make
  make modules_install && make install

    新内核编译安装过程将花费较长时间，数十分钟到数小时不等
    新内核文件被安装到/boot目录，模块文件将复制到/lib/modules/2.6.35.9

    如果编译内核，途中断过，想重新编译，那么先使用
        make mrproper    删除不必要的文件和目录，初次编译内核不需要
        make clean       删除不必要的模块和文件
   然后重新  make menuconfig

4.调整GRUB引导菜单，使系统以新内核启动，然后重启linux服务器 从新版内核启动
  vim /boot/grub/grub.conf   【修改default=0 ，1改为0】
       default=0
      timeout=5
      splashimage=(hd0,1)/boot/grub/splash.xpm.gz
      hiddenmenu
      title CentOS (2.6.35.9)
           root (hd0,1)
 reboot

======安装iptables/l7-protocols协议包=======

1、制作iptables升级包
  新建mockbuild用户，将l7-protocols-2009-05-28.tar.gz解压后的用于iptables 1.4.3和内核2.6.20之后的文件复制过来。
   注意目录层次。

  useradd mockbuild
  rpm -ivh iptables-1.4.7-11.el6.src.rpm
      warning: iptables-1.4.7-11.el6.src.rpm: Header V3 RSA/SHA256 Signature, key ID fd431d51: NOKEY
       1:iptables               ########################################### [100%]
  cd /root/rpmbuild/SOURCES/
  tar xf iptables-1.4.7.tar.bz2
  cd iptables-1.4.7
  cp /root/netfilter-layer7-v2.23/iptables-1.4.3forward-for-kernel-2.6.20forward/* ./extensions/
  cd ..
  tar -jcf iptables-1.4.7.tar.bz2 iptables-1.4.7/*
  mv iptables-1.4.7/ /tmp/
  cd ../SPECS/
  vim iptables.spec
       Version: 1.4.7
       Release: 11.5%{?dist}   //修改11.5表示升级

        CFLAGS="$RPM_OPT_FLAGS -fno-strict-aliasing"
           --with-kernel=/usr/src/linux --with-kbuild=/usr/src/linux --with-ksource=/usr/src/linux
              //最后 三项 参数改为编译 的内核 linux所在目录
       %changelog
       * Wed May 17 2016 Fisher 1.4.7-11.5
       - L7-filter support              //在 %changelog 后添加这两段，加入更新日志（日期为当天）

  yum install rpm-build libselinux-devel -y
  rpmbuild -ba iptables.spec


2、开始升级iptables
  cd /root/rpmbuild/RPMS/x86_64/
  rpm -Uvh iptables-1.4.7-11.5.el6.x86_64.rpm iptables-ipv6-1.4.7-11.5.el6.x86_64.rpm //可加参数 --nodeps 强制安装
  cd /tmp
  tar xf l7-protocols-2009-05-28.tar.gz
  cd  l7-protocols-2009-05-28
  make install
      mkdir -p /etc/l7-protocols
      cp -R * /etc/l7-protocols

3、检查l7-protocols协议包 
  rpm -ql iptables | grep layer7
     /lib64/xtables/libxt_layer7.so


========启用七层过滤/添加规则============

1、启用七层过滤
  # modprobe xt_layer7
  # lsmod | grep xt_layer7
      xt_layer7              12060  0
      nf_conntrack           79850  1 xt_layer7

2、查看并开启内核参数，确保net.netfilter.nf_conntrack_acct等于1
  # sysctl -a | grep conntrack_acct
      net.netfilter.nf_conntrack_acct = 1

3、在Iptables上做7层防火墙过虑限制
    vim /etc/sysctl.conf
       net.ipv4.ip_forward = 1      //开启路由转发功能
    sysctl -p
    lsmod | grep -w nf_conntrack    //查看nf_conntrack模块是否加载
        nf_conntrack           79485  6
       xt_layer7,iptable_nat,nf_nat,nf_conntrack_ipv4,nf_conntrack_ipv6,xt_state

    sysctl -a | grep acct           //查看内核连接追踪功能是否开启
    kernel.acct = 4 2   30
        ###如果下面值为0，修改为1
    net.netfilter.nf_conntrack_acct = 1
        ###打开下面文件加入到里面执行如下命令即可生效
    vim /etc/sysctl.conf
        net.netfilter.nf_conntrack_acct = 1
   sysctl -p
        ###也可使用此项命令修改，但一重启系统便会失效
    sysctl -w net.netfilter.nf_conntrack_acct=1

4、添加规则
   支持的layer7应用层协议
     匹配格式：iptables [-t 表名] -m layer7 --l7proto 协议名  
   根据时间过滤
     匹配格式：-m time --timestart 起始时间 --timestop 结束时间 --weekdays 每周的那些天
   时间格式以24小时制表示，如早9:30 晚18:00
    每周一至周日对应的英文缩写表示为：Mon、Tue、Wed、Thu、Fri、Sat、Sun 也可以使用数字表示周一至周日，如：1、2、3、4、5、6、7
  根据字符串过滤
     匹配格式：-m string --string “字符串” --algo {bm|kmp}
 实例：
  使用layer7显示匹配策略过滤使用QQ,MSN Edonkey等应用层协议的数据访问
    iptables -A FORWARD -m layer7 --l7proto qq -j DROP
   iptables -A FORWARD -m layer7 --l7proto msn-filetransfer -j DROP
   iptables -A FORWARD -m layer7 --l7proto msnmessenger -j DROP
   iptables -A FORWARD -m layer7 --l7proto bittorrenr -j DROP
   iptables -A FORWARD -m layer7 --l7proto xunlei -j DROP
   iptables -A FORWARD -m layer7 --l7proto edonkey -j DROP
  使用--connlimit 显示匹配进行数据并发连接控制，超过100个并发连接将拒绝
    iptables -A FORWARD -p tcp --syn -m connlimit --connlimit-above 100 -j DROP

  使用--time显示匹配根据时间范围设置访问策略，允许周一到周五 8:00-18:00之间的数据访问
    iptables -A FORWARD -p tcp --dport 80 -m time --timestart 8:00 --timestop 18:00 --weekdays Mon,Tue,Wed,Thu,Fri -j ACCEPT
       星期一 MON  星期二 TUE  星期三 WED  星期四 THU  星期五 FRI  星期六 SAT  星期天 SUN

  使用string显示匹配策略过滤包含tencent,verycd,色情，成人电影的网络访问
    iptables -A FORWARD   -m string --string "qq" --algo bm -j DROP
    iptables -A FORWARD  -m string --string "tencent" --algo bm -j DROP
    iptables -A FORWARD  -m string --string "verycd" --algo bm -j DROP
    iptables -A FORWARD  -m string --string "色情" --algo bm -j DROP
    iptables -A FORWARD  -m string --string "成人电影" --algo bm -j DROP
  其中--algo参数用于指定字符串识别算法，bm 或 kmp


5、查看支持的协议簇
    ls /etc/l7-protocols/protocols/

=======问题汇总=======
<code>
1、在make 内核过程中报 【gcc: error: elf_x86_64: No such file or directory】
   解决：gcc -v ，若gcc 版本为4.6 ，则不支持 linker-style 架构
      在内核目录arch/x86/vdso/Makefile中，大约在28,29行 找到 
      VDSO_LDFLAGS_vdso.lds = -m elf_x86_64 -Wl,-soname=linux-vdso.so.1 \
                -Wl,-z,max-page-size=4096 -Wl,-z,common-page-size=4096
              把"-m elf_x86_64" 替换为 "-m64"
     然后再继续找，大约在72行左右，找到
     VDSO_LDFLAGS_vdso32.lds = -m elf_i386 -Wl,-soname=linux-gate.so.1
     中的 "-m elf_i386" 替换为 "-m32"

2、在make 内核过程中报【drivers/net/igbvf/igbvf.h:129:15: 错误：重复的成员‘page’】
   解决：打开文件，看129行，代码为：struct page *page;再往上看，第124行，也有struct page *page这行代码，
   这个结构定义在内部的一个结构体中。就是他的名字与129行的重复了，而4.6.*的编译器不支持这种方式的定义，
   我们修改129行的代码为struct page *pagep；保存退出

3、在rpmbuild -bb iptables.spec 制作rpm包报 【*** ERROR: No build ID note found in /home/wuyang/rpmbuild/BUILDROOT/******
   error: Bad exit status from /var/tmp/rpm-tmp.BPd1OI (%install)】
   解决：在iptables.spec文件中任意位置添加如下参数：
    %define __debug_install_post   \
      %{_rpmconfigdir}/find-debuginfo.sh %{?_find_debuginfo_opts} "%{_builddir}/%{?buildsubdir}"\
   %{nil}

 重新打包


允许某个IP段远程访问ssh
iptables -A INPUT -p tcp -m tcp --dport 9527 -s 192.168.64.0/24 -j ACCEPT
开启80端口
iptables -A INPUT -P tcp -m tcp --dropt 80 -j ACCEPT
允许某个IP的所有请求
iptables -A INPUT -p all -s 124.43.56.90/30 -j ACCEPT
iptables -A INPUT -m state --state RELATED,ESTABLISHED -j ACCEPT
iptables -P INPUT DROP
iptables -P OUTPUT ACCEPT
iptables -P FORWARD DROP
/etc/init.d/iptables save
/etc/init.d/iptables restart



1. 删除已有规则
在新设定iptables规则时，我们一般先确保旧规则被清除，用以下命令清除旧规则：
iptables -F
(or iptables --flush)
2. 设置chain策略
对于filter table，默认的chain策略为ACCEPT，我们可以通过以下命令修改chain的策略：
iptables -P INPUT DROP
iptables -P FORWARD DROP
iptables -P OUTPUT DROP
以上命令配置将接收、转发和发出包均丢弃，施行比较严格的包管理。由于接收和发包均被设置为丢弃，当
进一步配置其他规则的时候，需要注意针对INPUT和OUTPUT分别配置。当然，如果信任本机器往外发包，
以上第三条规则可不必配置。
3. 屏蔽指定ip
有时候我们发现某个ip不停的往服务器发包，这时我们可以使用以下命令，将指定ip发来的包丢弃：
BLOCK_THIS_IP="x.x.x.x"iptables -A INPUT -i eth0 -p tcp -s "$BLOCK_THIS_IP" -j DROP
以上命令设置将由x.x.x.x ip发往eth0网口的tcp包丢弃。
4. 配置服务项
利用iptables，我们可以对日常用到的服务项进行安全管理，比如设定只能通过指定网段、由指定网口通过
SSH连接本机：
iptables -A INPUT -i eth0 -p tcp -s 192.168.100.0/24 --dport 22 -m state --state NEW,ESTABLESHED -j ACCEPT
iptables -A OUTPUT -o eth0 -p tcp --sport 22 -m state --state ESTABLISHED -j ACCEPT
若要支持由本机通过SSH连接其他机器，由于在本机端口建立连接，因而还需要设置以下规则：
iptables -A INPUT -i eth0 -p tcp -s 192.168.100.0/24 --dport 22 -m state --state ESTABLESHED -j ACCEPT
iptables -A OUTPUT -o eth0 -p tcp --sport 22 -m state --state NEW,ESTABLISHED -j ACCEPT
类似的，对于HTTP/HTTPS(80/443)、pop3(110)、rsync(873)、MySQL(3306)等基于tcp连接的服务，也可以参
照上述命令配置。
对于基于udp的dns服务，使用以下命令开启端口服务：
iptables -A OUTPUT -p udp -o eth0 --dport 53 -j ACCEPT
iptables -A INPUT -p udp -i eth0 --sport 53 -j ACCEPT
5. 网口转发配置
对于用作防火墙或网关的服务器，一个网口连接到公网，其他网口的包转发到该网口实现内网向公网通信，
假设eth0连接内网，eth1连接公网，配置规则如下：
iptables -A FORWARD -i eth0 -o eth1 -j ACCEPT
6. 端口转发配置
对于端口，我们也可以运用iptables完成转发配置：
iptables -t nat -A PREROUTING -p tcp -d 192.168.102.37 --dport 422 -j DNAT --to 192.168.102.37:22
以上命令将422端口的包转发到22端口，因而通过422端口也可进行SSH连接，当然对于422端口，我们也需要
像以上“4.配置服务项”一节一样，配置其支持连接建立的规则。
7. DoS攻击防范
利用扩展模块limit，我们还可以配置iptables规则，实现DoS攻击防范：
iptables -A INPUT -p tcp --dport 80 -m limit --limit 25/minute --limit-burst 100 -j ACCEPT
–litmit 25/minute 指示每分钟限制最大连接数为25
–litmit-burst 100 指示当总连接数超过100时，启动 litmit/minute 限制
8. 配置web流量均衡
我们可以将一台服务器作为前端服务器，利用iptables进行流量分发，配置方法如下：
iptables -A PREROUTING -i eth0 -p tcp --dport 80 -m state --state NEW -m nth --counter 0 --every 3 --packet 0 -j
DNAT --to-destination 192.168.1.101:80
iptables -A PREROUTING -i eth0 -p tcp --dport 80 -m state --state NEW -m nth --counter 0 --every 3 --packet 0 -j
DNAT --to-destination 192.168.1.102:80
iptables -A PREROUTING -i eth0 -p tcp --dport 80 -m state --state NEW -m nth --counter 0 --every 3 --packet 0 -j
DNAT --to-destination 192.168.1.103:80
以上配置规则用到nth扩展模块，将80端口的流量均衡到三台服务器。
9. 将丢弃包情况记入日志
使用LOG目标和syslog服务，我们可以记录某协议某端口下的收发包情况。拿记录丢包情况举例，可以通过以
下方式实现。
首先自定义一个chain：
iptables -N LOGGING
其次将所有接收包导入LOGGING chain中：
iptables -A INPUT -j LOGGING
然后设置日志前缀、日志级别：
iptables -A LOGGING -m limit --limit 2/min -j LOG --log-prefix "IPTables Packet Dropped: " --log-level 7
最后将包倒向DROP，将包丢弃：
iptables -A LOGGING -j DROP
另可以配置syslog.conf文件，指定iptables的日志输出。
ps -eo"pid,stime,args"
ps -eo rss,pmem,pcpu,vsize,args | sort -k 1 -r -n | less





```

<!-- Linux命令行搜索引擎：https://jaywcjlove.github.io/linux-command/ -->
