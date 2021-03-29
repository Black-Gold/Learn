# **dirname**

## 说明

**dirname命令** 去除文件名中的非目录部分，仅显示与目录有关的内容。dirname命令读取指定路径名保留最后一个`/`及其后面的字符，删除其他部分，并写结果到标准输出。如果最后一个`<cite>/</cite>`后无字符，dirname 命令使用倒数第二个`/`，并忽略其后的所有字符。dirname 和 basename 通常在 shell 内部命令替换使用，以指定一个与指定输入文件名略有差异的输出文件名

```markdown
-z, --zero     每行以斜杠/结束，而不是换行符
```

## 实例

```bash
dirname //  # 输出为 /
dirname /a/b/   # 输出为 /a
dirname a   # 输出为 .
dirname a/b # 输出为路径名 a

dirname dir1/str dir2/str
: << comment
# 输出为：
dir1
dir2
comment
```
