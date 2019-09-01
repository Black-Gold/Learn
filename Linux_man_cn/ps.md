# **ps**

## 说明

**ps命令** 用于报告当前系统的进程状态。可以搭配kill指令随时中断、删除不必要的程序。ps命令是最基本同时也是非常强大的进程
查看命令，使用该命令可以确定有哪些进程正在运行和运行的状态、进程是否结束、进程有没有僵死、哪些进程占用了过多的资源等等,
总之大部分信息都是可以通过执行该命令得到的。

## 选项

Usage: ps [options]

```sh
基本选项
-A, -e               all processes
-a                   all with tty, except session leaders
 a                   all with tty, including other users
-d                   除了sessions之外的所有进程
-N, --deselect       negate selection(显示所有的程序，除了执行ps指令终端机下的程序之外)
 r                   only running processes
 T                   all processes on this terminal
 x                   processes without controlling ttys

Selection by list:
-C <command>         command name
-G, --Group <GID>    real group id or name
-g, --group <group>  session or effective group name
-p, p, --pid <PID>   process id
       --ppid <PID>  parent process id
-q, q, --quick-pid <PID>
                     process id (quick mode)
-s, --sid <session>  session id
-t, t, --tty <tty>   terminal
-u, U, --user <UID>  effective user id or name
-U, --User <UID>     real user id or name
 The selection options take as their argument either:
   a comma-separated list e.g. '-u root,nobody' or
   a blank-separated list e.g. '-p 123 4567'

Output formats:
-F                   extra full
-f                   full-format, including command lines
 f, --forest         ascii art process tree
-H                   show process hierarchy
-j                   jobs format
 j                   BSD job control format
-l                   long format
 l                   BSD long format
-M, Z                add security data (for SELinux)
-O <format>          preloaded with default columns
 O <format>          as -O, with BSD personality
-o, o, --format <format>
                     user-defined format
 s                   signal format
 u                   user-oriented format
 v                   virtual memory format
 X                   register format
-y                   do not show flags, show rss vs. addr (used with-l)
    --context        display security context (for SELinux)
    --headers        repeat header lines, one per page
    --no-headers     do not print header at all
    --cols, --columns, --width <num>
                     set screen width
    --rows, --lines <num>
                     set screen height

Show threads:
 H                   as if they were processes
-L                   possibly with LWP and NLWP columns
-m, m                after processes
-T                   possibly with SPID column

Miscellaneous options:
-c                   show scheduling class with -l option
 c                   show true command name
 e                   show the environment after command
 k,    --sort        specify sort order as: [+|-]key[,[+|-]key[,...]]
 L                   show format specifiers
 n                   display numeric uid and wchan
 S,    --cumulative  include some dead child process data
-y                   do not show flags, show rss (only with -l)
-V, V, --version     display version information and exit
-w, w                unlimited output width
       --help <simple|list|output|threads|misc|all>
                     display help and exit
```

## 实例

```bash
ps aux | sort -rnk 4  # 按内存资源的使用量对进程进行排序
ps aux | sort -nk 3   # 按CPU 资源的使用量对进程进行排序
ps -le or ps -aux     # 查看所有用户执行的进程的详细信息
ps -aux --sort pid    # 可按照进程执行的时间，PID，UID等对进程进行排序
ps -uU tangsir / ps -aux | grep tangsir   # 查看系统中指定用户执行的进程
pstree | more   # 进程树，非常直观的观察父子进程
ps --no-headers -o "rss,cmd" -C php-fpm | awk '{ sum+=$1 } END { printf ("%d%s\n", sum/NR/1024,"M") }'  # PHP-FPM进程的平均内存占用
ps -u root | awk '/^test/ {print "kill -9" $1}' | sh     # 将用户root下所有进程名以test开头的全部强制杀死

```
