# logger

## 说明

**logger命令** 是用于往系统中写入日志，他提供一个shell命令接口到syslog系统模块

## 选项

```markdown
-T, --tcp             只使用 TCP
-d, --udp             只使用 UDP
-i, --id              同时记录进程 ID
-f, --file <文件>     记录此文件的内容
-h, --help            显示此帮助并退出
-S, --size <num>      maximum size for a single message (default 1024)
-n, --server <name>   write to this remote syslog server
-P, --port <port>     use this port for UDP or TCP connection
-p, --priority <prio> mark given message with this priority
-s, --stderr          output message to standard error as well
-t, --tag <标志>      用此标志标记每一行
-u, --socket <套接字> 写入此 Unix 套接字

```

## 实例

```bash
logger -p syslog.info "backup.sh is starting"
```



