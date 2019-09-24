# **find**

## 说明

```markdown
使用find和xargs可能需要系统查找具有某一特征的文件，例如文件权限、文件属主、文件长度、文件类型等，出于安全性考虑，一般系
统管理任务只是为了找出一个知道存放在哪里的文件，find可以遍历当前目录甚至整个文件系统查找文件或目录。即使系统中含有网络
文件系统(NFS)，find命令在该文件系统中同样有效，只要你具有相应的权限

## 选项

```markdown
用法: find [-H] [-L] [-P] [-Olevel] [-D help|tree|search|stat|rates|opt|exec] [path...] [expression]

默认路径为当前目录；默认表达式为 -print
表达式可能由下列成份组成：操作符、选项、测试表达式以及动作：
操作符 (优先级递减；未做任何指定时默认使用 -and):
( EXPR )   ! EXPR   -not EXPR   EXPR1 -a EXPR2   EXPR1 -and EXPR2
EXPR1 -o EXPR2   EXPR1 -or EXPR2   EXPR1 , EXPR2

positional options (always true): -daystart -follow -regextype

normal options (always true, specified before other expressions):
    -depth --help -maxdepth LEVELS -mindepth LEVELS -mount -noleaf
    --version -xautofs -xdev -ignore_readdir_race -noignore_readdir_race

比较测试 (N 可以是 +N 或 -N 或 N): -amin N -anewer FILE -atime N -cmin N
    -cnewer 文件 -ctime N -empty -false -fstype 类型 -gid N -group 名称
    -ilname 匹配模式 -iname 匹配模式 -inum N -ipath 匹配模式 -iregex 匹配模式
    -links N -lname 匹配模式 -mmin N -mtime N -name 匹配模式 -newer 文件
    -nouser -nogroup -path 匹配模式 -perm [+-]访问模式 -regex 匹配模式
    -readable -writable -executable
    -wholename 匹配模式 -size N[bcwkMG] -true -type [bcdpflsD] -uid N
    -used N -user 用户名 -xtype [bcdpfls]
    -context 文本
操作: -delete -print0 -printf 格式 -fprintf 文件 格式 -print
    -fprint0 文件 -fprint 文件 -ls -fls 文件 -prune -quit
    -exec 命令 ; -exec 命令 {} + -ok 命令
    -execdir 命令 ; -execdir 命令 {} + -okdir 命令

find 命令的一般形式为：find path  -options [-print -exec -ok]
该命令的参数解释：
path    find命令所查找的目录路径。例如用.来表示当前目录，用/来表示系统根目录
-print      find命令将匹配的文件输出到标准输出
-exec       find命令对匹配的文件执行该参数所给出的shell命令。相应命令的形式为'comm-and'{}\;，注意{}和\；之间的空格
-ok和-exec的作用相同，只不过以一种更为安全的模式来执行该参数所给出的shell命令，在执行每一个命令之前，会给出提示，让用户来确定是否执行


-amin<分钟>                       查找在指定时间曾被存取过的文件或目录，单位以分钟计算
-anewer<参考文件或目录>           查找其存取时间较指定文件或目录的存取时间更接近现在的文件或目录
-atime<24小时数>                  查找在指定时间曾被存取过的文件或目录，单位以24小时计算
-cmin<分钟>                       查找在指定时间之时被更改过的文件或目录
-cnewer<参考文件或目录>           查找其更改时间较指定文件或目录的更改时间更接近现在的文件或目录
-ctime<24小时数>                  查找在指定时间之时被更改的文件或目录，单位以24小时计算
-daystart                         从本日开始计算时间
-depth                            从指定目录下最深层的子目录开始查找
-empty                            寻找文件大小为0 Byte的文件，或目录下没有任何子目录或文件的空目录
-exec<执行指令>                   假设find指令的回传值为True，就执行该指令
-false                            将find指令的回传值皆设为False
-fls<列表文件>                    此参数的效果和指定“-ls”参数类似，但会把结果保存为指定的列表文件
-follow                           排除符号连接；如果find命令遇到符号链接文件，就跟踪至链接所指向的文件。(常用选项)
-fprint<列表文件>                 此参数的效果和指定“-print”参数类似，但会把结果保存成指定的列表文件
-fprint0<列表文件>                此参数的效果和指定“-print0”参数类似，但会把结果保存成指定的列表文件
-fprintf<列表文件><输出格式>      此参数的效果和指定“-printf”参数类似，但会把结果保存成指定的列表文件
-fstype<文件系统类型>             只寻找该文件系统类型下的文件或目录；(常用选项)
-gid<群组识别码>                  查找符合指定之群组识别码的文件或目录
-group<群组名称>                  查找符合指定之群组名称的文件或目录；(常用选项)
-ilname<范本样式>                 此参数的效果和指定“-lname”参数类似，但忽略字符大小写的差别
-iname<范本样式>                  此参数的效果和指定“-name”参数类似，但忽略字符大小写的差别
-inum<inode编号>                  查找符合指定的inode编号的文件或目录
-ipath<范本样式>                  此参数的效果和指定“-path”参数类似，但忽略字符大小写的差别
-iregex<范本样式>                 此参数的效果和指定“-regexe”参数类似，但忽略字符大小写的差别
-links<连接数目>                  查找符合指定的硬连接数目的文件或目录
-iname<范本样式>                  指定字符串作为寻找符号连接的范本样式
-ls                               假设find指令的回传值为Ture，就将文件或目录名称列出到标准输出
-maxdepth<目录层级>               设置最大目录层级
-mindepth<目录层级>               设置最小目录层级
-mmin<分钟>                       查找在指定时间曾被更改过的文件或目录，单位以分钟计算
-mount                            此参数的效果和指定“-xdev”相同；在查找文件时不跨越文件系统mount点。(常用选项)
-mtime<24小时数>                  查找在指定时间曾被更改过的文件或目录，单位以24小时计算；-mtime-n+n按照文件的更改时间来
                                  查找文件，-n表示文件更改时间距现在n天以内，+n表示文件更改时间距现在n天以前。(常用选项)
