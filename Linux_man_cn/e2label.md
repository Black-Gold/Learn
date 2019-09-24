# e2label

## 说明

**e2label命令** 用来修改ext2/ext3/ext4文件系统的卷标

## 选项

```markdown
e2label device [ new-label ]

若new-label可选参数未指定则只是查看对应设备的卷标，指定的卷标最多可以包含16个字符； 如果new-label的长度超过16个字符，
则e2label将截断它并打印一个警告信息
```

## 实例

```bash
e2lable /dev/sdb1   # 查看分区的卷标
e2lable /dev/sdb1 network   # 设置分区的卷标

```
