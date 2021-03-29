# **head**

```markdown
用法：head [选项]... [文件]...
Print the first 10 lines of each FILE to standard output
With more than one FILE, precede each with a header giving the file name
With no FILE, or when FILE is -, read standard input

-c, --bytes=[-]K         打印每个文件的前K个字节；以'-'开头，打印每个文件中除最后K个字节以外的所有字节
-n, --lines=[-]K         打印前K行而不是前10行；带前缀'-'并打印每个文件中除最后K行外的所有行
-q, --quiet, --silent    不显示包含给定文件名的文件头
-v, --verbose            总是显示包含给定文件名的文件头

K 后面可以跟乘号:
b 512, kB 1000, K 1024, MB 1000*1000, M 1024*1024,
GB 1000*1000*1000, G 1024*1024*1024, 对于T, P, E, Z, Y 同样适用
```

## 实例

```bash
head -1 file    # 显示file文件第一行
head -n1 /etc/issue # 查看操作系统版本,不一定每个系统都能看到
head -c 10MB /dev/zero > daygeek4.txt   # 创建10M大小的文件
```