-name<范本样式>                   指定字符串作为寻找文件或目录的范本样式；(常用选项)
-newer<参考文件或目录>            查找其更改时间较指定文件或目录的更改时间更接近现在的文件或目录；-newerfile1!file2
                                  查找更改时间比文件file1新但比文件file2旧的文件。(常用选项)
-nogroup                          找出不属于本地主机群组识别码的文件或目录；(常用选项)
-noleaf                           不去考虑目录至少需拥有两个硬连接存在
-nouser                           找出不属于本地主机用户识别码的文件或目录；(常用选项)
-ok<执行指令>                     此参数的效果和指定“-exec”类似，但在执行指令之前会先询问用户，若回答“y”或“Y”，则放弃执行命令
-path<范本样式>                   指定字符串作为寻找目录的范本样式
-perm<权限数值>                   查找符合指定的权限数值的文件或目录；(常用选项)
-print                            假设find指令的回传值为Ture，就将文件或目录名称列出到标准输出。格式为每列一个名称，每个名称前皆有“./”字符串
-print0                           假设find指令的回传值为Ture，就将文件或目录名称列出到标准输出。格式为全部的名称皆在同一行
-printf<输出格式>                 假设find指令的回传值为Ture，就将文件或目录名称列出到标准输出。格式可以自行指定
-prune                            不寻找字符串作为寻找文件或目录的范本样式;如果同时使用了-depth选项，那么-prune选项将被find命令忽略。(常用选项)
-regex<范本样式>                  指定字符串作为寻找文件或目录的范本样式
-size<文件大小>                   查找符合指定的文件大小的文件
-true                             将find指令的回传值皆设为True
-type<文件类型>                   只寻找符合指定的文件类型的文件；(常用选项)

诸如：
  b-块设备文件
  d-目录
  c-字符设备文件
  p-管道文件
  l-符号链接文件
  f-普通文件

-uid<用户识别码>：查找符合指定的用户识别码的文件或目录
-used<日数>：查找文件或目录被更改之后在指定时间曾被存取过的文件或目录，单位以日计算
-user<拥有者名称>：查找符和指定的拥有者名称的文件或目录；(常用选项)
-xdev：将范围局限在先行的文件系统中
-xtype<文件类型>：此参数的效果和指定“-type”参数类似，差别在于它针对符号连接检查
```

## 实例

```bash
find / -name *.jpg -exec wc -c {} \;|awk '{print $1}'|awk '{a+=$1}END{print a}' # 统计一下服务器下面所有的jpg的文件的大小
find ./ -type f -print | wc -l  # 统计一个目录中的全部文件数
find ./ -type d -print | wc -l  # 统计一个目录中的全部子目录数

# 查找指定文件并执行删除操作
find . -name "文件名" | xargs rm -rf
find . -name "文件名" -exec rm -f {}\;
find $HOME/. -name "*.txt" -ok rm {} \; # 找出家目录下所有的.txt文件并删除,和-exec一样但会给出提示

