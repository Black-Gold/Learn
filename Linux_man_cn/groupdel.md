# groupdel

## 说明

**groupdel命令** 用于删除指定的工作组，本命令要修改的系统文件包括/ect/group和/ect/gshadow。
若该群组中仍包括某些用户，则必须先删除这些用户后，方能删除群组


## 选项

```markdown
用法：groupdel [选项] 组

-R, --root CHROOT_DIR         chroot到的目录
```

## 实例

```bash
groupdel damon  # 删除damon工作组
```

