# pwck

## 说明

**pwck命令** 用来验证系统认证文件`/etc/passwd`和`/etc/shadow`的内容和格式的完整性

## 选项

```markdown
用法：pwck [选项] [passwd [shadow]]

-h, --help                    显示此帮助信息并推出
-q, --quiet                   只报告错误
-r, --read-only               显示错误和警告，但不改变文件
-R, --root CHROOT_DIR         chroot 到的目录
-s, --sort                    通过 UID 排序项目
```

## 实例

```bash
pwck /etc/passwd

```
