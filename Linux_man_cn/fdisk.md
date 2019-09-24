# **fdisk**

## 说明

**fdisk命令** 用于观察硬盘实体使用情况，也可对硬盘分区。它采用传统的问答式界面，而非类似DOSfdisk的cfdisk互动式操作界面，
因此在使用上较为不便，但功能却丝毫不打折扣

## 选项

```markdown
fdisk [选项] <磁盘>    更改分区表
fdisk [选项] -l <磁盘> 列出分区表
fdisk -s <分区>        给出分区大小(块数)

 -b <大小>             扇区大小(512、1024、2048或4096)
 -c[=<模式>]           兼容模式：“dos”或“nondos”(默认)
 -h                    打印此帮助文本
 -u[=<单位>]           显示单位：“cylinders”(柱面)或“sectors”(扇区，默认)
 -v                    打印程序版本
 -C <数字>             指定柱面数
 -H <数字>             指定磁头数
 -S <数字>             指定每个磁道的扇区数

```

## 实例

```bash
e2fsck -f -y -v -C 0 '/dev/sdb2'
resize2fs -p '/dev/sdb2' 15171584k
mkfs.ext4 -F -O ^64bit -L 'data' '/dev/sdb3'
```
