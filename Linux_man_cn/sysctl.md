# **sysctl**

## 说明

**sysctl命令** 被用于在内核运行时动态地查看修改内核的运行参数，可用的内核参数在目录`/proc/sys`中。它包含一些TCP/ip堆栈和虚拟内存系统
的高级选项

## 选项

```markdown
-a, --all            显示当前所有可用的内核参数变量和值
-A                   alias of -a(但以表格方式显示)
-X                   alias of -a
    --deprecated     include deprecated parameters to listing
-b, --binary         print value without new line
-e, --ignore         ignore unknown variables errors
-N, --names          print variable names without values
-n, --values         print only values of a variables
-p, --load[=<file>]  read values from file
-f                   alias of -p
    --system         read values from all system directories
-r, --pattern <expression>  select setting that match expression
-q, --quiet          do not echo variable set
-w, --write          enable writing a value to variable;当改变sysctl设置时使用此项
-o                   does nothing
-x                   does nothing
-d                   alias of -h

```

## 实例

```bash

sysctl -a   # 查看所有可读内核变量
sysctl net.nf_conntrack_max  # 读取一个指定的变量，例如net.nf_conntrack_max
sysctl net.nf_conntrack_max=262144  # 要设置一个指定的变量，直接用variable=value,但并不是所有的变量都可以在这个模式下设定

```
