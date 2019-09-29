# swapon

## 说明

**swapon命令** 用于激活Linux系统中交换空间，Linux系统的内存管理必须使用交换区来建立虚拟内存

## 选项

```markdown
-a：将/etc/fstab文件中所有设置为swap的设备，启动为交换区
-h：显示帮助
-p<优先顺序>：指定交换区的优先顺序
-s：显示交换区的使用状况
-V：显示版本信息
```

## 实例

```bash
mkswap -c /dev/hdb4     # -c是检查有无坏块
swapon -v /dev/hdb4
swapon -s

```


