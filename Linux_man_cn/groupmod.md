groupmod
===

更改群组识别码或名称

## 补充说明

**groupmod命令** 更改群组识别码或名称。需要更改群组的识别码或名称时，可用groupmod指令来完成这项工作。

### 语法  

```
groupmod(选项)(参数)
```

### 选项  

```
-g, --gid GID                 将组 ID 改为 GID
-h, --help                    显示此帮助信息并推出
-n, --new-name NEW_GROUP      改名为 NEW_GROUP
-o, --non-unique              允许使用重复的 GID
-p, --password PASSWORD   将密码更改为(加密过的) PASSWORD
-R, --root CHROOT_DIR         chroot 到的目录
```

### 参数  

组名：指定要修改的工作的组名。


<!-- Linux命令行搜索引擎：https://jaywcjlove.github.io/linux-command/ -->
