# **chown**

## 说明

**chown命令** 改变某个文件或目录的所有者和所属的组，该命令可以向某个用户授权，使该用户变成指定文件的所有者或者改变文件所
属的组。用户可以是用户或者是用户D，用户组可以是组名或组id。文件名可以使由空格分开的文件列表，在文件名中可以包含通配符

只有文件属主和超级用户才可以便用该命令

## 选项

```markdown
用法：chown [选项]... [所有者][:[组]] 文件...
　或：chown [选项]... --reference=参考文件 文件...
Change the owner and/or group of each FILE to OWNER and/or GROUP.
With --reference, change the owner and group of each FILE to those of RFILE.

-c, --changes          和-v选项类似，但值打印更改的部分
-f, --silent, --quiet  禁止显示错误信息
-v, --verbose          显示每个文件执行过程
    --dereference      影响每个符号链接的引用（这是默认值），而不是符号链接本身，和-h选项相同
-h, --no-dereference   只对符号连接的文件作修改，而不更改其他任何相关文件，即影响符号链接而不是任何引用的文件
                （仅在可以更改符号链接的所有权的系统上有用）
    --from=当前所有者:当前所属组
                只当每个文件的所有者和组符合选项所指定时才更改所有者和组。其中一个可以省略，这时已省略的属性就不
				需要符合原有的属性
    --no-preserve-root  do not treat '/' specially (the default)
    --preserve-root    fail to operate recursively on '/'
    --reference=RFILE  使用RFILE的所有者和组，而不是指定OWNER：GROUP值 
-R, --recursive        对文件和目录递归处理

指定了-R选项时，以下选项将修改遍历层次的方式，如果制定了多个，只有最后一个生效

-H      如果命令行参数是目录的符号链接，则遍历它 
-L      遍历目录下的没一个符号链接 
-P      不遍历任何符号链接(默认)

Owner is unchanged if missing.  Group is unchanged if missing, but changed
to login group if implied by a ':' following a symbolic OWNER.
OWNER and GROUP may be numeric as well as symbolic.



```

## 实例

```bash
chown root /u		    # 将 /u 的属主更改为"root"
chown root:staff /u	    # 和上面类似，但同时也将其属组更改为"staff"
chown -hR root /u	    # 将 /u 及其子目录下所有文件的属主更改为"root"
```
