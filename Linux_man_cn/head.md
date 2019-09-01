# **head**

```markdown
用法：head [选项]... [文件]...
Print the first 10 lines of each FILE to standard output.
With more than one FILE, precede each with a header giving the file name.
With no FILE, or when FILE is -, read standard input.

Mandatory arguments to long options are mandatory for short options too.
  -c, --bytes=[-]K         print the first K bytes of each file;
                             with the leading '-', print all but the last
                             K bytes of each file
  -n, --lines=[-]K         print the first K lines instead of the first 10;
                             with the leading '-', print all but the last
                             K lines of each file
  -q, --quiet, --silent	不显示包含给定文件名的文件头
  -v, --verbose		总是显示包含给定文件名的文件头

K 后面可以跟乘号:
b 512, kB 1000, K 1024, MB 1000*1000, M 1024*1024,
GB 1000*1000*1000, G 1024*1024*1024, 对于T, P, E, Z, Y 同样适用
```

## 实例

```bash
head -1 file    # 显示file文件第一行

```