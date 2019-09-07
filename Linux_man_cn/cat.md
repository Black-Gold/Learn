# **cat**

```markdown
将[文件]或标准输入组合输出到标准输出
-A, --show-all           等于-vET,显示不可打印字符，行尾显示“$”
-b, --number-nonblank    对非空输出行编号
-e                       等于-vE
-E, --show-ends          在每行结束处显示"$"
-n, --number             对输出的所有行编号
-s, --squeeze-blank      不输出多行空行,连续两行以上的空白行，以一行空白行代替
-t                       与-vT等价
-T, --show-tabs          将跳格字符显示为^I
-u                       (被忽略)
-v, --show-nonprinting   使用^ 和M- 引用，除了LFD和 TAB 之外

如果没有指定文件，或者文件为"-"，则从标准输入读取
```

## 实例

```bash
cat -n /etc/passwd | sed '2,5d' # 显示passwd内容，将2-5行删除后再显示
cat -n /etc/passwd | sed '2a hello' # 在passwd文件第二行后加上hello语句
cat -n /etc/passwd | sed '2a hello? \ zhangfneg ?'  # 在passwd文件第二行后面加上两行字
cat -n /etc/passwd  | sed '3,37c我是好人'   # 将2至5行内容替换成我是好人
cat -n /etc/passwd | sed -n '5,7p'  # 只显示5至7行
cat /var/log/secure | sed -n '/12:12:50/,/12:13:50/p'   # 分析secure日志
cat /proc/partitions    # 显示所在系统注册的分区
```