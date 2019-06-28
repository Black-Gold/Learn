# **syslog**

## 说明

**syslog** 是Linux系统默认的日志守护进程。默认的syslog配置文件是/etc/syslog.conf文件。程序，守护进程和内核提供了访问系统的日志信息。因此，任何希望生成日志信息的程序都可以向 syslog 接口呼叫生成该信息。

几乎所有的网络设备都可以通过syslog协议，将日志信息以用户数据报协议(UDP)方式传送到远端服务器，远端接收日志服务器必须通过syslogd监听UDP 端口514，并根据 syslog.conf配置文件中的配置处理本机，接收访问系统的日志信息，把指定的事件写入特定文件中，供后台数据库管理和响应之用。意味着可以让任何事件都登录到一台或多台服务器上，以备后台数据库用off-line(离线) 方法分析远端设备的事件。

通常，syslog 接受来自系统的各种功能的信息，每个信息都包括重要级。/etc/syslog.conf 文件通知 syslogd 如何根据设备和信息重要级别来报告信息。

此 rsyslogd 后台进程负责搜集来自应用程序与核心的服务消息，然后送至日志档内 (通常保存在 /var/log/ 文件夹内)。遵守 /etc/rsyslog.conf 配置文件的要求。
每个日志信息都和应用子系统相关联（文档中称为“facility”）：
auth 和 authpriv：用于授权；
cron：源于任务调度服务， cron 和 atd；
daemon：影响未分类的守护进程（DNS， NTP，等）；
ftp：涉及FTP 服务器；
kern：源于内核的消息
lpr：源于打印子系统；
mail：源于电子邮件子系统；
news：Usenet 子系统消息（主要源自NNTP －网络消息传输协议－管理新闻组的服务器）；
syslog：源于 syslogd 服务自身的消息；
user：用户消息；
uucp：源于UUCP（Unix to Unix Copy Program，一种老式的分发电子邮件消息的协议）服务的消息；
local0 到 local7：保留本地使用。
每种消息都有其优先级。下面按降序列出：
emerg：“救命！” 紧急状态，系统可能已挂了。
alert赶快，任何推迟都是危险的，必须马上采取行动；
crit：情况很严苛；
err：错误；
warn：警告（潜在的错误）；
notice：正常情况，但是该消息很重要；
info：提供信息；
debug：调试消息。

### 使用方法  

在/var/log中创建并写入日志信息是由syslog协议处理的，是由守护进程sylogd负责执行。每个标准的进程都可以用syslog记录日志。可以使用logger命令通过syslogd记录日志。

要向syslog文件/var/log/messages中记录日志信息：

```
logger this is a test log line

输出：
tail -n 1 messages
Jan  5 10:07:03 localhost root: this is a test log line

```

如果要记录特定的标记（tag）可以使用：

```
logger -t TAG this is a test log line

输出：
tail -n 1 messages
Jan  5 10:37:14 localhost TAG: this is a test log line
```


