# **w**

## 说明

**w命令** 用于显示已经登陆系统的用户列表，并显示用户正在执行的指令。执行这个命令可得知目前登入系统的用户有那些人，以及他们正在执行的程序
单独执行w命令会显示所有的用户，您也可指定用户名称，仅显示某位用户的相关信息

## 选项

```markdown
-h, --no-header     不打印头信息
-u, --no-current    ignore current process username
-s, --short         short format
-f, --from          show remote hostname field
-o, --old-style     old style output
-i, --ip-addr       display IP address instead of hostname (if possible)

```

## 实例

```bash
w
: << comment
 20:59:50 up 60 days,  6:58,  2 users,  load average: 0.05, 0.04, 0.05
USER     TTY      FROM             LOGIN@   IDLE   JCPU   PCPU WHAT

Load average    分别显示系统在过去的1,5,15分钟内的平均负载程序
USER            登陆用户
TTY             登陆终端，是本地登陆还是远程登陆（pts/0,1,2,3）
FROM            显示用户从何处登陆系统，如果显示“:0”显示代表了该用户是从Xwindows下，打开文本模式窗口登陆的
IDLE            用户闲置的时间，这是一个计时器，一旦用户执行任何操作，该计时器便会被重置
JCPU            以终端代号来区分，该终端所有相关的进程执行时，所消耗的CPU时间会显示在这里
PCPU            CPU执行程序耗费的时间
WHAT            用户正在执行的操作
comment


```


