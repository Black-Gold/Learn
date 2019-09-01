# **chmod**

## 说明

**chmod命令** 用来变更文件或目录的权限。在UNIX系统家族里，文件或目录权限的控制分别以读取、写入、执行3种一般权限来区分
另有3种特殊权限可供运用。用户可以使用chmod指令去变更文件与目录的权限，设置方式采用文字或数字代号皆可。符号连接的权限无法
变更，如果用户对符号连接修改权限，其改变会作用在被连接的原始文件



## 选项

```markdown
用法：chmod [选项]   模式[,模式]  文件
　或：chmod [选项]   八进制模式 文件
　或：chmod [选项]   --reference=参考文件 文件

权限范围的表示法如下：
u     # User，即文件或目录的拥有者
g     # Group，即文件或目录的所属群组
o     # Other，除了文件或目录拥有者或所属群组之外，其他用户皆属于这个范围
a     # All，即全部的用户，包含拥有者，所属群组以及其他用户

r     # 读取权限，数字代号为4
w     # 写入权限，数字代号为2
x     # 执行或切换权限，数字代号为1
-     # 不具任何权限，数字代号为0
s     # 特殊功能说明：变更文件或目录的权限

+     # 添加某些权限
-     # 取消某些权限
=     # 设置文件的权限为给定的权限

X     # 如果目标文件是可执行文件或目录，可给其设置可执行权限
s     # 设置权限suid和sgid，使用权限组合“u+s”设定文件的用户的ID位，“g+s”设置组ID位
t     # 只有目录或文件的所有者才可以删除目录下的文件

-c, --changes          和-v选项类似，但只打印已经更改的部分
-f, --silent, --quiet  禁止大部分错误信息
-v, --verbose          输出每个文件的执行详细信息
    --no-preserve-root  do not treat '/' specially (the default)
    --preserve-root    fail to operate recursively on '/'
    --reference=RFILE  use RFILE's mode instead of MODE values
-R, --recursive        对文件和目录进行递归处理

MODE如下：
[ugoa]*([-+=]([rwxXst]*|[ugo]))+|[-+=][0-7]+
```

## 实例

```bash
chmod u+x,g+w f01   # 为文件f01设置自己可以执行，组员可以写入的权限
chmod u=rwx,g=rw,o=r f01
chmod 764 f01
chmod a+x f01       # 对文件f01的u,g,o都设置可执行属性
chown user:market f01   # 把文件f01给uesr，添加到market组
```

