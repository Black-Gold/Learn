# ipcs

## 说明

**ipcs命令**分析消息队列共享内存和信号量,用于报告Linux中进程间通信设施的状态，显示的信息包括消息列表、共享内存和信号量的信息。

## 选项

```markdown
选项：
 -i, --id <id>  打印由 id 标识的资源的详细信息
 -h, --help     显示此帮助并退出
 -V, --version  输出版本信息并退出

资源选项：
 -m, --shmems      显示共享内存段信息
 -q, --queues      显示消息队列
 -s, --semaphores  显示信号量
 -a, --all         全部(默认)

输出格式：
 -t, --time        显示附加、脱离和更改时间
 -p, --pid         显示 PID 的创建者和最后操作
 -c, --creator     显示创建者和拥有者
 -l, --limits      显示资源限制
 -u, --summary     显示状态摘要
     --human       以易读格式显示大小
 -b, --bytes       以字节数显示大小

```

## 实例

```bash
# 查看IPC资源被谁占用，假设有个IPCKEY为51036需要查询是否被占用
echo "obase=16;51036" | bc  # 利用bc首先将51036十进制数字转换为16进制得到c75c
ipcs -m | grep c75c

```


