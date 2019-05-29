useradd
===

创建的新的系统用户

## 补充说明

**useradd命令** 用于Linux中创建的新的系统用户。useradd可用来建立用户帐号。帐号建好之后，再用passwd设定帐号的密码．而可用userdel删除帐号。使用useradd指令所建立的帐号，实际上是保存在`/etc/passwd`文本文件中。

在Slackware中，adduser指令是个script程序，利用交谈的方式取得输入的用户帐号资料，然后再交由真正建立帐号的useradd命令建立新用户，如此可方便管理员建立用户帐号。在Red Hat Linux中， **adduser命令** 则是useradd命令的符号连接，两者实际上是同一个指令。

### 语法  

```
useradd(选项)(参数)
```

  

```

eradd [选项] 登录
      useradd -D
      useradd -D [选项]

选项：
-b, --base-dir BASE_DIR   新账户的主目录的基目录
-c, --comment COMMENT         新账户的 GECOS 字段
-d, --home-dir HOME_DIR       新账户的主目录
-D, --defaults        显示或更改默认的 useradd 配置
-e, --expiredate EXPIRE_DATE  新账户的过期日期
-f, --inactive INACTIVE       新账户的密码不活动期
-g, --gid GROUP       新账户主组的名称或 ID
-G, --groups GROUPS   新账户的附加组列表
-h, --help                    显示此帮助信息并推出
-k, --skel SKEL_DIR   使用此目录作为骨架目录
-K, --key KEY=VALUE           不使用 /etc/login.defs 中的默认值
-l, --no-log-init 不要将此用户添加到最近登录和登录失败数据库
-m, --create-home 创建用户的主目录
-M, --no-create-home      不创建用户的主目录
-N, --no-user-group   不创建同名的组
-o, --non-unique      允许使用重复的 UID 创建用户
-p, --password PASSWORD       加密后的新账户密码
-r, --system                  创建一个系统账户
-R, --root CHROOT_DIR         chroot 到的目录
-s, --shell SHELL     新账户的登录 shell
-u, --uid UID         新账户的用户 ID
-U, --user-group      创建与用户同名的组
-Z, --selinux-user SEUSER     为 SELinux 用户映射使用指定 SEUSER
```

### 参数  

用户名：要创建的用户名。

### 实例  

新建用户加入组：

```
useradd –g sales jack –G company,employees    //-g：加入主要组、-G：加入次要组
```

建立一个新用户账户，并设置ID：

```
useradd caojh -u 544
```

需要说明的是，设定ID值时尽量要大于500，以免冲突。因为Linux安装后会建立一些特殊用户，一般0到499之间的值留给bin、mail这样的系统账号。


