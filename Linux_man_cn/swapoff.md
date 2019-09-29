# swapoff

## 说明

**swapoff命令** 用于关闭指定的交换空间（包括交换文件和交换分区）。swapoff实际上为swapon的符号连接，可用来关闭系统的交换区

## 选项

```markdown
-a：关闭配置文件“/etc/fstab”中所有的交换空间
```

## 实例

```bash
swapoff /dev/sda2   # 关闭交换分区

```


