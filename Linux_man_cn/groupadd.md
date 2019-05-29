groupadd
===

用于创建一个新的工作组

## 补充说明

**groupadd命令** 用于创建一个新的工作组，新工作组的信息将被添加到系统文件中。

### 语法  

```
groupadd(选项)(参数)
```

  

```
-f, --force       如果组已经存在则成功退出
并且如果 GID 已经存在则取消 -g
-g, --gid GID                 为新组使用 GID
-h, --help                    显示此帮助信息并推出
-K, --key KEY=VALUE           不使用 /etc/login.defs 中的默认值
-o, --non-unique              允许创建有重复 GID 的组
-p, --password PASSWORD       为新组使用此加密过的密码
-r, --system                  创建一个系统账户
-R, --root CHROOT_DIR         chroot 到的目录
```

### 参数  

组名：指定新建工作组的组名。

### 实例  

建立一个新组，并设置组ID加入系统：

```
groupadd -g 344 jsdigname
```

此时在`/etc/passwd`文件中产生一个组ID（GID）是344的项目。



