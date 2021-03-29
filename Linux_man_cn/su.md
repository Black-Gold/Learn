# **su**

## 说明

**su命令** 用于切换当前用户身份到其他用户身份，变更时须输入所要变更的用户帐号与密码

```markdown
su [选项] [-] [USER [参数]...]

将有效用户id和组id更改为USER的id。单个 - 视为 -l。如果未指定USER，将假定为root

-m, -p, --preserve-environment  不重置环境变量
-g, --group <组>             指定主组
-G, --supp-group <组>        指定一个辅助组

-, -l, --login                  使 shell 成为登录 shell
-c, --command <命令>            使用 -c 向 shell 传递一条命令
--session-command <命令>        使用 -c 向 shell 传递一条命令
                                而不创建新会话
-f, --fast                      向shell 传递 -f 选项(csh 或 tcsh)
-s, --shell <shell>             若 /etc/shells 允许，则运行 shell

```

## 实例

```bash
su -c ls root   # 变更帐号为root并在执行ls指令后退出变回原使用者
su root -f      # 变更帐号为root并传入`-f`选项给新执行的shell
su -test        # 变更帐号为test并改变工作目录至test的家目录
```
