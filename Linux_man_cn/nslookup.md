# nslookup

## 说明

**nslookup命令** 是常用域名查询工具，就是查DNS信息用的命令

nslookup4有两种工作模式，即“交互模式”和“非交互模式”。在“交互模式”下，用户可以向域名服务器查询各类主机、域名的信息，或者输出域名中的
主机列表。而在“非交互模式”下，用户可以针对一个主机或域名仅仅获取特定的名称或所需信息

输入nslookup命令直接进入交互模式，此时nslookup会连接到默认的域名服务器（即`/etc/resolv.conf`的第一个dns地址）。或者输入
`nslookup -nameserver/ip`。进入非交互模式，就直接输入`nslookup 域名`就可以

## 选项

```markdown
-sil：不显示任何警告信息
```

## 实例

```bash
nslookup www.jsdig.com

```


