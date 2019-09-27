# **ethtool**

## 说明

ethtool命令用于获取以太网卡的配置信息，或者修改这些配置。这个命令比较复杂，功能特别多

## 选项

```markdown
ethtool [ -a | -c | -g | -i | -d | -k | -r | -S |] ethX
ethtool [-A] ethX [autoneg on|off] [rx on|off] [tx on|off]
ethtool [-C] ethX [adaptive-rx on|off] [adaptive-tx on|off] [rx-usecs N] [rx-frames N] [rx-usecs-irq N] [rx-frames-irq N] [tx-usecs N] [tx-frames N] [tx-usecs-irq N] [tx-frames-irq N] [stats-block-usecs N][pkt-rate-low N][rx-usecs-low N] [rx-frames-low N] [tx-usecs-low N] [tx-frames-lowN] [pkt-rate-high N] [rx-usecs-high N] [rx-frames-high N] [tx-usecs-high N] [tx-frames-high N] [sample-interval N]
ethtool [-G] ethX [rx N] [rx-mini N] [rx-jumbo N] [tx N]
ethtool [-e] ethX [raw on|off] [offset N] [length N]
ethtool [-E] ethX [magic N] [offset N] [value N]
ethtool [-K] ethX [rx on|off] [tx on|off] [sg on|off] [tso on|off]
ethtool [-p] ethX [N]
ethtool [-t] ethX [offline|online]
ethtool [-s] ethX [speed 10|100|1000] [duplex half|full] [autoneg on|off] [port tp|aui|bnc|mii] [phyad N] [xcvr internal|external]
[wol p|u|m|b|a|g|s|d...] [sopass xx:yy:zz:aa:bb:cc] [msglvl N]

-a 查看网卡中 接收模块RX、发送模块TX和Autonegotiate模块的状态：启动on 或 停用off
-A 修改网卡中 接收模块RX、发送模块TX和Autonegotiate模块的状态：启动on 或 停用off
-c display the Coalesce information of the specified ethernet card
-C Change the Coalesce setting of the specified ethernet card
-g Display the rx/tx ring parameter information of the specified ethernet card
-G change the rx/tx ring setting of the specified ethernet card
-i 显示网卡驱动的信息，如驱动的名称、版本等
-d 显示register dump信息, 部分网卡驱动不支持该选项
-e 显示EEPROM dump信息，部分网卡驱动不支持该选项
-E 修改网卡EEPROM byte
-k 显示网卡Offload参数的状态：on 或 off，包括rx-checksumming、tx-checksumming等
-K 修改网卡Offload参数的状态
-p 用于区别不同ethX对应网卡的物理位置，常用的方法是使网卡port上的led不断的闪；N指示了网卡闪的持续时间，以秒为单位
-r 如果auto-negotiation模块的状态为on，则restarts auto-negotiation
-S 显示NIC- and driver-specific 的统计参数，如网卡接收/发送的字节数、接收/发送的广播包个数等
-t 让网卡执行自我检测，有两种模式：offline or online
-s 修改网卡的部分配置，包括网卡速度、单工/全双工模式、mac地址等

   ethtool DEVNAME	Display standard information about device
   ethtool -s|--change DEVNAME	Change generic options
	[ speed %d ]
	[ duplex half|full ]
	[ port tp|aui|bnc|mii|fibre ]
	[ mdix auto|on|off ]
	[ autoneg on|off ]
	[ advertise %x ]
	[ phyad %d ]
	[ xcvr internal|external ]
	[ wol p|u|m|b|a|g|s|d... ]
	[ sopass %x:%x:%x:%x:%x:%x ]
	[ msglvl %d | msglvl type on|off ... ]
   ethtool -a|--show-pause DEVNAME	Show pause options
   ethtool -A|--pause DEVNAME	Set pause options
	[ autoneg on|off ]
	[ rx on|off ]
	[ tx on|off ]
   ethtool -c|--show-coalesce DEVNAME	Show coalesce options
   ethtool -C|--coalesce DEVNAME	Set coalesce options
	[adaptive-rx on|off]
	[adaptive-tx on|off]
	[rx-usecs N]
	[rx-frames N]
	[rx-usecs-irq N]
	[rx-frames-irq N]
	[tx-usecs N]
	[tx-frames N]
	[tx-usecs-irq N]
	[tx-frames-irq N]
	[stats-block-usecs N]
	[pkt-rate-low N]
	[rx-usecs-low N]
	[rx-frames-low N]
	[tx-usecs-low N]
	[tx-frames-low N]
	[pkt-rate-high N]
	[rx-usecs-high N]
	[rx-frames-high N]
	[tx-usecs-high N]
	[tx-frames-high N]
	[sample-interval N]
   ethtool -g|--show-ring DEVNAME	Query RX/TX ring parameters
   ethtool -G|--set-ring DEVNAME	Set RX/TX ring parameters
	[ rx N ]
	[ rx-mini N ]
	[ rx-jumbo N ]
	[ tx N ]
   ethtool -k|--show-features|--show-offload DEVNAME	Get state of protocol offload and other features
   ethtool -K|--features|--offload DEVNAME	Set protocol offload and other features
	FEATURE on|off ...
   ethtool -i|--driver DEVNAME	Show driver information
   ethtool -d|--register-dump DEVNAME	Do a register dump
	[ raw on|off ]
	[ file FILENAME ]
   ethtool -e|--eeprom-dump DEVNAME	Do a EEPROM dump
	[ raw on|off ]
	[ offset N ]
	[ length N ]
   ethtool -E|--change-eeprom DEVNAME	Change bytes in device EEPROM
	[ magic N ]
	[ offset N ]
	[ length N ]
	[ value N ]
   ethtool -r|--negotiate DEVNAME	Restart N-WAY negotiation
   ethtool -p|--identify DEVNAME	Show visible port identification (e.g. blinking)
          [ TIME-IN-SECONDS ]
   ethtool -t|--test DEVNAME	Execute adapter self test
          [ online | offline | external_lb ]
   ethtool -S|--statistics DEVNAME	Show adapter statistics
   ethtool --phy-statistics DEVNAME	Show phy statistics
   ethtool -n|-u|--show-nfc|--show-ntuple DEVNAME	Show Rx network flow classification options or rules
	[ rx-flow-hash tcp4|udp4|ah4|esp4|sctp4|tcp6|udp6|ah6|esp6|sctp6 [context %d] |
	  rule %d ]
   ethtool -N|-U|--config-nfc|--config-ntuple DEVNAME	Configure Rx network flow classification options or rules
	rx-flow-hash tcp4|udp4|ah4|esp4|sctp4|tcp6|udp6|ah6|esp6|sctp6 m|v|t|s|d|f|n|r... [context %d] |
	flow-type ether|ip4|tcp4|udp4|sctp4|ah4|esp4|ip6|tcp6|udp6|ah6|esp6|sctp6
		[ src %x:%x:%x:%x:%x:%x [m %x:%x:%x:%x:%x:%x] ]
		[ dst %x:%x:%x:%x:%x:%x [m %x:%x:%x:%x:%x:%x] ]
		[ proto %d [m %x] ]
		[ src-ip IP-ADDRESS [m IP-ADDRESS] ]
		[ dst-ip IP-ADDRESS [m IP-ADDRESS] ]
		[ tos %d [m %x] ]
		[ tclass %d [m %x] ]
		[ l4proto %d [m %x] ]
		[ src-port %d [m %x] ]
		[ dst-port %d [m %x] ]
		[ spi %d [m %x] ]
		[ vlan-etype %x [m %x] ]
		[ vlan %x [m %x] ]
		[ user-def %x [m %x] ]
		[ dst-mac %x:%x:%x:%x:%x:%x [m %x:%x:%x:%x:%x:%x] ]
		[ action %d ]
		[ context %d ]
		[ loc %d]] |
	delete %d
   ethtool -T|--show-time-stamping DEVNAME	Show time stamping capabilities
   ethtool -x|--show-rxfh-indir|--show-rxfh DEVNAME	Show Rx flow hash indirection table and/or RSS hash key
	[ context %d ]
   ethtool -X|--set-rxfh-indir|--rxfh DEVNAME	Set Rx flow hash indirection table and/or RSS hash key
	[ context %d|new ]
	[ equal N | weight W0 W1 ... | default ]
	[ hkey %x:%x:%x:%x:%x:.... ]
	[ hfunc FUNC ]
	[ delete ]
   ethtool -f|--flash DEVNAME	Flash firmware image from the specified file to a region on the device
          FILENAME [ REGION-NUMBER-TO-FLASH ]
   ethtool -P|--show-permaddr DEVNAME	Show permanent hardware address
   ethtool -w|--get-dump DEVNAME	Get dump flag, data
	[ data FILENAME ]
   ethtool -W|--set-dump DEVNAME	Set dump flag of the device
	N
   ethtool -l|--show-channels DEVNAME	Query Channels
   ethtool -L|--set-channels DEVNAME	Set Channels
          [ rx N ]
          [ tx N ]
          [ other N ]
          [ combined N ]
   ethtool --show-priv-flags DEVNAME	Query private flags
   ethtool --set-priv-flags DEVNAME	Set private flags
	FLAG on|off ...
   ethtool -m|--dump-module-eeprom|--module-info DEVNAME	Query/Decode Module EEPROM information and optical diagnostics if available
	[ raw on|off ]
	[ hex on|off ]
	[ offset N ]
	[ length N ]
   ethtool --show-eee DEVNAME	Show EEE settings
   ethtool --set-eee DEVNAME	Set EEE settings
	[ eee on|off ]
	[ advertise %x ]
	[ tx-lpi on|off ]
	[ tx-timer %d ]
   ethtool --show-fec DEVNAME	Show FEC settings
   ethtool --set-fec DEVNAME	Set FEC settings
	[ encoding auto|off|rs|baser ]

```

