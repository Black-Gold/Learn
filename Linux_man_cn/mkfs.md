# **mkfs**

## 说明

**mkfs命令** 用于在设备上（通常为硬盘）创建Linux文件系统。mkfs本身并不执行建立文件系统的工作，而是去调用相关的程序来执行

## 选项

```markdown
mkfs [选项] [-t <类型>] [文件系统选项] <设备> [<大小>]

-t, --type=<类型>  文件系统类型；若不指定，将使用 ext2
    fs-options     实际文件系统构建程序的参数
    <设备>         要使用设备的路径
    <大小>         要使用设备上的块数
-V, --verbose      解释正在进行的操作；多次指定 -V 将导致空运行(dry-run)
-V, --version      显示版本信息并退出,将 -V 作为 --version 选项时必须是惟一选项

```

## 实例

```bash
mkfs -t ext3 /dev/sda6     # 将sda6分区格式化为ext3格式
mkfs -t ext2 /dev/sda7     # 将sda7分区格式化为ext2格式
```