find . -name "my*" -ls       # 搜索当前目录中所有文件名以my开头的文件并显示它们的详细信息
find /home -iname "*.txt" -print    # 查看home目录下以txt结尾的文件，iname表示忽略大小写
find /home ! -name "*.txt" -print   # 找出/home下不是以.txt结尾的文件
find /usr/ -path "*local*" -print   # 匹配文件路径或者文件,path后路径可以是多级的子目录

# -prune    使用这一选项可以使find命令不在当前指定的目录中查找，如果同时使用-depth选项，那么-prune将被find命令忽略
find . -path "./sk" -prune -o -name "*.txt" -print  # 查找当前目录或者子目录下所有.txt文件，但是跳过子目录sk
find /usr/sam \( -path /usr/sam/dir1 -o -path /usr/sam/file1 \) -prune -o -print    # 排除多个目录

# 当前目录及子目录下查找所有以.txt和.pdf结尾的文件
find . -name "*.txt" -o -name "*.pdf" -print
find . \( -name "*.txt" -o -name "*.pdf" \) -print

find . -regex ".*\(\.txt\|\.pdf\)$" -print  # 基于正则表达式匹配文件路径
find . -iregex ".*\(\.txt\|\.pdf\)$" -print  # 基于正则表达式匹配文件路径,但忽略大小写
find . -name  "[A-Z]*" -print   # 查找当前目录及子目录中文件名以一个大写字母开头的文件

# 统计var目录下文件以M为大小,以列表形式列出来
find /var -type f | xargs ls -s | sort -rn | awk '{size=$1/1024; printf("%dMb %s\n", size,$2);}' | head
```

### 通过文件特征查找

```bash
: << comment
常用的find命令的控制选项及其用法
选项               用途描述
-daystart     .   .测试系统从今天开始24小时以内的文件，用法类似-amin
-depth             使用深度级别的查找过程方式,在某层指定目录中优先查找文件内容
-follow            遵循通配符链接方式查找; 另外也可忽略通配符链接方式查询
-maxdepth levels   在某个层次的目录中按照递减方法查找
-mount             不在文件系统目录中查找，用法类似 -xdev.
-noleaf            禁止在非UNUX文件系统，MS-DOS系统，CD-ROM文件系统中进行最优化查找
-fstype            查找位于某一类型文件系统的文件，这些文件通常在/etc/fstab中可以找到
-cpio              对匹配的文件使用cpio命令
comment

: << comment
常用的查找文件并显示文件信息的参数和使用方法
选项                     用途描述
-exec command;           查找并执行命令
-exec ./text.sh {} \;    单行命令中-exec参数中无法使用多个命令，此方法可以实现在-exec之后接受多条命令
-fprint file             打印文件完整文件名
-fprint0 file            打印文件完整文件名包括空的文件
-fprintf file format     打印文件格式
-ok command;             给用户命令执行操作，根据用户的Y 确认输入执行
-printf format           打印文件格式
comment

```

### 根据-type文件类型进行搜索

```bash
: << comment
类型参数列表：

* b 块设备
* c 字符设备
* d 目录
* f 普通文件
* l 符号连接
* p 命名管道(FIFO)
* s 套接字
comment

find . -maxdepth 3 -type f  # 基于目录深度搜索,向下最大深度限制为3
find . -mindepth 2 -type f  # 搜索出深度距离当前目录至少2个子目录的所有文件
find .-type f -user root -exec chown tom {} \;  # 找出当前目录下所有root的文件，并把所有权更改为用户tom
find . -type f -name "*.txt" -delete    # 删除当前目录下所有.txt文件
find . -type f -name "*.txt" -exec cat {} \;> all.txt   # 查找当前目录下所有.txt文件并把他们拼接起来写入到all.txt文件中
find . -type f -name "*.txt" -exec printf "File: %s\n" {} \;    # 找出当前目录下所有.txt文件并以“File:文件名”的形式打印出来
find . -type f -name "*" | xargs grep "test"  # 当前目录搜索包含test内容的文件
find . -type f -mmin -10    # 搜索当前目录中，所有过去10分钟中更新过的普通文件。如果不加-type f参数，则搜索普通文件+特殊文件+目录

```

### 根据文件时间戳进行搜索

```bash
: << comment
find . -type f 时间戳,UNIX/Linux文件系统每个文件都有三种时间戳：
精确到分钟的用amin,mmin,cmin，精确到天的用atime,mtime,ctime
-mtime -n +n  -n表示文件更改时间距现在n天以内，+n表示文件更改时间距现在n天以前

* atime:访问时间(-atime/天，-amin/分钟)：用户最近一次访问时间。当备份实用程序或脚本已读取文件以及用户已读取文件时，atime也会更改
* mtime:修改时间(-mtime/天，-mmin/分钟)：文件最后一次修改时间。文件系统备份会随时更改，而原始设备备份不会更改。要实施增量或差异备份很重要
* 变化时间(-ctime/天，-cmin/分钟)：文件数据元（例如权限等）最后一次修改时间。
comment

