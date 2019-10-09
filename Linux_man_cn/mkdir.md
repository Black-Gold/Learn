# **mkdir**

## 说明

**mkdir命令** 用来创建目录

## 选项

```markdown

用法：mkdir [选项]... 目录...
Create the DIRECTORY(ies), if they do not already exist.

Mandatory arguments to long options are mandatory for short options too.
  -m, --mode=MODE   建立目录的同时设置权限
  -p, --parents     若所建立目录的上层目录尚未建立，则一并创建上层目录
  -v, --verbose     print a message for each created directory
  -Z                设置安全上下文，当使用SELinux时生效
      --context[=CTX]  like -Z, or if CTX is specified then set the SELinux or SMACK security context to CTX
# 多个目录要用空格隔开
```

## 实例

```bash
mkdir -p -m 700 /usr/meng/test # 在目录`/usr/meng`下建立子目录test，并且只有文件主有读、写和执行权限，其他人无权访问
```

