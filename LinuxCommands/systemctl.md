systemctl
===

系统服务管理器指令

## 补充说明

**systemctl命令** 是系统服务管理器指令，它实际上将 service 和 chkconfig 这两个命令组合到一起。

<table>

<tbody>

<tr>

<td>任务</td>

<td>旧指令</td>

<td>新指令</td>

</tr>

<tr>

<td>使某服务自动启动</td>

<td>chkconfig --level 3 httpd on</td>

<td>systemctl enable httpd.service</td>

</tr>

<tr>

<td>使某服务不自动启动</td>

<td>chkconfig --level 3 httpd off</td>

<td>systemctl disable httpd.service</td>

</tr>

<tr>

<td>检查服务状态</td>

<td>service httpd status</td>

<td>systemctl status httpd.service （服务详细信息） systemctl is-active httpd.service （仅显示是否 Active)</td>

</tr>

<tr>

<td>显示所有已启动的服务</td>

<td>chkconfig --list</td>

<td>systemctl list-units --type=service</td>

</tr>

<tr>

<td>启动某服务</td>

<td>service httpd start</td>

<td>systemctl start httpd.service</td>

</tr>

<tr>

<td>停止某服务</td>

<td>service httpd stop</td>

<td>systemctl stop httpd.service</td>

</tr>

<tr>

<td>重启某服务</td>

<td>service httpd restart</td>

<td>systemctl restart httpd.service</td>

</tr>

</tbody>

</table>

### 实例  

1.启动nfs服务

```
systemctl start nfs-server.service
```

2.设置开机自启动

```
systemctl enable nfs-server.service
```

3.停止开机自启动

```
systemctl disable nfs-server.service
```

4.查看服务当前状态

```
systemctl status nfs-server.service
```

5.重新启动某服务

```
systemctl restart nfs-server.service
```

6.查看所有已启动的服务

```
systemctl list -units --type=service
```

开启防火墙22端口

```
iptables -I INPUT -p tcp --dport 22 -j accept
```

如果仍然有问题，就可能是SELinux导致的

关闭SElinux：

修改`/etc/selinux/config`文件中的`SELINUX=””`为disabled，然后重启。

彻底关闭防火墙：

```
sudo systemctl status firewalld.service
sudo systemctl stop firewalld.service          
sudo systemctl disable firewalld.service
```

```sh
1.systemctl
# 重启系统
systemctl reboot
# 关闭系统，切断电源
systemctl poweroff
# CPU停止工作
systemctl halt
# 暂停系统
systemctl suspend
# 让系统进入冬眠状态
systemctl hibernate
# 让系统进入交互式休眠状态
systemctl hybrid-sleep
# 启动进入救援状态（单用户状态）
systemctl rescue
2.systemd-analyze
# 查看启动耗时
systemd-analyze
# 查看每个服务的启动耗时
systemd-analyze blame
# 显示瀑布状的启动过程流
systemd-analyze critical-chain
# 显示指定服务的启动流
systemd-analyze critical-chain atd.service
3.hostnamectl
# 显示当前主机的信息
hostnamectl
# 设置主机名。
hostnamectl set-hostname rhel7
4.localectl
# 查看本地化设置
localectl
# 设置本地化参数。
localectl set-locale LANG=en_GB.utf8 localectl set-keymap en_GB
5.timedatectl
# 查看当前时区设置
timedatectl
# 显示所有可用的时区
timedatectl list-timezones
# 设置当前时区
timedatectl set-timezone America/New_York
timedatectl set-time YYYY-MM-DD
timedatectl set-time HH:MM:SS
6.loginctl
# 列出当前session
loginctl list-sessions
# 列出当前登录用户
loginctl list-users
# 列出显示指定用户的信息
loginctl show-user ruanyf
# 列出正在运行的 Unit
systemctl list-units
# 列出所有Unit，包括没有找到配置文件的或者启动失败的
systemctl list-units --all
# 列出所有没有运行的 Unit
systemctl list-units --all --state=inactive
# 列出所有加载失败的 Unit
systemctl list-units --failed
# 列出所有正在运行的、类型为 service 的 Unit
systemctl list-units --type=service

除了systemctl status ，还有三个查询状态方法，主要是脚本内部的判断语句使用
# 显示某个 Unit 是否正在运行
systemctl is-active application.service
# 显示某个 Unit 是否处于启动失败状态
systemctl is-failed application.service
# 显示某个 Unit 服务是否建立了启动链接
systemctl is-enabled application.service
```

