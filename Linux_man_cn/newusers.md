# newusers

## 说明

**newusers命令** 用于批处理的方式一次创建多个命令

```markdown
-r, --system                  create system accounts
-R, --root CHROOT_DIR         directory to chroot into
```

## 实例

```bash
# newusers命令批量添加用户：newusers后面直接跟一个文件，文件格式和`/etc/passwd`的格式相同
:<< comment
用户名1:x:UID:GID:用户说明:用户的家目录:所用SHELL
jingang0:x:520:520::/home/jingang0:/sbin/nologin
jingang1:x:521:521::/home/jingang1:/sbin/nologin
comment
```
