# **ps**

## 说明

**ps命令** 用于报告当前系统的进程状态。可以搭配kill指令随时中断、删除不必要的程序。ps命令是最基本同时也是非常强大的进程
查看命令，使用该命令可以确定有哪些进程正在运行和运行的状态、进程是否结束、进程有没有僵死、哪些进程占用了过多的资源等等,
总之大部分信息都是可以通过执行该命令得到的

```markdown
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
ps -aux | sort -nk +3 | tail    # 查看消耗CPU最多的十个进程
ps -aux | sort -nk +4 | tail    # 查看消耗内存最多的十个进程
ps -le
pstree | more   # 进程树，非常直观的观察父子进程
ps -eo pid,args,psr  # 查看进程在哪个CPU上运行
ps -p pid1,pid2 # 显示指定进程id的信息，此例为pid1，pid2进程的信息
ps -eo pid,args --forest    # 以树结构显示进程
ps aux | sort -nk 3   # 按CPU 资源的使用量对进程进行排序
ps -eo pcpu,cpu,nice,state,cputime,args --sort pcpu | sed '/^ 0.0 /d' # 以CPU占用率为序显示进程
ps -eo "%C  : %p : %z : %a" | sort  -nr # 按CPU利用率从大到小排序
ps -e -orss=,args= | sort -rb -k1,1n | pr -TW$COLUMNS    # 以内存使用量排序显示进程
ps aux | sort -rnk 4  # 按内存资源的使用量对进程进行排序
ps -eo "%C  : %p : %z : %a" | sort -k5 -nr # 按内存占用从大到小排序
ps -eo "%C%p%z%a"|sort -k3 -nr  # 进程按虚拟内存从大到小排列
ps -eo user,pid,size,pmem,vsize,command|sort -k4 -nr|more   # 按实际使用内存百分比排序
ps -eo rss,pmem,pcpu,vsize,args | sort -k 1 -r -n | less    # 按进程消耗内存多少排序
ps -auxww|awk '{print $5,$1,$11}'|sort -r|more  # 按照内存使用量从大到小排序
ps -C nginx -L -o pid,tid,pcpu,state    # 显示指定进程的所有线程信息
ps -aux --sort pid    # 可按照进程执行的时间，PID，UID等对进程进行排序
ps -uU tangsir / ps -aux | grep tangsir   # 查看系统中指定用户执行的进程
ps -u root | awk '/^test/ {print "kill -9" $1}' | sh     # 将用户root下所有进程名以test开头的全部强制杀死

# PHP-FPM进程的平均内存占用
ps --no-headers -o "rss,cmd" -C php-fpm | awk '{ sum+=$1 } END { printf ("%d%s\n", sum/NR/1024,"M") }'

# 统计僵尸进程数目
ps -ef | grep defunct | grep -v grep | wc -l
ps -eo ppid,stat | grep Z | wc -l

# 清理僵尸进程
ps -eal | awk '{ if ($2 == "Z") {print $4}}' | kill -9
ps -eo ppid,stat | grep Z | cut -d " " -f2 | xargs kill -9
kill -HUP `ps -A -ostat,ppid | grep -e '^[Zz]' | awk '{print $2}'`
ps -A -ostat,ppid | awk '/[zZ]/{print $2}'
kill $(ps -A -ostat,ppid | awk '/[zZ]/{print $2}' | sort -u)

: << comment
rss: resident set size, 表示进程占用RAM(内存)的大小，单位是KB
pmem: %M, 占用内存的百分比
pcpu：%C，占用cpu的百分比
vsize:表示进程占用的虚拟内存的大小，KB
comment

# java进程cpu占用过高排查
ps -mp pid -o THREAD,tid,time
printf "%x\n" tid   # 将需要的线程ID转换为16进制格式
jstack pid |grep tid -A 30  # 打印线程的堆栈信息

# java进程占用内存过高排查
jmap -histo:live [pid]  # 分析具体的对象数目和占用内存大小，从而定位代码
jmap -dump:live,format=b,file=xxx.hprof [pid]   # 利用MAT工具分析是否存在内存泄漏等
```

## linux进程5种状态

* 运行        (正在运行或在运行队列中等待)
* 中断        (休眠中, 受阻, 在等待某个条件的形成或接受到信号)
* 不可中断    (收到信号不唤醒和不可运行, 进程必须等待直到有中断发生)
* 僵死        (进程已终止, 但进程描述符存在, 直到父进程调用wait4()系统调用后释放)
* 停止        (进程收到SIGSTOP, SIGTSTP, SIGTTIN, SIGTTOU信号后停止运行运行)

ps命令标识进程的5种状态码

* D 不可中断   uninterruptible sleep (usually IO)
* R 运行      runnable (on run queue)
* S 中断      sleeping
* T 停止      traced or stopped
* Z 僵死      a defunct (”zombie”) process
