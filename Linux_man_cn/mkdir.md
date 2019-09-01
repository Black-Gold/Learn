# **mkdir**

## 说明

**mkdir命令** 用来创建目录。该命令创建由dirname命名的目录。如果在目录名的前面没有加任何路径名，则在当前目录下创建由dirna
me指定的目录；如果给出了一个已经存在的路径，将会在该目录下创建一个指定的目录。在创建目录时，应保证新建的目录与它所在目录
下的文件没有重名

注意：在创建文件时，不要把所有的文件都存放在主目录中，可以创建子目录，通过它们来更有效地组织文件。最好采用前后一致的命名
方式来区分文件和目录。例如，目录名可以以大写字母开头，这样，在目录列表中目录名就出现在前面

在一个子目录中应包含类型相似或用途相近的文件。例如，应建立一个子目录，它包含所有的数据库文件，另有一个子目录应包含电子表
格文件，还有一个子目录应包含文字处理文档，等等。目录也是文件，它们和普通文件一样遵循相同的命名规则，并且利用全路径可以唯
一地指定一个目录

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
mkdir -m 700 /usr/meng/test # 在目录`/usr/meng`下建立子目录test，并且只有文件主有读、写和执行权限，其他人无权访问

mkdir -p-m 750 bin/os_1     # 在当前目录中建立bin和bin下的os_1目录，权限设置为文件主可读、写、执行，同组用户可读和执行，其他用户无权访问
```

