# **ssh**

## 说明

**ssh命令** 是openssh套件中的客户端连接工具，可以给予ssh加密协议实现安全的远程登录服务器

## 选项

```markdown
ssh [-1246AaCfGgKkMNnqsTtVvXxYy] [-b bind_address] [-c cipher_spec]
           [-D [bind_address:]port] [-E log_file] [-e escape_char]
           [-F configfile] [-I pkcs11] [-i identity_file]
           [-J [user@]host[:port]] [-L address] [-l login_name] [-m mac_spec]
           [-O ctl_cmd] [-o option] [-p port] [-Q query_option] [-R address]
           [-S ctl_path] [-W host:port] [-w local_tun[:remote_tun]]
           [user@]hostname [command]

-1      强制使用ssh协议版本1
-2      强制使用ssh协议版本2
-4      强制使用IPv4地址
-6      强制使用IPv6地址
-A      开启认证代理连接转发功能
-a      关闭认证代理连接转发功能
-b      使用本机指定地址作为对应连接的源ip地址
-C      请求压缩所有数据
-F      指定ssh指令的配置文件
-f      后台执行ssh指令
-g      允许远程主机连接主机的转发端口
-i      指定身份文件
-l      指定连接远程服务器登录用户名
-N      不执行远程指令
-o      指定配置选项
-p      指定远程服务器上的端口
-q      静默模式
-X      开启X11转发功能
-x      关闭X11转发功能
-y      开启信任X11转发功能
```

## 实例

```bash


#### 如何更改 SSH 服务的端口号

SSH 服务器是默认运行在 22 号端口上的。然而，由于某些原因需要，它也可以运行在别的端口上。比如为了方便测试使用，又比如在同一个宿主机上运行多个不同的配置。当然，极少情况下，不使用 root 权限运行它也可以，比如某些必须运行在非特权的端口的情况（端口号大于等于 1024）。

端口号可以在配置文件 /etc/ssh/sshd_config 中将 Port 22 更改。也可以使用 -p  选项运行 sshd。SSH 客户端和 sftp 程序也可以使用 -p  选项。

#### 配置 SSH 协议穿越防火墙

SSH 是少数通常被许可穿越防火墙的协议之一。通常的做法是不限制出站的 SSH 连接，尤其常见于一些较小的或者比较技术型的组织中，而入站的 SSH 连接通常会限制到一台或者是少数几台服务器上。

#### 出站的 SSH 连接

在防火墙中配置出站的 SSH 连接十分简单。如果完全限制了外发连接，那么只需要创建一个允许 TCP 端口 22 可以外发的规则即可。如果你想限制目标地址，你可以限制该规则仅允许访问你的组织放在云端的外部服务器或保护该云端的跳板服务器即可。

#### 反向通道是有风险的

其实不限制出站的 SSH 连接虽然是可以的，但是是存在风险的，SSH 协议是支持 通道访问 的。最初的想法是在外部服务器搭建一个 SSH 服务监听来自各处的连接，将进入的连接转发到组织，并让这个连接可以访问某个内部服务器。

在某些场景下这当然非常的方便。开发者和系统管理员经常使用它打开一个通道以便于他们可以远程访问，比如在家里或者在旅行中使用笔记本电脑等场景。

然而通常来讲这些做法是违背安全策略的，跳过了防火墙管理员和安全团队保护的控制无疑是违背安全策略的，比如这些： PCI、HIPAA、NIST SP 800-53 等。它可以被黑客和外国情报机构用来在组织内留下后门。

CryptoAuditor 是一款可以控制通道穿过防火墙或者一组云端服务器入口的产品。该款产品可以配合 通用 SSH 密钥管理器（Universal SSH Key Manager） 来获得对 主机密钥（host keys）的访问，以在启用防火墙并阻挡未授权转发的场景中解密 SSH 会话。

#### 入站的 SSH 访问

对于入站访问而言，这里有几点需要说一下：

配置防火墙，并转发所有去往 22 端口的连接只能流向到一个特定的内部网络 IP 地址或者一个 DMZ 主机。在该 IP 上运行 CryptoAuditor 或者跳板机来控制和审查所有访问该组织的连接。
在防火墙上使用不同的端口访问不同的服务器。
只允许使用 IPsec 协议这样的 VPN（虚拟专用网）登录后连接 SSH 服务。

#### 通过 iptables 服务限制 SSH 访问

iptables 是一款内建在 Linux 内核的宿主防火墙。通常配置用于保护服务器以防止被访问那些未明确开启的端口。

如果服务器上启用了 iptables，使用下面的命令将可以允许进入的 SSH 访问，当然命令需要以 root 身份运行。

```
iptables -A INPUT -p tcp --dport 22 -m conntrack --ctstate NEW,ESTABLISHED -j ACCEPT
iptables -A OUTPUT -p tcp --sport 22 -m conntrack --ctstate ESTABLISHED -j ACCEPT
```

如果你想将上述命令创建的规则持久地保存，在某些系统版本中，可使用如下命令：

```
service iptables save
```


