# **dmesg**

## 说明

**dmesg命令** 被用于检查和控制内核的环形缓冲区。kernel会将开机信息存储在ring buffer中。您若是开机时来不及查看信息，可利用dmesg来查看。
开机信息保存在`/var/log/dmesg`文件里

```markdown
-C, --clear                 清除内核环形缓冲区(ring butter)
-c, --read-clear            读取并清除所有消息
-D, --console-off           禁止向终端打印消息
-d, --show-delta            显示打印消息之间的时间差
-e, --reltime               以易读格式显示本地时间和时间差
-E, --console-on            启用向终端打印消息
-F, --file <文件>           用 文件 代替内核日志缓冲区
-f, --facility <列表>       将输出限制为定义的设施
-H, --human                 易读格式输出
-k, --kernel                显示内核消息
-L, --color                 显示彩色消息
-l, --level <列表>          限制输出级别
-n, --console-level <级别>  设置打印到终端的消息级别
-P, --nopager               不将输出通过管道传递给分页程序
-r, --raw                   打印原生消息缓冲区
-S, --syslog                强制使用 syslog(2) 而非 /dev/kmsg
-s, --buffer-size <大小>    查询内核环形缓冲区所用的缓冲区大小
-T, --ctime                 显示易读的时间戳(如果您使用了
                            SUSPEND/RESUME 则可能不准)
-t, --notime                不打印消息时间戳
-u, --userspace             显示用户空间消息
-w, --follow                等待新消息
-x, --decode                将设施和级别解码为可读的字符串

支持的日志设施：
    kern - 内核消息
    user - 随机的用户级消息
    mail - 邮件系统
  daemon - 系统守护进程
    auth - 安全/认证消息
  syslog - syslogd 内部生成的消息
     lpr - 行打印机子系统
    news - 网络新闻子系统

支持的日志级别(优先级)：
   emerg - 系统无法使用
   alert - 操作必须立即执行
    crit - 紧急条件
     err - 错误条件
    warn - 警告条件
  notice - 正常但重要的条件
    info - 信息
   debug - 调试级别的消息

```

## 实例

```bash
dmesg | grep sda    # 查看硬盘基础信息
```
