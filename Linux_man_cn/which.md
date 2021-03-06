# **which**

## 说明

**which命令** 用于查找并显示给定命令的绝对路径，环境变量PATH中保存了查找命令时需要遍历的目录。which指令会在环境变量$PATH设置的目录里
查找符合条件的文件。也就是说，使用which命令，就可以看到某个系统命令是否存在，以及执行的到底是哪一个位置的命令



```markdown
--skip-dot       Skip directories in PATH that start with a dot
--skip-tilde     Skip directories in PATH that start with a tilde
--show-dot       Don't expand a dot to current directory in output
--show-tilde     Output a tilde for HOME directory for non-root
--tty-only       Stop processing options on the right if not on tty
--all, -a        输出所有在PATH匹配的可执行文件
--read-alias, -i Read list of aliases from stdin
--skip-alias     Ignore option --read-alias; don't read stdin
--read-functions Read shell functions from stdin
--skip-functions Ignore option --read-functions; don't read stdin
```

## 实例

```bash
# 说明：which是根据使用者所配置的 PATH 变量内的目录去搜寻可运行档的！所以，不同的PATH配置内容所找到的命令不一样！

which cd    # 用 which 去找出 cd

```
