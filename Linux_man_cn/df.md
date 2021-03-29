# **df**

## 说明

**df命令** 用于显示磁盘分区上的可使用的磁盘空间。默认显示单位为KB。可以利用该命令来获取硬盘占用空间等信息

```markdown
-a, --all              包含全部的文件系统
-B, --block-size=SIZE  在打印之前按size调整大小; 例如:'- BM'以1048576字节为单位打印size;请参阅下面的SIZE格式
    --direct           show statistics for a file instead of mount point
    --total            produce a grand total
-h, --human-readable   以可读性较高的方式来显示信息(e.g., 1K 234M 2G)
-H, --si               与-h参数相同，但在计算时是以1000 Bytes为换算单位而非1024 Bytes
-i, --inodes            显示inode 信息而非块使用量
-k                      即--block-size=1K
-l, --local           只显示本机的文件系统
    --no-sync         取得使用量数据前不进行同步动作(默认)
    --output[=FIELD_LIST]  use the output format defined by FIELD_LIST,
                             or print all fields if FIELD_LIST is omitted.
-P, --portability      使用POSIX的输出格式
    --sync             invoke sync before getting usage info
-t, --type=TYPE        仅显示指定文件系统类型的磁盘信息
-T, --print-type       显示文件系统的类型
-x, --exclude-type=TYPE   不显示指定文件系统类型的磁盘信息
```

## 实例

```bash
df  # 查看系统磁盘设备，默认是KB为单位
```
