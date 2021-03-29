# **nohup**

## 说明

**nohup命令** 可以将程序以忽略挂起信号的方式运行起来，被运行的程序的输出信息将不会显示到终端

无论是否将 nohup 命令的输出重定向到终端，输出都将附加到当前目录的 nohup.out 文件中。如果当前目录的 nohup.out 文件不可写，输出重定向
到`$HOME/nohup.out`文件中。如果没有文件能创建或打开以用于追加，那么 command 参数指定的命令不可调用。如果标准错误是一个终端，那么把
指定的命令写给标准错误的所有输出作为标准输出重定向到相同的文件描述符

```markdown
If standard input is a terminal, redirect it from /dev/null
If standard output is a terminal, append output to 'nohup.out' if possible,'$HOME/nohup.out' otherwise
If standard error is a terminal, redirect it to standard output
To save output to FILE, use 'nohup COMMAND > FILE
```

## 实例

```bash
nohup command > myout.file 2>&1 &
```