find . -type f -atime -7    # 搜索最近七天内被访问过的所有文件
find . -type f -atime 7     # 搜索恰好在七天前被访问过的文件
find . -type f -atime +7    # 搜索超过七天被访问过的所有文件
find . -type f -mtime -5    # 查找更改时间在5天以内的文件
find . -type f -ctime -1    # 查找在24小时内状态改变的文件
find . -type f -amin +10    # 搜索访问时间超过10分钟的所有文件
find . -type f -mmin -5     # 查找在5分钟内修改过的文件
find . -type f -newer file.log  # 找出比file.log修改时间更长的所有文件
find . -type f -mtime +30 -name "*.log" -exec cp {} old \;  # 将30天前的log文件移动到old目录中
find . -newer file1 ! -newer file2 -exec ls -l {} \;    # 查找更改时间比文件file1新但比file2旧的文件

# 查找当前目录更改时间一天以内的文件并压缩
find . -mtime -1 -type f -print0 | xargs -0 tar rvf "archive.tar"
find . -mtime -1 -type f -exec tar rvf "archive.tar" '{}' \;
```

### 根据文件大小-size进行匹配

```bash
: << comment
find . -type f -size 文件大小单元
文件大小单元：

*    **b**  —— 块（512字节）
*    **c**  —— 字节
*    **w**  —— 字（2字节）
*    **k**  —— 千字节
*    **M**  —— 兆字节
*    **G**  —— 吉字节
comment

find . -empty   # 要列出所有空文件
find . -type f -size 0      # 搜索大小0字节的文件
find . -type f -size +10k   # 搜索大于10KB的文件
find . -type f -size -10k   # 搜索小于10KB的文件
find . -type f -size 10k    # 搜索等于10KB的文件
```

### 根据文件权限/所有权进行匹配

```bash
-perm mode:文件许可正好符合mode
-perm +mode:文件许可部分符合mode
-perm -mode: 文件许可完全符合mode

find -type f ! -perm -444   # 寻找所有不可读的文件；对网站有用
find -type d ! -perm -111   # 寻找不可访问的目录；对网站有用
find . -type f -perm 777    # 当前目录下搜索出权限为777的文件
find / -perm /u=s   # 查找所有SUID set文件
find / -perm /u=r   # 查找所有只读文件
find . -type f -name "*.php" ! -perm 644   # 找出当前目录下权限不是644的php文件
find . -perm 644 # 搜索对其所有者和组具有读写权限的文件，但其他用户可以读取不能写入
find . -perm -644  # 搜索对其所有者和组具有读写权限以及其他用户可以读取的文件，而不考虑是否存在其他额外权限，如可执行权限

# 搜索可由其所有者或其组写入的文件，这些文件不必是其所有者和组都具有写入权限的文件
# 第一个使用文件模式的八进制表示，另外两个使用sym-bolic形式
find . -perm /220
find . -perm /u+w,g+w
find . -perm /u=w,g=w

# 搜索其所有者和组都具有写入权限的文件
find . -perm -220
find . -perm -g+w,u+w

# 找出设置了SET位的权限的文件,-perm +6000表示不检查基本权限,第一种是find命令执行完才能看到结果，第二种没找到一条就立即显示
ls -lh $(find / -type f -perm +6000)

find / -type f -perm +6000 -exec ls -lh {} \;

find . -type f -user tom    # 找出当前目录用户tom拥有的所有文件
find . -type f -group sunk  # 找出当前目录用户组sunk拥有的所有文件
find . -user jack -or -user lee
find /home -nouser -print   # 找出宿主账户已经删除的文件,对应无宿组文件选项为-nogroup，即文件所属组在/etc/groups不存在
```

```bash
# cpio选项用于向磁带设备备份或从其中恢复文件
# 注意例子中路径中缺少/。这叫作相对路径。之所以使用相对路径，是因为在从磁带中恢复这些文件的时候，可以选择恢复文件的路径
# 例如，可以将这些文件先恢复到另外一个目录中，对它们进行某些操作后，再恢复到原始目录中。如果在备份时使用了绝对路径，例如
# /etc，那么在恢复时，就只能恢复到/etc目录中去，别无其他选择
# 例子中cpio命令使用了C65536选项，本可以使用B选项，但块大小只有512字节，而使用了C65536选项后，块大小变成了64K字节
find home -depth -print | cpio -ivcdC65536 -o /dev/rmt0

```
