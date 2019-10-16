# **basename**

## 说明

**basename命令** 用于打印目录或者文件的基本名称。basename和dirname命令通常用于shell脚本中的命令替换来指定和指定的输入文件名称有所差异
的输出文件名称

## 选项

```markdown
-a, --multiple       support multiple arguments and treat each as a NAME
-s, --suffix=SUFFIX  remove a trailing SUFFIX
-z, --zero           separate output with NUL rather than newline

```

## 实例

```bash
basename $WORKFILE  # 显示一个shell变量的基本名称
basename /usr/bin/sort          # 输出 "sort"
basename include/stdio.h .h     # 输出 "stdio"
basename -s .h include/stdio.h  # 输出 "stdio"
basename -a any/str1 any/str2   # 输出 "str1" followed by "str2"
```
