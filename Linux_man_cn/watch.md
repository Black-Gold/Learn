# **watch**

## 说明

**watch命令** 以周期性的方式执行给定的指令，指令输出以全屏方式显示。watch是一个非常实用的命令，基本所有的Linux发行版都带
有这个小工具，如同名字一样，watch可以帮你监测一个命令的运行结果

```markdown
watch [options] command

-b, --beep             beep if command has a non-zero exit
-c, --color            interpret ANSI color and style sequences
-d, --differences[=<permanent>]   高亮显示变化的区域
   而-d=cumulative选项会把变动过的地方(不管最近的那次有没有变动)都高亮显示出来
-e, --errexit          exit if command has a non-zero exit
-g, --chgexit          exit when output from command changes
-n, --interval <secs>  缺省每2秒运行一次，-n可以指定间隔时间
-p, --precise          attempt run command in precise intervals
-t, --no-title         turn off header
-x, --exec             pass command to exec instead of "sh -c"

```

## 实例

```bash
watch -n 1 -d netstat -ant       # 命令：每隔一秒高亮显示网络链接数的变化情况
watch -n 1 -d 'pstree|grep http' # 每隔一秒高亮显示http链接数的变化情况。后面接的命令若带有管道符，需要加''将命令区域归整
watch 'netstat -an | grep:21 | \ grep<模拟攻击客户机的IP>| wc -l' # 实时查看模拟攻击客户机建立起来的连接数
watch -d 'ls -l|grep scf'       # 监测当前目录中 scf' 的文件的变化
watch -n 10 'cat /proc/loadavg' # 10秒一次输出系统的平均负载
watch -d -n 1 netstat -ntlp
watch -d 'ls -l | fgrep goface'     # 监测goface的文件
watch -t -differences=cumulative uptime
watch -n 60 from            # 监控mail
watch -n 1 "df -i;df"       # 监测磁盘inode和block数目变化情况
```

FreeBSD和Linux下watch命令的不同，在Linux下，watch是周期性的执行下个程序，并全屏显示执行结果,
如：`watch -n 1 -d netstat -ant`，而在FreeBSD下的watch命令是查看其它用户的正在运行的操作
watch允许你偷看其它terminal正在做什么，该命令只能让超级用户使用

```bash
watch -n 1 'cat /proc/interrupts'   # 检测文件/proc/interrupts的变化
```
