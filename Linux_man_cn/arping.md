# arping

## 说明

**arping命令** 是用于发送arp请求到一个相邻主机的工具，arping使用arp数据包，通过ping命令检查设备上的硬件地址。能够测试一个ip地址是否
在网络上已经被使用，并能够获取更多设备信息。功能类似于ping

## 选项

```markdown
-f : quit on first reply
-q : be quiet
-b : keep broadcasting, don't go unicast
-D : duplicate address detection mode
-U : Unsolicited ARP mode, update your neighbours
-A : ARP answer mode, update your neighbours
-V : print version and exit
-c count : how many packets to send
-w timeout : how long to wait for a reply
-I device : which ethernet device to use
-s source : source ip address
destination : ask for what ip address

```

## 实例

```bash
arping www.baidu.com 

```


