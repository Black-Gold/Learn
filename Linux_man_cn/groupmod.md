# **groupmod**

## 说明

**groupmod命令** 更改群组识别码或名称。需要更改群组的识别码或名称时，可用groupmod指令来完成这项工作

## 选项

```markdown
用法：groupmod [选项] 组

-g, --gid GID                 将组 ID 改为 GID
-h, --help                    显示此帮助信息并推出
-n, --new-name NEW_GROUP      改名为 NEW_GROUP
-o, --non-unique              允许使用重复的 GID
-p, --password PASSWORD	      将密码更改为(加密过的)PASSWORD
-R, --root CHROOT_DIR         chroot 到的目录

```

## 实例

```bash
groupmod -n cisco web   # 将组名web改成cisco
groupmod -g 9999 web    # 创建web组的同时指定gid为9999

```
