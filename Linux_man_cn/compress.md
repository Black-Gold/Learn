# compress

## 说明

**compress命令** 使用“Lempress-Ziv”编码压缩数据文件。compress是个历史悠久的压缩程序，文件经它压缩后，其名称后面会多出".Z"的扩展名。
当要解压缩时，可执行uncompress指令。事实上uncompress是指向compress的符号连接，因此不论是压缩或解压缩，都可通过compress指令单独完成

## 选项

```markdown
-f：不提示用户，强制覆盖掉目标文件
-c：将结果送到标准输出，无文件被改变
-r：递归的操作方式
-b<压缩效率>：压缩效率是一个介于9~16的数值，预设值为"16"，指定愈大的数值，压缩效率就愈高
-d：对文件进行解压缩而非压缩
-v：显示指令执行过程
-V：显示指令版本及程序预设值
```

## 实例

```bash
compress -d man.config.Z    # 解压
compress -c man.config > man.config.back.Z  # 将man.config压缩成另外一个文件来备份
```


