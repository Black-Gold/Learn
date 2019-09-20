# **gpasswd**

## 说明

**gpasswd命令** 是Linux下工作组文件`/etc/group`和`/etc/gshadow`管理工具

## 选项

```markdown
用法：gpasswd [选项] 组

-a, --add USER                  向组 GROUP 中添加用户 USER
-d, --delete USER               从组 GROUP 中添加或删除用户
-Q, --root CHROOT_DIR           要 chroot 进的目录
-r, --delete-password           remove the GROUP's password
-R, --restrict                  向其成员限制访问组 GROUP
-M, --members USER,...          设置组 GROUP 的成员列表
-A, --administrators ADMIN,...	设置组的管理员列表
除非使用 -A 或 -M 选项，不能结合使用这些选项

```

## 实例


```bash
gpasswd groupname   # 如系统有个peter账户，该账户本身不是groupname群组的成员，使用newgrp需要输入密码即可。

: << comment
让使用者暂时成为该组成员，之后peter用户创建的文件组名也会是groupname。所以该方式可暂时让peter建立文件时使用其他的组，
而不是peter本身所在的组。所以使用`gpasswd groupname`设定密码，就是让知道该群组密码的人可以暂时切换具备groupname群组功能的。
comment
gpasswd -A peter users  # 此处peter就是users群组的管理员

: << comment
注意：添加用户到某一个组 可以使用`usermod -G group_name user_name`这个命令可以添加一个用户到指定的组，但是以前添加的组就会清空掉。
所以想要添加一个用户到一个组，同时保留以前添加的组时，请使用gpasswd这个命令来添加操作用户
comment
gpasswd -a user_name group_name
```


