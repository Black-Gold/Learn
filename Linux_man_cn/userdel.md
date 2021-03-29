# **userdel**

## 说明

**userdel命令** 用于删除给定的用户，以及与用户相关的文件。若不加选项，则仅删除用户帐号，而不删除相关文件

```markdown
-f, --force                   强制执行某些否则会失败的动作，例如：即使用户已经登录状态
-r, --remove                  删除用户的同时删除主目录和邮件池
-R, --root CHROOT_DIR         chroot 到的目录
-Z, --selinux-user            为用户删除所有的 SELinux 用户映射

```

## 实例

```bash
userdel linuxde       # 删除用户linuxde，但不删除其家目录及文件
userdel -r linuxde    # 删除用户linuxde，其家目录及文件一并删除;不要轻易用`-r`选项
```