### 常用systemctl命令

```sh
# 立即启动一个服务
systemctl start apache.service
# 立即停止一个服务
systemctl stop apache.service
# 重启一个服务
systemctl restart apache.service
# 杀死一个服务的所有子进程
systemctl kill apache.service
# 重新加载一个服务的配置文件
systemctl reload apache.service
# 重载所有修改过的配置文件
systemctl daemon-reload
# 显示某个 Unit 的所有底层参数
$ systemctl show httpd.service
# 显示某个 Unit 的指定属性的值
$ systemctl show -p CPUShares httpd.service
# 设置某个 Unit 的指定属性
systemctl set-property httpd.service CPUShares=500
# 列出一个unit的所有依赖
systemctl list-dependencies nginx.service
# 列出所有systemctl配置文件
systemctl list-unit-files
# 列出指定类型的配置文件
systemctl list-unit-files --type=service
# 查看当前系统的所有 Target
$ systemctl list-unit-files --type=target
# 查看一个 Target 包含的所有 Unit
$ systemctl list-dependencies multi-user.target
# 查看启动时的默认 Target
$ systemctl get-default
# 设置启动时的默认 Target
systemctl set-default multi-user.target
# 查看所有日志（默认情况下 ，只保存本次启动的日志）
journalctl
# 查看内核日志（不显示应用日志）
journalctl -k
# 查看系统本次启动的日志
journalctl -b
journalctl -b -0
# 查看上一次启动的日志（需更改设置）
journalctl -b -1
# 查看指定时间的日志
journalctl --since="2012-10-30 18:17:16"
journalctl --since "20 min ago"
journalctl --since yesterday
journalctl --since "2015-01-10" --until "2015-01-11 03:00" journalctl --since 09:00 --until "1 hour ago"
# 显示尾部的最新10行日志
journalctl -n
# 显示尾部指定行数的日志
journalctl -n 20
# 实时滚动显示最新日志
journalctl -f
# 查看指定服务的日志
journalctl /usr/lib/systemd/systemd
# 查看指定进程的日志
journalctl _PID=1
# 查看某个路径的脚本的日志
journalctl /usr/bin/bash
# 查看指定用户的日志
journalctl _UID=33 --since today
# 查看某个 Unit 的日志
journalctl -u nginx.service
journalctl -u nginx.service --since today
# 实时滚动显示某个 Unit 的最新日志
journalctl -u nginx.service -f
# 合并显示多个 Unit 的日志
journalctl -u nginx.service -u php-fpm.service --since today
# 查看指定优先级（及其以上级别）的日志，共有8级
0: emerg
1: alert
2: crit
3: err
4: warning
5: notice
6: info
7: debug
journalctl -p err -b
# 日志默认分页输出，--no-pager 改为正常的标准输出
journalctl --no-pager
# 以 JSON 格式（单行）输出
journalctl -b -u nginx.service -o json
# 以 JSON 格式（多行）输出，可读性更好
journalctl -b -u nginx.serviceqq -o json-pretty
# 显示日志占据的硬盘空间
journalctl --disk-usage
# 指定日志文件占据的最大空间
journalctl --vacuum-size=1G
# 指定日志文件保存多久
journalctl --vacuum-time=1years
```

<!-- Linux命令行搜索引擎：https://jaywcjlove.github.io/linux-command/ -->