## 数据来源

Ethtool命令显示的信息来源于网卡驱动层，即TCP/ip协议的链路层。该命令在Linux内核中实现的逻辑层次为：

最重要的结构体`struct ethtool_ops`，该结构体成员为用于显示或修改以太网卡配置的一系列函数指针，见下表中的第二列

网卡驱动负责实现（部分）这些函数，并将其封装入`ethtool_ops`结构体，为网络核心层提供统一的调用接口。因此，不同的网卡驱动
会给应用层返回不同的信息。`Ethtool命令选项`、`struct ethtool_ops成员函数`、`Ethtool命令显示参数的来源`，三者间的对应关系
如下表所示：

| 命令选项 | struct ethtool_ops成员函数 | Ethtool命令显示参数的来源（以网卡驱动BNX2为例） |
| :------: | :------: | :------: |
| 无 -s | get_settingsget_wol get_msglevel get_link set_settings set_wol set_msglevel | 从网卡寄存器中获得网卡速度等信息，可配置 |
| -a -A | get_pauseparam set_pauseparam | 从网卡寄存器中获得Autonegotiate/RX/TX模块的状态：on oroff，可配置 |
| -c -C | get_coalesceset_coalesce | 从网卡寄存器中获得coalescing参数：TX/RX一个数据包后，推迟发生TX/RX中断的时间(us)/数据包个数<br>—减小该值可以提高网卡的响应时间。 当rx-usecs&rx-frames同时被设为0时，RX中断停止。 当tx-usecs&tx-frames同时被设为0时，TX中断停止 |
| -g -G | get_ringparam set_ringparam | 除当前TX/RX ring的值（从网卡寄存器中读取得到，可配置）外，其它为网卡bnx2自己固定的信息 |
| -k -K | get_rx_csumget_tx_csum get_sg get_tso set_rx_csum set_tx_csum set_sg set_tso | 显示信息从保存该状态的变量中读取<br>得到，没有对应的寄存器。因此，TX/RX校验等模块一直处于on状态，实际上是无法修改的 |
| -i | get_drvinfo[self_test_count, get_stats_coun,t get_regs_len, get_eeprom_len] | 网卡bnx2自己固定的信息，如：<br>—– driver: bnx2 version: 1.4.30 firmware-version: 1.8.0.5 bus-info: 0000:09:00.0 —— |
| -d | get_drvinfoget_regs | 不支持，即bnx2中没有实现函数get_regs |
| -e -E | get_eepromset_eeprom | 不支持，即bnx2中没有实现函数get_eeprom |
| -r | nway_reset | 配置网卡MII_BMCR寄存器，重启Auto negotiation模块 |
| -p | phys_id | 配置网卡BNX2_EMAC_LED寄存器，实现LED闪功能 |
| -t | self_test | 通过配置网卡寄存器，逐一测试网卡的硬件模块：registers，memory，loopback，Link stat，interrupt |
| -S | get_ethtool_stats | 显示信息来源于网卡驱动中的结构体变量stats_blk。（网卡通过DMA方式，将寄存器BNX2_HC_STATISTICS_ADDR_L<br>和BNX2_HC_STATISTICS_ADDR_H中的数据实时地读取到结构体变量struct statistics_block *stats_blk中。） —显示的数据都是从网卡寄存器中统计得到的，各项的含义需查询网卡（芯片）手册 |

由上可见，ethtool命令用于显示/配置网卡硬件（寄存器）

## 实例

```bash
ethool eth0 # 查看机器上网卡的速度：百兆还是千兆
ethtool -A tx off eth0  # 输出信息中`Speed:`这一项就指示了网卡的速度。停止网卡的发送模块TX
ethtool -i eth0     # 可输入`ethtool -a eth0`，查看tx模块是否已被停止。查看网卡eth0采用了何种驱动
ethtool -K eth0 rx off  # 显示 driver: bnx2；version: 1.4.30 等信息。关闭网卡对收到的数据包的校验功能
ethtool -p eth0 10  # 可输入`ethtool –k eth0`，查看校验功能是否已被停止。如安装了两块网卡，查询eth0对应那块网卡
ethtool -S eth0     # 看哪块网卡的led灯在闪，eth0就对应着哪块网卡。查看网卡，在接收/发送数据时，有没有出错
ethtool -s eth0 speed 100   # 将千兆网卡的速度降为百兆
ethtool --change eth0 autoneg off speed 100 duplex full     # 手动设制网卡速度
```
