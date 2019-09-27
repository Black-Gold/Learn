# **chgrp**

## 说明

**chgrp命令** 用来改变文件或目录所属的用户组。该命令用来改变指定文件所属的用户组。其中，组名可以是用户组的id，也可以是用户组的组名
文件名可以 是由空格分开的要改变属组的文件列表，也可以是由通配符描述的文件集合。如果用户不是该文件的文件主或超级用户(root)，则不能改变
该文件的组

在UNIX系统家族里，文件或目录权限的掌控以拥有者及所属群组来管理。您可以使用chgrp指令去变更文件与目录的所属群组，设置方式采用群组名称或
群组识别码皆可

## 选项

```markdown
用法：chgrp [选项]... 用户组 文件...
　或：chgrp [选项]... --reference=参考文件 文件...

-c, --changes          like verbose but report only when a change is made
-f, --silent, --quiet  suppress most error messages
-v, --verbose          output a diagnostic for every file processed
    --dereference      affect the referent of each symbolic link (this is
                       the default), rather than the symbolic link itself
-h, --no-dereference   affect symbolic links instead of any referenced file
                       (useful only on systems that can change the
                       ownership of a symlink)
    --no-preserve-root  do not treat '/' specially (the default)
    --preserve-root    fail to operate recursively on '/'
    --reference=RFILE  use RFILE's group rather than specifying a
                       GROUP value
-R, --recursive        operate on files and directories recursively

以下选项修改了在指定-R选项时遍历层次结构的方式。 如果指定了多个，则只有最后一个生效
-H                     if a command line argument is a symbolic link
                       to a directory, traverse it
-L                     traverse every symbolic link to a directory
                       encountered
-P                     do not traverse any symbolic links (default)

示例：
  chgrp staff /u            将 /u 的属组更改为"staff"
  chgrp -hR staff /u    将 /u 及其子目录下所有文件的属组更改为"staff"

```

## 实例

```bash
chgrp -R mengxin /usr/meng  # 将`/usr/meng`及其子目录下的所有文件的用户组改为mengxin
chgrp newuser ah    # 更改文件ah的组群所有者为newuser

```
