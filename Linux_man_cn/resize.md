# resize

## 说明

**resize命令** 命令设置终端机视窗的大小。执行resize指令可设置虚拟终端机的视窗大小

## 选项

```markdown
-c 　就算用户环境并非C Shell，也用C Shell指令改变视窗大小
-s <列数> <行数> 　设置终端机视窗的垂直高度和水平宽度
-u 　就算用户环境并非Bourne Shell，也用Bourne Shell指令改变视窗大小
```

## 实例

```bash
resize -c   # 使用 C shell
resize -u   # 使用 Bourne shell
resize -s 80 160    # 设置指定大小

```



