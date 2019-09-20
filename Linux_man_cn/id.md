# **id**

## 说明

**id命令** 可以显示真实有效的用户ID(UID)和组ID(GID)。UID 是对一个用户的单一身份标识。组ID（GID）则对应多个UID。id命令已经默认预装
在大多数Linux系统中。要使用它，只需要在你的控制台输入id。不带选项输入id会显示如下。结果会使用活跃用户

当我们想知道某个用户的UID和GID时id命令是非常有用的。一些程序可能需要UID/GID来运行。id使我们更加容易地找出用户的UID以GID而不必在
`/etc/group`文件中搜寻。如往常一样，你可以在控制台输入`man id`进入id的手册页来获取更多的详情

## 选项

```markdown
-a             ignore, for compatibility with other versions
-Z, --context  print only the security context of the current user
-g, --group    仅打印有效的组ID
-G, --groups   print all group IDs
-n, --name     print a name instead of a number, for -ugG
-r, --real     print the real ID instead of the effective ID, with -ugG
-u, --user     print only the effective user ID
-z, --zero     delimit entries with NUL characters, not whitespace;not permitted in default format

如果不附带任何选项，程序会显示一些可供识别用户身份的有用信息
```

## 实例

```bash
id

```


