# **sudo**

## 说明

**sudo命令**用来以其他身份来执行命令，预设身份为root。在`/etc/sudoers`中设置可执行sudo指令的用户。若其未经授权的用户企图
使用sudo，则会发出警告的邮件给管理员。用户使用sudo时，必须先输入密码，之后有5分钟的有效期限，超过期限则必须重新输入密码

## 选项

```markdown
sudo - 以其他用户身份执行一条命令

sudo -h | -K | -k | -V
sudo -v [-AknS] [-g group] [-h host] [-p prompt] [-u user]
sudo -l [-AknS] [-g group] [-h host] [-p prompt] [-U user] [-u user] [command]
sudo [-AbEHknPS] [-r role] [-t type] [-C num] [-g group] [-h host] [-p prompt] [-T timeout] [-u user] [VAR=value]
 [-i|-s] [<command>]
sudo -e [-AknS] [-r role] [-t type] [-C num] [-g group] [-h host] [-p prompt] [-T timeout] [-u user] file ...

-A, --askpass                 使用助手程序进行密码提示
-b, --background              在后台运行命令
-C, --close-from=num          关闭所有 >= num 的文件描述符
-E, --preserve-env            在执行命令时保留用户环境
    --preserve-env=list       保留特定的环境变量
-e, --edit                    编辑文件而非执行命令
-g, --group=group             以指定的用户组或 ID 执行命令
-H, --set-home                将 HOME 变量设为目标用户的主目录
-h, --help                    显示帮助消息并退出
-h, --host=host               在主机上运行命令(如果插件支持)
-i, --login                   以目标用户身份运行一个登录 shell；可同时指定一条命令
-K, --remove-timestamp        完全移除时间戳文件
-k, --reset-timestamp         无效的时间戳文件
-l, --list                    列出用户权限或检查某个特定命令；对于长格式，使用两次
-n, --non-interactive         非交互模式，不提示
-P, --preserve-groups         保留组向量，而非设置为目标的组向量
-p, --prompt=prompt           使用指定的密码提示
-r, --role=role               以指定的角色创建 SELinux 安全环境
-S, --stdin                   从标准输入读取密码
-s, --shell                   以目标用户运行 shell；可同时指定一条命令
-t, --type=type               以指定的类型创建 SELinux 安全环境
-T, --command-timeout=timeout 在达到指定时间限制后终止命令
-U, --other-user=user         在列表模式中显示用户的权限
-u, --user=user               以指定用户或 ID 运行命令(或编辑文件)
-V, --version                 显示版本信息并退出
-v, --validate                更新用户的时间戳而不执行命令
--                            停止处理命令行参数

```

## 实例

```bash
: << comment
配置sudo必须通过编辑`/etc/sudoers`文件，而且只有超级用户才可修改它，还必须使用visudo编辑。之所以使用visudo有两个原因，一
是能够防止两个用户同时修改；二是它也能进行有限的语法检查。所以，即使只有你一个超级用户，你也最好用visudo来检查一下语法

visudo默认的是在vi里打开配置文件，用vi来修改文件。我们可以在编译时修改这个默认项。visudo不会擅自保存带有语法错误的配置文
件，它会提示你出现的问题，并询问该如何处理

此时有三种选择：键入“e”重新编辑，键入“x”不保存退出，键入“Q”退出并保存。选择Q，那么sudo将不会再运行，直到错误被纠正
comment

# 日志与安全,sudo不仅可以记录日志，还能在有必要时向系统管理员报告。但sudo的日志功能不是自动的，必须由管理员开启
touch /var/log/sudo
# 编辑/etc/syslog.conf,在syslog.conf最后面添加如下一行内容（必须用tab分割开）并保存
local2.debug                    /var/log/sudo

# sudo记录日志并不是很完善,重定向没有被记录,但也有个好处，下面的手段不会得逞：
sudo ls /root > /etc/shadow     # 提示：bash: /etc/shadow: 权限不够

# sudo 有自己的方式来保护安全。以root的身份执行`sudo-V`，查看一下sudo的设置。因为考虑到安全问题，一部分环境变量并没有传
# 递给sudo后面的命令，或者被检查后再传递的，比如：PATH，HOME，SHELL等。当然，你也可以通过sudoers来配置这些环境变量
```
