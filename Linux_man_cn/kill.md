# **kill**

## 说明

**kill命令** 用来删除执行中的程序或工作。kill可将指定的信息送至程序。预设的信息为SIGTERM(15),可将指定程序终止。若仍无法
终止该程序，可使用SIGKILL(9)信息尝试强制删除程序。程序或工作的编号可利用ps指令或job指令查看

```markdown
-a：当处理当前进程时，不限制命令名和进程号的对应关系
-l <信息编号>：若不加<信息编号>选项，则-l参数会列出全部的信息名称
-L, --table List signal names in a nice table
-p：指定kill 命令只打印相关进程的进程号，而不发送任何信号
-s <信息名称或编号>：指定要送出的信息
-u：指定用户
```

## 实例

```markdown
# 列出所有信号名称
 kill -l
 1) SIGHUP       2) SIGINT       3) SIGQUIT      4) SIGILL
 2) SIGTRAP      6) SIGABRT      7) SIGBUS       8) SIGFPE
 3) SIGKILL     10) SIGUSR1     11) SIGSEGV     12) SIGUSR2
1)  SIGPIPE     14) SIGALRM     15) SIGTERM     16) SIGSTKFLT
2)  SIGCHLD     18) SIGCONT     19) SIGSTOP     20) SIGTSTP
3)  SIGTTIN     22) SIGTTOU     23) SIGURG      24) SIGXCPU
4)  SIGXFSZ     26) SIGVTALRM   27) SIGPROF     28) SIGWINCH
5)  SIGIO       30) SIGPWR      31) SIGSYS      34) SIGRTMIN
6)  SIGRTMIN+1  36) SIGRTMIN+2  37) SIGRTMIN+3  38) SIGRTMIN+4
7)  SIGRTMIN+5  40) SIGRTMIN+6  41) SIGRTMIN+7  42) SIGRTMIN+8
8)  SIGRTMIN+9  44) SIGRTMIN+10 45) SIGRTMIN+11 46) SIGRTMIN+12
9)  SIGRTMIN+13 48) SIGRTMIN+14 49) SIGRTMIN+15 50) SIGRTMAX-14
10) SIGRTMAX-13 52) SIGRTMAX-12 53) SIGRTMAX-11 54) SIGRTMAX-10
11) SIGRTMAX-9  56) SIGRTMAX-8  57) SIGRTMAX-7  58) SIGRTMAX-6
12) SIGRTMAX-5  60) SIGRTMAX-4  61) SIGRTMAX-3  62) SIGRTMAX-2
13) SIGRTMAX-1  64) SIGRTMAX


只有第9种信号(SIGKILL)才可以无条件终止进程，其他信号进程都有权利忽略，下面是常用的信号：

HUP     1    终端断线
INT     2    中断（同 Ctrl + C）
QUIT    3    退出（同 Ctrl + \）
TERM   15    终止
KILL    9    强制终止
CONT   18    继续（与STOP相反， fg/bg命令）
STOP   19    暂停（同 Ctrl + Z）
```

```bash

```
