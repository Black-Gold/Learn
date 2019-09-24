# **top**

## 说明

**top命令** 可以实时动态地查看系统的整体运行情况，是一个综合了多方信息监测系统性能和运行信息的实用工具。通过top命令所提
供的互动式界面，用热键可以管理

## 选项

```markdown
-b          以批处理模式操作
-c          显示完整的治命令
-d          屏幕刷新间隔时间
-I          忽略失效过程
-s          保密模式
-S          累积模式
-i<时间>    设置间隔时间
-u<用户名>  指定用户名
-p<进程号>  指定进程
-n<次数>    循环显示的次数
-k          关闭指定进程号
```

## top交互命令

在top命令执行过程中可以使用的一些交互命令。这些命令都是单字母的，如果在命令行中使用了-s选项， 其中一些命令可能会被屏蔽

```markdown
h                   帮助命令
q                   退出程序
k                   杀死一个进程
<space>(空格按键)   立即刷新
s                   改变两次刷新之间的延迟时间（单位为s），如果有小数，就换算成ms。输入0值则系统将不断刷新，默认值是5s
S                   切换到累计模式
c                   切换显示命令名称和完整命令行
t                   切换显示进程和CPU状态信息
m                   切换显示内存信息
l                   切换显示平均负载和启动时间信息
f或者F              从当前显示中添加或者删除项目
o或者O              改变显示项目的顺序
P                   根据CPU使用百分比大小进行排序
i                   忽略闲置和僵死进程，这是一个开关式命令，即只显示正在运行的进程
r                   修改一个进程的优先级别即renice值
M                   根据驻留内存大小进行排序
T                   根据时间/累计时间进行排序
w                   将当前设置写入~/.toprc文件中
```

## 实例

```markdown
top - 09:44:56 up 16 days, 21:23,  1 user,  load average: 9.59, 4.75, 1.92
Tasks: 145 total,   2 running, 143 sleeping,   0 stopped,   0 zombie
%Cpu(s):  0.1 us,  0.0 sy,  0.0 ni, 99.8 id,  0.0 wa,  0.0 hi,  0.0 si,  0.0 st
Mem:   4147888k total,  2493092k used,  1654796k free,   158188k buffers
Swap:  5144568k total,  1245456k used,  5144512k free,  2013180k cached
```

```markdown
# 输出解释
top - 09:44:56  当前系统时间
16 days         系统已经运行了16天
1 user          1个用户当前登录
load average: 9.59, 4.75, 1.92    系统负载，即任务队列的平均长度，此处是1分钟，5分钟，10分钟的平均负载
Tasks: 145 total    总进程数
2 running           正在运行的进程数
143 sleeping        睡眠的进程数
0 stopped           停止的进程数
0 zombie            冻结进程数

Cpu(s): Linux使用nice值来确定进程的优先级，显示在各项任务上花费的CPU时间百分
0.1 us, user    CPU花费在用户空间执行进程的时间占用百分比--(time running un-niced user processes)
0.1 sy, system  CPU在内核空间执行进程所花费的时间百分比--(time running kernel processes)
0.0 ni, nice    用户进程空间内改变过优先级的进程占用CPU百分比--(time running niced user processes)
0.2 id, idle    空闲CPU百分比--(time spent in the kernel idle handler)
0.0 wa, IO-wait 等待输入输出(I/O)的CPU时间百分比--(time waiting for I/O completion)
0.0 hi          处理硬件中断所花费时间的百分比--(time spent servicing hardware interrupts)
0.0 si          处理软件中断所花费时间的百分比--(time spent servicing software interrupts)
0.0 st          虚拟化环境中，部分CPU资源提供给虚拟机，操作系统检测是否有任务执行，但由于忙于其他VM，因此无法执行他们，
                以此方损失的时间占用的百分比叫st--(time stolen from this vm by the hypervisor)

Mem: 4147888k total     物理内存总量
2493092k used           使用的物理内存总量
1654796k free           空闲内存总量
158188k buffers         用作内核缓存的内存量
Swap:  5144568k total  交换区总量
1215456k used           使用的交换区总量
5144512k free           空闲交换区总量
2013180k cached         缓冲的交换区总量

PID         进程ID
USER        进程所有者
PR          进程优先级，越小越先被执行
NI          nice值
VIRT        进程占用的虚拟内存
RES         进程占用的物理内存
SHR         进程使用的共享内存
S           进程的状态，S：休眠；R：运行；Z：僵尸进程；N：进程优先级值为负数
%CPU        进程占用CPU的使用率
%MEM        进程使用的物理内存和总内存百分比
TIME+       进程启动占用的总CPU时间，即占用CPU使用时间的累加值
COMMAND     进程启动命令名称

1. R 运行 runnable (on run queue)#运行(正在运行或在运行队列中等待)
2. S 中断 sleeping#中断(休眠中, 受阻, 在等待某个条件的形成或接受到信号)
3. D 不可中断 uninterruptible sleep (usually IO)#不可中断(收到信号不唤醒和不可运行, 进程必须等待直到有中断发生)
4. Z 僵死 a defunct (”zombie”) process#僵死(进程已终止, 但进程描述符存在, 直到父进程调用wait4()系统调用后释放)
5. T 停止 traced or stopped#停止(进程收到SIGSTOP, SIGSTP, SIGTIN, SIGTOU信号后停止运行运行)

```

```bash
top -d 1 -n 1 -b |awk -F '[ ,.%k]+' '/^Cpu/{printf "UPU_USAGE %.f%%\t",100-$11}/^Mem/\
{printf "MEM_USAGE %.f%%\n",($4-$8)/$2*100}'

top -d 1 -n 1 -b |awk -F '[ ,.%k]+' '/^Cpu/{printf "CPU_USAGE %.f%%\t",100-$11}/^Mem/\
{printf "MEM_USAGE %.f%%\t",($4-$8)/$2*100;now=strftime("%D %T");print now}'

```
