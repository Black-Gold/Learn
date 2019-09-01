# **pmap**

## 说明

**pmap命令** 用于报告进程的内存映射关系，是Linux调试及运维一个很好的工具

## 选项

```markdown
pmap [options] PID [PID ...]

Options:
 -x, --extended              显示详细信息
 -X                          显示比-x更为详细的信息；WARNING: format changes according to /proc/PID/smaps
 -XX                         show everything the kernel provides
 -c, --read-rc               read the default rc
 -C, --read-rc-from=<file>   read the rc from file
 -n, --create-rc             create new default rc
 -N, --create-rc-to=<file>   create new rc to file；NOTE: pid arguments are not allowed with -n, -N
 -d, --device                显示设备格式
 -q, --quiet                 不显示头尾行
 -p, --show-path             show path in the mapping
 -A, --range=<low>[,<high>]  limit results to the given range
```

## 实例

```bash
pmap PID    # 分析进程号PID的内存线程栈
```


