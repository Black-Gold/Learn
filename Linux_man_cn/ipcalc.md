# ipcalc

## 说明

**ipcalc命令** 是一个简单的ip地址计算器，可以完成简单的IP地址计算任务

## 选项

```markdown
-c, --check         Validate IP address for specified address family
-4, --ipv4          IPv4 address family (default)
-6, --ipv6          IPv6 address family
-b, --broadcast     Display calculated broadcast address
-h, --hostname      Show hostname determined via DNS
-m, --netmask       Display default netmask for IP (class A, B, or C)
-n, --network       Display network address
-p, --prefix        Display network prefix
-s, --silent        Don't ever display error messages

```

## 实例

```bash
ipcalc -p 192.168.2.1 255.255.255.0 # 输出：PREFIX=24
ipcalc -n 192.168.2.1 255.255.255.0 # 输出：NETWORK=192.168.2.0
ipcalc -h 127.0.0.1 # 输出：hostname=localhost.localdomain
ipcalc -m 192.168.2.1   # 输出：NETMASK=255.255.255.0
ipcalc -pnbm 192.168.2.1 255.255.255.0  # 输出以上四个选项所有

```


