find
===

```txt
使用find和xargs可能需要系统查找具有某一特征的文件，例如文件权限、文件属主、文件长度、文件类型等，出于安全性考虑，一般系统管理任务只是为了找出一个知道存放在哪里的文件，find可以遍历当前目录甚至整个文件系统查找文件或目录。即使系统中含有网络文件系统(NFS)，find命令在该文件系统中同样有效，只要你具有相应的权限。
```

## 补充说明

**find命令** 用来在指定目录下查找文件。任何位于参数之前的字符串都将被视为欲查找的目录名。如果使用该命令时，不设置任何参数，则find命令将在当前目录下查找子目录与文件。并且将查找到的子目录和文件全部进行显示。

在运行一个非常消耗资源的find命令时，很多人都倾向于把它放在后台执行，因为遍历一个大的文件系统可能会花费很长的时间(这里是指30G字节以上的文件系统)。

### 语法

```sh
find(选项)(参数)

find的使用格式如下：
$ find <指定目录> <指定条件> <指定动作>
- <指定目录>： 所要搜索的目录及其所有子目录。默认为当前目录。
- <指定条件>： 所要搜索的文件的特征。
- <指定动作>： 对搜索结果进行特定的处理。

find 命令格式:
1、find命令的一般形式为；
2、find命令的参数；
3、find命令选项；
4、使用exec或ok来执行shell命令；
```

```sh
Find命令的一般形式为：
  find pathname  -options [-print -exec -ok]
该命令的参数解释：
  pathname find命令所查找的目录路径。例如用.来表示当前目录，用/来表示系统根目录。
  -print find命令将匹配的文件输出到标准输出。
  -exec find命令对匹配的文件执行该参数所给出的shell命令。相应命令的形式为'comm-
  and'{}\;，注意{}和\；之间的空格。
  -ok和-exec的作用相同，只不过以一种更为安全的模式来执行该参数所给出的shell命令，在执行每一个命令之前，都会给出提示，让用户来确定是否执行。
```

### 选项  

```sh
-amin<分钟>：查找在指定时间曾被存取过的文件或目录，单位以分钟计算；
-anewer<参考文件或目录>：查找其存取时间较指定文件或目录的存取时间更接近现在的文件或目录；
-atime<24小时数>：查找在指定时间曾被存取过的文件或目录，单位以24小时计算；
-cmin<分钟>：查找在指定时间之时被更改过的文件或目录；
-cnewer<参考文件或目录>查找其更改时间较指定文件或目录的更改时间更接近现在的文件或目录；
-ctime<24小时数>：查找在指定时间之时被更改的文件或目录，单位以24小时计算；
-daystart：从本日开始计算时间；
-depth：从指定目录下最深层的子目录开始查找；
-empty：寻找文件大小为0 Byte的文件，或目录下没有任何子目录或文件的空目录；
-exec<执行指令>：假设find指令的回传值为True，就执行该指令；
-false：将find指令的回传值皆设为False；
-fls<列表文件>：此参数的效果和指定“-ls”参数类似，但会把结果保存为指定的列表文件；
-follow：排除符号连接；如果find命令遇到符号链接文件，就跟踪至链接所指向的文件。(常用选项)
-fprint<列表文件>：此参数的效果和指定“-print”参数类似，但会把结果保存成指定的列表文件；
-fprint0<列表文件>：此参数的效果和指定“-print0”参数类似，但会把结果保存成指定的列表文件；
-fprintf<列表文件><输出格式>：此参数的效果和指定“-printf”参数类似，但会把结果保存成指定的列表文件；
-fstype<文件系统类型>：只寻找该文件系统类型下的文件或目录；(常用选项)
-gid<群组识别码>：查找符合指定之群组识别码的文件或目录；
-group<群组名称>：查找符合指定之群组名称的文件或目录；(常用选项)
-help或——help：在线帮助；
-ilname<范本样式>：此参数的效果和指定“-lname”参数类似，但忽略字符大小写的差别；
-iname<范本样式>：此参数的效果和指定“-name”参数类似，但忽略字符大小写的差别；
-inum<inode编号>：查找符合指定的inode编号的文件或目录；
-ipath<范本样式>：此参数的效果和指定“-path”参数类似，但忽略字符大小写的差别；
-iregex<范本样式>：此参数的效果和指定“-regexe”参数类似，但忽略字符大小写的差别；
-links<连接数目>：查找符合指定的硬连接数目的文件或目录；
-iname<范本样式>：指定字符串作为寻找符号连接的范本样式；
-ls：假设find指令的回传值为Ture，就将文件或目录名称列出到标准输出；
-maxdepth<目录层级>：设置最大目录层级；
-mindepth<目录层级>：设置最小目录层级；
-mmin<分钟>：查找在指定时间曾被更改过的文件或目录，单位以分钟计算；
-mount：此参数的效果和指定“-xdev”相同；在查找文件时不跨越文件系统mount点。(常用选项)
-mtime<24小时数>：查找在指定时间曾被更改过的文件或目录，单位以24小时计算；-mtime-n+n按照文件的更改时间来查找文件，-n表示文件更改时间距现在n天以内，+n表示文件更改时间距现在n天以前。(常用选项)
-name<范本样式>：指定字符串作为寻找文件或目录的范本样式；(常用选项)
-newer<参考文件或目录>：查找其更改时间较指定文件或目录的更改时间更接近现在的文件或目录；-newerfile1!file2查找更改时间比文件file1新但比文件file2旧的文件。(常用选项)
-nogroup：找出不属于本地主机群组识别码的文件或目录；(常用选项)
-noleaf：不去考虑目录至少需拥有两个硬连接存在；
-nouser：找出不属于本地主机用户识别码的文件或目录；(常用选项)
-ok<执行指令>：此参数的效果和指定“-exec”类似，但在执行指令之前会先询问用户，若回答“y”或“Y”，则放弃执行命令；
-path<范本样式>：指定字符串作为寻找目录的范本样式；
-perm<权限数值>：查找符合指定的权限数值的文件或目录；(常用选项)
-print：假设find指令的回传值为Ture，就将文件或目录名称列出到标准输出。格式为每列一个名称，每个名称前皆有“./”字符串；
-print0：假设find指令的回传值为Ture，就将文件或目录名称列出到标准输出。格式为全部的名称皆在同一行；
-printf<输出格式>：假设find指令的回传值为Ture，就将文件或目录名称列出到标准输出。格式可以自行指定；
-prune：不寻找字符串作为寻找文件或目录的范本样式;如果同时使用了-depth选项，那么-prune选项将被find命令忽略。(常用选项)
-regex<范本样式>：指定字符串作为寻找文件或目录的范本样式；
-size<文件大小>：查找符合指定的文件大小的文件；
-true：将find指令的回传值皆设为True；
-type<文件类型>：只寻找符合指定的文件类型的文件；(常用选项)
诸如：
	b-块设备文件。
	d-目录。
	c-字符设备文件。
	p-管道文件。
	l-符号链接文件。
	f-普通文件。
-uid<用户识别码>：查找符合指定的用户识别码的文件或目录；
-used<日数>：查找文件或目录被更改之后在指定时间曾被存取过的文件或目录，单位以日计算；
-user<拥有者名称>：查找符和指定的拥有者名称的文件或目录；(常用选项)
-version或——version：显示版本信息；
-xdev：将范围局限在先行的文件系统中；
-xtype<文件类型>：此参数的效果和指定“-type”参数类似，差别在于它针对符号连接检查。
```

### 参数  

起始目录：查找文件的起始目录。

### 实例

```sh
# 当前目录搜索所有文件，文件内容 包含 “140.206.111.111” 的内容
find . -type f -name "*" | xargs grep "140.206.111.111" -print
```

搜索当前目录中，所有文件名以my开头的文件，并显示它们的详细信息。
find . -name 'my*' -ls

搜索当前目录中，所有过去10分钟中更新过的普通文件。如果不加-type f参数，则搜索普通文件+特殊文件+目录。
find . -type f -mmin -10

#### 根据文件或者正则表达式进行匹配  

列出当前目录及子目录下所有文件和文件夹

```sh
find .
```

在`/home`目录下查找以.txt结尾的文件名

```sh
find /home -name "*.txt" -print
```

同上，但忽略大小写

```sh
find /home -iname "*.txt" -print
```

当前目录及子目录下查找所有以.txt和.pdf结尾的文件

```sh
find . \( -name "*.txt" -o -name "*.pdf" \) -print

或

find . -name "*.txt" -o -name "*.pdf" -print
```

匹配文件路径或者文件

```sh
find /usr/ -path "*local*" -print
```

基于正则表达式匹配文件路径

```sh
find . -regex ".*\(\.txt\|\.pdf\)$" -print
```

同上，但忽略大小写

```sh
find . -iregex ".*\(\.txt\|\.pdf\)$" -print
```

想要在/etc目录中查找文件名以host开头的文件，可以用：
```
find /etc -name  "host*" -print
```

想要的当前目录及子目录中查找文件名以一个大写字母开头的文件，可以用：

```sh
find . -name  "[A-Z]*" -print
```

如果想在当前目录查找文件名以两个小写字母开头，跟着是两个数字，最后是*.txt的文件，下面的命令就能够返回名为ax37.txt的文件：
```
find . -name  "[a-z][a-z][0--9][0--9].txt" -print
```

Find命令查找指定文件并执行删除操作
```
find ./ -name "文件名" -exec rm -f {}\;
```

#### 否定参数  

找出/home下不是以.txt结尾的文件

```sh
find /home ! -name "*.txt" -print
```

#### 根据文件类型进行搜索  

```sh
find . -type 类型参数
```


类型参数列表：

*    **f**  普通文件
*    **l**  符号连接
*    **d**  目录
*    **c**  字符设备
*    **b**  块设备
*    **s**  套接字
*    **p**  Fifo

#### 基于目录深度搜索

向下最大深度限制为3

```
find . -maxdepth 3 -type f
```

搜索出深度距离当前目录至少2个子目录的所有文件

```
find . -mindepth 2 -type f
```

#### 根据文件时间戳进行搜索  

```
find . -type f 时间戳
```

UNIX/Linux文件系统每个文件都有三种时间戳：

*    **访问时间** （-atime/天，-amin/分钟）：用户最近一次访问时间。
*    **修改时间** （-mtime/天，-mmin/分钟）：文件最后一次修改时间。
*    **变化时间** （-ctime/天，-cmin/分钟）：文件数据元（例如权限等）最后一次修改时间。

搜索最近七天内被访问过的所有文件

```
find . -type f -atime -7
```

搜索恰好在七天前被访问过的所有文件

```
find . -type f -atime 7
```

搜索超过七天内被访问过的所有文件

```
find . -type f -atime +7
```

搜索访问时间超过10分钟的所有文件

```
find . -type f -amin +10
```

找出比file.log修改时间更长的所有文件

```
find . -type f -newer file.log
```

#### 根据文件大小进行匹配  

```
find . -type f -size 文件大小单元
```

文件大小单元：

*    **b**  —— 块（512字节）
*    **c**  —— 字节
*    **w**  —— 字（2字节）
*    **k**  —— 千字节
*    **M**  —— 兆字节
*    **G**  —— 吉字节

搜索大于10KB的文件

```
find . -type f -size +10k
```

搜索小于10KB的文件

```
find . -type f -size -10k
```

搜索等于10KB的文件

```
find . -type f -size 10k
```

#### 删除匹配文件  

删除当前目录下所有.txt文件

```
find . -type f -name "*.txt" -delete
```

#### 根据文件权限/所有权进行匹配  

当前目录下搜索出权限为777的文件

```
find . -type f -perm 777
```

找出当前目录下权限不是644的php文件

```
find . -type f -name "*.php" ! -perm 644
```

找出当前目录用户tom拥有的所有文件

```
find . -type f -user tom
```

找出当前目录用户组sunk拥有的所有文件

```
find . -type f -group sunk
```

#### 借助`-exec`选项与其他命令结合使用  

找出当前目录下所有root的文件，并把所有权更改为用户tom

```
find .-type f -user root -exec chown tom {} \;
```

上例中， **{}**  用于与 **-exec** 选项结合使用来匹配所有文件，然后会被替换为相应的文件名。

找出自己家目录下所有的.txt文件并删除

```
find $HOME/. -name "*.txt" -ok rm {} \;
```

上例中， **-ok** 和 **-exec** 行为一样，不过它会给出提示，是否执行相应的操作。

查找当前目录下所有.txt文件并把他们拼接起来写入到all.txt文件中

```
find . -type f -name "*.txt" -exec cat {} \;> all.txt
```

将30天前的.log文件移动到old目录中

```
find . -type f -mtime +30 -name "*.log" -exec cp {} old \;
```

找出当前目录下所有.txt文件并以“File:文件名”的形式打印出来

```
find . -type f -name "*.txt" -exec printf "File: %s\n" {} \;
```

因为单行命令中-exec参数中无法使用多个命令，以下方法可以实现在-exec之后接受多条命令

```
-exec ./text.sh {} \;
```

#### 搜索但跳出指定的目录  

查找当前目录或者子目录下所有.txt文件，但是跳过子目录sk

```
find . -path "./sk" -prune -o -name "*.txt" -print
```

#### find其他技巧收集  

要列出所有长度为零的文件

```
find . -empty
```

#### 删除指定文件夹下后缀名相同的文件

```sh
方法一:
find 目录 -name "*.abc" | xargs rm
命令有点危险，可以先执行前半段，看看是不是你要删除的文件, 然后再整条执行

方法二:
find . -name '*.exe' -type f -print -exec rm -rf {} \;
(1) "."    表示从当前目录开始递归查找
(2) “ -name '*.exe' "根据名称来查找，要查找所有以.exe结尾的文件夹或者文件
(3) " -type f "查找的类型为文件
(4) "-print" 输出查找的文件目录名
(5) 最主要的是是-exec了，-exec选项后边跟着一个所要执行的命令，表示将find出来的文件或目录执行该命令。
exec选项后面跟随着所要执行的命令或脚本，然后是一对儿{}，一个空格和一个\，最后是一个分号
```

#### 如何找出设置了SET位的权限的文件？

```sh
ls -lh $(find / -type f -perm +6000)
find / -type f -perm +6000 -exec ls -lh {} \;
命令含义介绍:
-perm +6000 表示不检查基本权限（000），只要附加权限中匹配任何一位（6包含了4、2）即满足条件;结合“ls -lh”命令是为了同时显示出结果文件的详细属性
两种方法的区别在于：前者使用了Shell的命令替换操作（ $() 符号或者反撇号 ``），只有在find命令执行完毕后才能看到结果；而后一种方法则每找到一条结果就立即显示出来了
```

<!-- Linux命令行搜索引擎：https://jaywcjlove.github.io/linux-command/ -->

#### 暂未整理一

```sh

2.1.2使用perm选项 
如果希望按照文件权限模式来查找文件的话，可以采用-perm选项。你可能需要找到所有用户都具有执行权限的文件，或是希望查看某个用户目录下的文件权限类型。在使用这一选项的时候，最好使用八进制的权限表示法。
为了在当前目录下查找文件权限位为755的文件，即文件属主可以读、写、执行，其他用户可以读、执行的文件，可以用：
$ find . -perm  755 -print
如果希望在当前目录下查找所有用户都可读、写、执行的文件（要小心这种情况），我们可以使用find命令的-perm选项。在八进制数字前面要加一个横杠-。在下面的命令中-perm代表按照文件权限查找，而‘007’和你在chmod命令的绝对模式中所采用的表示法完全相同。
$ find . -perm  -007 -print
2.1.3忽略某个目录 
如果在查找文件时希望忽略某个目录，因为你知道那个目录中没有你所要查找的文件，那么可以使用-prune选项来指出需要忽略的目录。在使用-prune选项时要当心，因为如果你同时使用了-depth选项，那么-prune选项就会被find命令忽略。
如果希望在/apps目录下查找文件，但不希望在/apps/bin目录下查找，可以用：
$ find /apps -name  "/apps/bin" -prune -o -print
2.1.4使用user和nouser选项 
如果希望按照文件属主查找文件，可以给出相应的用户名。例如，在$HOME目录中查找文件属主为dave的文件，可以用：
$ find ~ -user  dave -print
在/etc目录下查找文件属主为uucp的文件：
$ find /etc -user  uucp -print
为了查找属主帐户已经被删除的文件，可以使用-nouser选项。这样就能够找到那些属主在/etc/passwd文件中没有有效帐户的文件。在使用-nouser选项时，不必给出用户名；find命令能够为你完成相应的工作。例如，希望在/home目录下查找所有的这类文件，可以用：
$ find /home -nouser  -print
2.1.5使用group和nogroup选项 
就像user和nouser选项一样，针对文件所属于的用户组，find命令也具有同样的选项，为了在/apps目录下查找属于accts用户组的文件，可以用：
$ find /apps -group  accts -print
要查找没有有效所属用户组的所有文件，可以使用nogroup选项。下面的find命令从文件系统的根目录处查找这样的文件
$ find / -nogroup  -print
2.1.6按照更改时间查找文件 
如果希望按照更改时间来查找文件，可以使用mtime选项。如果系统突然没有可用空间了，很有可能某一个文件的长度在此期间增长迅速，这时就可以用mtime选项来查找这样的文件。用减号-来限定更改时间在距今n日以内的文件，而用加号+来限定更改时间在距今n日以前的文件。
希望在系统根目录下查找更改时间在5日以内的文件，可以用：
$ find/-mtime-5-print
为了在/var/adm目录下查找更改时间在3日以前的文件，可以用：
$ find /var/adm  -mtime +3 -print
2.1.7查找比某个文件新或旧的文件 
如果希望查找更改时间比某个文件新但比另一个文件旧的所有文件，可以使用-newer选项。它的一般形式为：
newest_file_name  ! oldest_file_name
其中，！是逻辑非符号。
这里有两个文件，它们的更改时间大约相差两天。
-rwxr-x-r-x     1 root     root        92    Apr  18 11:18         age.awk
-rwxrwxr-x     1 root     root   1045    Apr 20 19:37         belts.awk
下面给出的find命令能够查找更改时间比文件age.awk新但比文件belts.awk旧的文件：
$ find . -newer age.awk ! -newer belts.awk -exec ls -l  {} \;
-rwxrwxr-x     1 root     root        62    Apr  18 11:32         ./who.awk
-rwxr-xr-x      1 root     root        49    Apr  18 12:05         ./group.awk
-rw-r--r--              1 root     root    201    Apr  20 19:30         ./grade2.txt
-rwxrwxr-x     1 root     root   1054    Apr 20 19:37         ./belts.awk
如果想使用find命令的这一选项来查找更改时间在两个小时以内的文件，除非有一个现成的文件其更改时间恰好在两个小时以前，否则就没有可用来比较更改时间的文件。为了解决这一问题，可以首先创建一个文件并将其日期和时间戳设置为所需要的时间。这可以用touch命令来实现。
假设现在的时间是23:40，希望查找更改时间在两个小时以内的文件，可以首先创建这样一个文件：
$ touch -t 05042140 dstamp
-rw-r--r--              1 dave    admin     0     May 4  21:40        dstamp
一个符合要求的文件已经被创建；这里我们假设今天是五月四日，而该文件的更改时间是21:40，比现在刚好早两个小时。
现在我们就可以使用find命令的-newer选项在当前目录下查找所有更改时间在两个小时以内的文件：
$find . -newer  dstamp -print
2.1.8使用type选项 
UNIX或LINUX系统中有若干种不同的文件类型，这部分内容我们在前面的章节已经做了介绍，这里就不再赘述。如果要在/etc目录下查找所有的目录，可以用：
$find /etc -type  d -print
为了在当前目录下查找除目录以外的所有类型的文件，可以用：
$find . ! -type  d -print
为了在/etc目录下查找所有的符号链接文件，可以用：
$find /etc -type  l -print
2.1.9
使用size选项可以按照文件长度来查找文件，这里所指的文件长度既可以用块（block）来计量，也可以用字节来计量。以字节计量文件长度的表达形式为Nc；以块计量文件长度只用数字表示即可。
就我个人而言，我总是使用以字节计的方式，在按照文件长度查找文件时，大多数人都喜欢使用这种以字节表示的文件长度，而不用块的数目来表示，除非是在查看文件系统的大
小，因为这时使用块来计量更容易转换。
为了在当前目录下查找文件长度大于1M字节的文件，可以用：
$find . -size  +1000000c -print
为了在/home/apache目录下查找文件长度恰好为100字节的文件，可以用：
$find /home /apache  -size 100c -print
为了在当前目录下查找长度超过10块的文件（一块等于512字节），可以用：
$find . -size  +10 -print
2.1.10使用depth选项 
在使用find命令时，可能希望先匹配所有的文件，再在子目录中查找。使用depth选项就可以使find命令这样做。这样做的一个原因就是，当在使用find命令向磁带上备份文件系统时，希望首先备份所有的文件，其次再备份子目录中的文件。
在下面的例子中，find命令从文件系统的根目录开始，查找一个名为CON.FILE的文件。它将首先匹配所有的文件然后再进入子目录中查找。
$find / -name  "CON.FILE" -depth -print
2.1.11使用mount选项 
在当前的文件系统中查找文件（不进入其他文件系统），可以使用find命令的mount选项。在下面的例子中，我们从当前目录开始查找位于本文件系统中文件名以XC结尾的文件：
$find . -name  "*.XC" -mount -print
2.1.12使用cpio选项 
cpio命令可以用来向磁带设备备份文件或从中恢复文件。可以使用find命令在整个文件系统中（更多的情况下是在部分文件系统中）查找文件，然后用cpio命令将其备份到磁带上。
如果希望使用cpio命令备份/etc、/home和/apps目录中的文件，可以使用下面所给出的命令，不过要记住你是在文件系统的根目录下：
$ cd /
$ find etc home apps -depth -print | cpio -ivcdC65536  -o /dev/rmt0
（在上面的例子中，第一行末尾的\告诉shell命令还未结束，忽略\后面的回车。）
在上面的例子中，应当注意到路径中缺少/。这叫作相对路径。之所以使用相对路径，是因为在从磁带中恢复这些文件的时候，可以选择恢复文件的路径。例如，可以将这些文件先恢复到另外一个目录中，对它们进行某些操作后，再恢复到原始目录中。如果在备份时使用了绝对路径，例如/etc，那么在恢复时，就只能恢复到/etc目录中去，别无其他选择。在上面的例子中，我告诉find命令首先进入/etc目录，然后是/home和/apps目录，先匹配这些目录下的文件，然后再匹配其子目录中的文件，所有这些结果将通过管道传递给cpio命令进行备份。
顺便说一下，在上面的例子中cpio命令使用了C65536选项，我本可以使用B选项，不过这样每块的大小只有512字节，而使用了C65536选项后，块的大小变成了64K字节（65536/1024）。
2.1.13使用exec或ok来执行shell命令 
当匹配到一些文件以后，可能希望对其进行某些操作，这时就可以使用-exec选项。一旦find命令匹配到了相应的文件，就可以用-exec选项中的命令对其进行操作（在有些操作系统中只允许-exec选项执行诸如ls或ls-l这样的命令）。大多数用户使用这一选项是为了查找旧文件并删除它们。这里我强烈地建议你在真正执行rm命令删除文件之前，最好先用ls命令看一下，确认它们是所要删除的文件。
exec选项后面跟随着所要执行的命令，然后是一对儿{}，一个空格和一个\，最后是一个分号。
为了使用exec选项，必须要同时使用print选项。如果验证一下find命令，会发现该命令只输出从当前路径起的相对路径及文件名。
为了用ls-l命令列出所匹配到的文件，可以把ls-l命令放在find命令的-exec选项中，例如：
$ find . -type f -exec ls-l {} \;
-rwxr-xr-x      10 root   wheel            1222       Jan  4     1993       ./sbin/C80
-rwxr-xr-x      10 root   wheel            1222       Jan  4     1993       ./sbin/Normal
-rwxr-xr-x      10 root   wheel            1222       Jan  4     1993       ./sbin/Revvid
上面的例子中，find命令匹配到了当前目录下的所有普通文件，并在-exec选项中使用ls-l命令将它们列出。
为了在/logs目录中查找更改时间在5日以前的文件并删除它们，可以用：
$ find logs -type  f -mtime +5 -exec rm {} \;
记住，在shell中用任何方式删除文件之前，应当先查看相应的文件，一定要小心！
当使用诸如mv或rm命令时，可以使用-exec选项的安全模式。它将在对每个匹配到的文件进行操作之前提示你。在下面的例子中，find命令在当前目录中查找所有文件名以.LOG结尾、更改时间在5日以上的文件，并删除它们，只不过在删除之前先给出提示。
$ find . -name “*.LOG” -mtime +5 -ok rm {} \;
<rm  … ./nets.LOG> ?y
按y键删除文件，按n键不删除。
任何形式的命令都可以在-exec选项中使用。在下面的例子中我们使用grep命令。find命令首先匹配所有文件名为“passwd*”的文件，例如passwd、passwd.old、passwd.bak，然后执行grep命令看看在这些文件中是否存在一个rounder用户。
$ find /etc -name “passwd*” -exec grep “rounder” {} \;
rounder:JL9TtUqk8EHwc:500:500::/home/apps/nets/rounder:/bin/sh
2.1.14find命令的例子 
我们已经介绍了find命令的基本选项，下面给出find命令的一些其他的例子。
为了匹配$HOME目录下的所有文件，下面两种方法都可以使用：
$ find $HOME -print
$ find ~ -print
为了在当前目录中查找suid置位，文件属主具有读、写、执行权限，并且文件所属组的用户和其他用户具有读和执行的权限的文件，可以用：
$ find . -type  f -perm 4755 -print
为了查找系统中所有文件长度为0的普通文件，并列出它们的完整路径，可以用：
$ find / -type  f -size 0 -exec ls-l {} \;
为了查找/var/logs目录中更改时间在7日以前的普通文件，并删除它们，可以用：
$ find /var/logs  -type f -mtime +7 -exec rm {} \;
为了查找系统中所有属于audit组的文件，可以用：
$ find / -name  -group audit -print
我们的一个审计系统每天创建一个审计日志文件。日志文件名的最后含有数字，这样我们一眼就可以看出哪个文件是最新的，哪个是最旧的。Admin.log文件编上了序号：admin.log.001、admin.log.002等等。下面的find命令将删除/logs目录中访问时间在7日以前、含有数字后缀的admin.log文件。该命令只检查三位数字，所以相应日志文件的后缀不要超过999。
$ find / logs  -name 'admin.log[0-9][0-9]' [-0a-t9i]me  +7 -exec rm {} \;
为了查找当前文件系统中的所有目录并排序，可以用：
$ find . -type  d -print -local -mount | sort
为了查找系统中所有的rmt磁带设备，可以用：
$ find /dev/rmt  -print
2.2xargs
在使用find命令的-exec选项处理匹配到的文件时，find命令将所有匹配到的文件一起传递给exec执行。不幸的是，有些系统对能够传递给exec的命令长度有限制，这样在find命令运行几分钟之后，就会出现溢出错误。错误信息通常是“参数列太长”或“参数列溢出”。这就是xargs命令的用处所在，特别是与find命令一起使用。Find命令把匹配到的文件传递给xargs命令，而xargs命令每次只获取一部分文件而不是全部，不像-exec选项那样。这样它可以先处理最先获取的一部分文件，然后是下一批，并如此继续下去。在有些系统中，使用-exec选项会为处理每一个匹配到的文件而发起一个相应的进程，并非将匹配到的文件全部作为参数一次执行；这样在有些情况下就会出现进程过多，系统性能下降的问题，因而效率不高；而使用xargs命令则只有一个进程。另外，在使用xargs命令时，究竟是一次获取所有的参数，还是分批取得参数，以及每一次获取参数的数目都会根据该命令的选项及系统内核中相应的可调参数来确定。
让我们来看看xargs命令是如何同find命令一起使用的，并给出一些例子。
下面的例子查找系统中的每一个普通文件，然后使用xargs命令来测试它们分别属于哪类文件：
$ find / -type f -print | xargs file
/etc/protocols:  Enghlish text
/etc/securetty:  ASCII test
…
下面的例子在整个系统中查找内存信息转储文件(coredump)，然后把结果保存到/tmp/core.log文件中：
$ find . -name  "core" -print | xargs echo "" >/tmp/core.log
下面的例子在/apps/audit目录下查找所有用户具有读、写和执行权限的文件，并收回相应的写权限：
$ find /apps/audit  -perm -7 -print | xargs chmod o -w
在下面的例子中，我们用grep命令在所有的普通文件中搜索device这个词：
$ find / -type  f -print | xargs grep "device"
在下面的例子中，我们用grep命令在当前目录下的所有普通文件中搜索DBO这个词：
$ find . -name ＊\ -type f -print  | xargs grep "DBO"
注意，在上面的例子中，\用来取消find命令中的*在shell中的特殊含义。
find简单示例
(1) find . -type f -exec ls -l {} \;
解释：查找当前路径下的所有普通文件，并把它们列出来。
(2)find logs -type f -mtime +5 -exec rm {} \;
解释：删除logs目录下更新时间为5日以上的文件。
(3)find . -name "*.log" -mtime +5 -ok rm {} \;
解释：删除当前路径下以。log结尾的五日以上的文件，删除之前要确认。
(4) find ~ -type f -perm 4755 -print
解释：查找$HOME目录下suid位被设置，文件属性为755的文件打印出来。
说明： find在有点系统中会一次性得到将匹配到的文件都传给exec，但是有的系统对exec的命令长度做限制，就会报：”参数列太长“，这就需要使用xargs。xargs是部分取传来的文件。
（5）find / -type f -print |xargs file
解释：xargs测试文件分类
（6）find . -name "core*" -print|xargs echo " ">/tmp/core.log
解释：将core文件信息查询结果报存到core。log日志。
（7）find / -type f -print | xargs chmod o -w
（8）find . -name * -print |xargs grep "DBO"
find用法小结
1. 通过文件的特征查找：
1) 按文件名
find /    -name httpd.conf
find /usr -name httpd.conf
find /etc -name '*srm*'
2) 按大小
find / -size 1500c      # 查找文件大小为1,500 bytes的文件，字符 c 表明这个要查找的文件的大小是以bytes为单位。
find/ -size +10000000c  # "+”是表示要求系统只列出大于指定大小的文件,  "-”表示小于
find / -empty           # 查找在系统中为空的文件或者文件夹
-size：表示文件大小，＋表示大于某个数，－表示小于某个数。c表示单位是字节，你可以将c换成k,M,G。
3) 按时间
find / -amin -10        # 查找在系统中最后10分钟访问的文件
find / -atime -2        # 查找在系统中最后48小时访问的文件
find / -mmin -5         # 查找在系统中最后5分钟里修改过的文件
find / -mtime -1        # 查找在系统中最后24小时里修改过的文件
find / -cmin -5         # 查找在系统中最后5分钟里被改变状态的文件
find / -ctime -1        # 查找在系统中最后24小时里被改变状态的文件
访问过用amin，修改过用mmin，文件状态改变过用cmin
精确到分钟的用amin,mmin,cmin，精确到天的用atime,mtime,ctime
在5分钟之内的用-5，在5分钟以上的用＋5
4) 按用户
find / -user fred       # 查找在系统中属于FRED这个用户的文件
find / -group cat       # 查找在系统中属于 groupcat的文件
find / -nouser          # 查找在系统中属于作废用户的文件
5) 其他
-false 查找系统中总是错误的文件
-fstype type 查找系统中存在于指定文件系统的文件，例如：ext2 .
-gid n 查找系统中文件数字组 ID 为 n的文件
-group gname 查找系统中文件属于gnam文件组，并且指定组和ID的文件
2. 通过文件的特征查找：
Find命令也提供给用户一些特有的选项来控制查找操作。下表就是我们总结出的最基本，最常用的find命令的控制选项及其用法。
选项               用途描述
-daystart     .   .测试系统从今天开始24小时以内的文件，用法类似-amin
-depth             使用深度级别的查找过程方式,在某层指定目录中优先查找文件内容
-follow            遵循通配符链接方式查找; 另外，也可忽略通配符链接方式查询
-maxdepth levels   在某个层次的目录中按照递减方法查找
-mount             不在文件系统目录中查找， 用法类似 -xdev.
-noleaf            禁止在非UNUX文件系统，MS-DOS系统，CD-ROM文件系统中进行最优化查找
-help              显示命令摘要
-version           打印版本数字
使用-follow选项后，find命令则遵循通配符链接方式进行查uuuu找，除非你指定这个选项，否则一般情况下find命令将忽略通配符链接方式进行文件查找。
-maxdepth选项的作用就是限制find命令在目录中按照递减方式查找文件的时候搜索文件超过某个级别或者搜索过多的目录，这样导致查找速度变慢，查找花费的时间过多。例如，我们要在当前(.)目录技巧子目录中查找一个名叫fred的文件，我们可以使用如下命令
find . -maxdepth 2 -name fred
假如这个fred文件在./sub1/fred目录中，那么这个命令就会直接定位这个文件，查找很容易成功。假如，这个文件在./sub1/sub2 /fred目录中，那么这个命令就无法查找到。因为前面已经给find命令在目录中最大的查询目录级别为2，只能查找2层目录下的文件。这样做的目的就是为了让find命令更加精确的定位文件，如果你已经知道了某个文件大概所在的文件目录级数，那么加入-maxdepth n 就很快的能在指定目录中查找成功。
3. 使用混合查找方式：
find /tmp -size +10000000c -and -mtime +2       // -and
find /    -user fred       -or -user george     // -or   在/tmp目录中查找属于fred或者george这两个用户的文件
find /tmp ! -user panda                         // -or   在/tmp目录中查找所有不属于panda的文件
命令就可以解决了。很简单。
查找并显示文件的方法
查找到某个文件是我们的目的，我们更想知道查找到的文件的详细信息和属性，
find / -name "httpd.conf" -ls
下面的表格就是一些常用的查找文件并显示文件信息的参数和使用方法
选项      用途描述
-exec command;   查找并执行命令
-fprint file   打印文件完整文件名
-fprint0 file   打印文件完整文件名包括空的文件
-fprintf file format     打印文件格式
-ok command;             给用户命令执行操作，根据用户的Y 确认输入执行
-printf format           打印文件格式
-ls                      打印同种文件格式的文件.
2. 普通用户无错误查找：
find / -name access_log 2>/dev/null
说明：当普通用户使用"find”命令来查询某些没有相应权限文件目录时（Linux系统中系统管理员ROOT可以把某些文件目录设置成禁止访问模式）
往往会出现"Permissiondenied."（禁止访问）字样。 2>/dev/null就是表明系统将把错误信息输送到stderrstream 2中.
-exec command; 
删除一个目录中的全部文件
cd “目的目录”
find . -name * -exec rm -f {} \;
-exec 参数后面跟的是 command命令，注意如下几点：
1) command命令的终止，使用 ';' (分号）来判定，在后面必须有一个 ';'
出于不明原因， ';'需要用'\'来转义  ,所以命令整体形式为: -exec rm -f {} \;
2) '{}'，使用{}来表示文件名，也就是find前面处理过程中过滤出来的文件，用于command命令进行处理
1.查询所有保护字符串“Hello”的文件
find / -exec grep "Hello" {} \;
2.删除所有临时文件
find / -name "*.tmp" -exec rm -f {} \;
3. 使用混合查找方式：
find /tmp -size +10000000c -and -mtime +2       // -and
find /    -user fred       -or -user george     // -or   在/tmp目录中查找属于fred或者george这两个用户的文件
find /tmp ! -user panda                         // -or   在/tmp目录中查找所有不属于panda的文件
find /tmp !  \( -user 0 -o -user 500 -o -user 501 \) -exec ls -l {} \;
把用户名改成UID就可以了
find命令使用经验
find pathname  -options [-print -exec -ok]
pathname find命令所查找的目录路径。例如用.来表示当前目录，用/来表示系统根目录。
-print find命令将匹配的文件输出到标准输出。
-exec find命令对匹配的文件执行该参数所给出的shell命令。
相应命令的形式为'command'{} \;，注意{}和\；之间的空格。
-ok和-exec的作用相同，只不过以一种更为安全的模式来执行该参数所给出的shell命令，在执行每一个命令之前，都会给出提示，让用户来确定是否执行
文件状态判断:
-mtime: 指定时间文件内容被修改过
-ctime: 指定时间文件权限被修改过
-atime: 指定时间文件被读取过
找出3天“以前”被修改过的文档
# find /var/log/ -mtime +3 -type f -print
找出3天“内”被修改过的文档
# find /var/log/ -mtime -3 -type f -print
找出第3天被修改过的文档.
# find /var/log/ -mtime 3 -type f -print
或这样写：
#find /var/log/ -mtime +2 -mtime -4 -type f -print
注：
访问过用amin，修改过用mmin，文件状态改变过用cmin
精确到分钟的用amin,mmin,cmin，精确到天的用atime,mtime,ctime
xargs - build and execute command lines from standard input
在使用find命令的-exec选项处理匹配到的文件时， find命令将所有匹配到的文件一起传递给exec执行。但有些系统对能够传递给exec的命令长度有限制，这样在find命令运行几分钟之后，就会出现溢出错误。错误信息通常是“参数列太长”或“参数列溢出”。这就是xargs命令的用处所在，特别是与find命令一起使用。
find命令把匹配到的文件传递给xargs命令，而xargs命令每次只获取一部分文件而不是全部，不像-exec选项那样。这样它可以先处理最先获取的一部分文件，然后是下一批，并如此继续下去。
在有些系统中，使用-exec选项会为处理每一个匹配到的文件而发起一个相应的进程，并非将匹配到的文件全部作为参数一次执行；这样在有些情况下就会出现进程过多，系统性能下降的问题，因而效率不高；
而使用xargs命令则只有一个进程。另外，在使用xargs命令时，究竟是一次获取所有的参数，还是分批取得参数，以及每一次获取参数的数目都会根据该命令的选项及系统内核中相应的可调参数来确定。
来看看xargs命令是如何同find命令一起使用的，并给出一些例子。
下面的例子查找系统中的每一个普通文件，然后使用xargs命令来测试它们分别属于哪类文件
#find . -type f -print | xargs file
./.kde/Autostart/Autorun.desktop: UTF-8 Unicode English text
./.kde/Autostart/.directory:      ISO-8859 text\
......
在整个系统中查找内存信息转储文件(core dump) ，然后把结果保存到/tmp/core.log 文件中：
$ find / -name "core" -print | xargs echo "" >/tmp/core.log
上面这个执行太慢，我改成在当前目录下查找
#find . -name "file*" -print | xargs echo "" > /temp/core.log
# cat /temp/core.log
./file6
在当前目录下查找所有用户具有读、写和执行权限的文件，并收回相应的写权限：
# ls -l
drwxrwxrwx    2 sam      adm          4096 10月 30 20:14 file6
-rwxrwxrwx    2 sam      adm             0 10月 31 01:01 http3.conf
-rwxrwxrwx    2 sam      adm             0 10月 31 01:01 httpd.conf
# find . -perm -7 -print | xargs chmod o-w
# ls -l
drwxrwxr-x    2 sam      adm          4096 10月 30 20:14 file6
-rwxrwxr-x    2 sam      adm             0 10月 31 01:01 http3.conf
-rwxrwxr-x    2 sam      adm             0 10月 31 01:01 httpd.conf
用grep命令在所有的普通文件中搜索hostname这个词：
# find . -type f -print | xargs grep "hostname"
./httpd1.conf:#     different IP addresses or hostnames and have them handled by the
./httpd1.conf:# VirtualHost: If you want to maintain multiple domains/hostnames
on your
用grep命令在当前目录下的所有普通文件中搜索hostnames这个词：
# find . -name \* -type f -print | xargs grep "hostnames"
./httpd1.conf:#     different IP addresses or hostnames and have them handled by the
./httpd1.conf:# VirtualHost: If you want to maintain multiple domains/hostnames
on your
注意，在上面的例子中， \用来取消find命令中的*在shell中的特殊含义。
find命令配合使用exec和xargs可以使用户对所匹配到的文件执行几乎所有的命令
使用exec或ok来执行shell命令
使用find时，只要把想要的操作写在一个文件里，就可以用exec来配合find查找，很方便的
在有些操作系统中只允许-exec选项执行诸如l s或ls -l这样的命令。大多数用户使用这一选项是为了查找旧文件并删除它们。建议在真正执行rm命令删除文件之前，最好先用ls命令看一下，确认它们是所要删除的文件。
exec选项后面跟随着所要执行的命令或脚本，然后是一对儿{ }，一个空格和一个\，最后是一个分号。为了使用exec选项，必须要同时使用print选项。如果验证一下find命令，会发现该命令只输出从当前路径起的相对路径及文件名。
例如：为了用ls -l命令列出所匹配到的文件，可以把ls -l命令放在find命令的-exec选项中
# find . -type f -exec ls -l {  } \;
-rw-r--r--    1 root     root        34928 2003-02-25  ./conf/httpd.conf
-rw-r--r--    1 root     root        12959 2003-02-25  ./conf/magic
-rw-r--r--    1 root     root          180 2003-02-25  ./conf.d/README
上面的例子中，find命令匹配到了当前目录下的所有普通文件，并在-exec选项中使用ls -l命令将它们列出。
在/logs目录中查找更改时间在5日以前的文件并删除它们：
$ find logs -type f -mtime +5 -exec rm {  } \;
记住：在shell中用任何方式删除文件之前，应当先查看相应的文件，一定要小心！当使用诸如mv或rm命令时，可以使用-exec选项的安全模式。它将在对每个匹配到的文件进行操作之前提示你。
在下面的例子中， find命令在当前目录中查找所有文件名以.LOG结尾、更改时间在5日以上的文件，并删除它们，只不过在删除之前先给出提示。
$ find . -name "*.conf"  -mtime +5 -ok rm {  } \;
< rm ... ./conf/httpd.conf > ? n
按y键删除文件，按n键不删除。
任何形式的命令都可以在-exec选项中使用。
在下面的例子中我们使用grep命令。find命令首先匹配所有文件名为“ passwd*”的文件，例如passwd、passwd.old、passwd.bak，然后执行grep命令看看在这些文件中是否存在一个sam用户。
# find /etc -name "passwd*" -exec grep "sam" {  } \;
sam:x:501:501::/usr/sam:/bin/bash
find 命令用法
find / -name access_log 2>/dev/null
find /etc -name ‘*srm*’
find / -amin -10 # 查找在系统中最后10分钟访问的文件
find / -atime -2 # 查找在系统中最后48小时访问的文件
find / -mmin -5 # 查找在系统中最后5分钟里修改过的文件
find / -mtime -1 #查找在系统中最后24小时里修改过的文件
find / -cmin -5 # 查找在系统中最后5分钟里被改变状态的文件
find / -ctime -1 #查找在系统中最后24小时里被改变状态的文件
find / -user reda #查找在系统中属于fred这个用户的文件
find / -not -user red #查找在系统中不属于red这个用户的文件
find / -group redagrp # 查找在系统中属于redagrp组的文件
find / -gid 501 #查找系统中属于组id为501的文件
find / -user fred -a -group redagrp
find / -user reda -o -user tracy
find / -nouser #查找在系统中属于作废用户的文件
find / -empty # 查找在系统中为空的文件或者为空的文件夹
find / -false #查找系统中总是错误的文件
find / -size +5k #查找系统中大于5k字节的文件
find / -size +5c #查找系统中大于5字节的文件
find / -perm +6000
find / -type b
文件类型:
b   块(缓冲)设备.
c   字符设备.
d   目录.
p   有名管道(FIFO).
f    规则文件.
l    符号链结.
s    SOCKET.
find / -maxdepth 2 -name fred
find /tmp -size +10000000c -and -mtime +2
find / -user reda -or -user tracy
find /tmp ! -user reda
find / -name "httpd.conf" -ls
find / -user reda -exec ls -l {} \;
find / -user reda -ok #确认后执行
find / -user reda | xargs ls -l
6.2 使用||
使用||的一般形式为： 
命令1 || 命令2
||的作用有一些不同。如果||左边的命令（命令1）未执行成功，那么就执行||右边的命令（命令2）；或者换句话说，“如果这个命令执行失败了|| 那么就执行这个命令”。 
这里有一个使用||的简单例子： 
$ cp wopper.txt wopper.bak ||  echo “if you are seeing this cp failed”
cp: wopper.txt: No such file  or directory
if you are seeing this cp  failed
在上面的例子中，拷贝命令没有能够被成功执行，因此||后面的命令被执行。 
这里有一个更为实用的例子。我希望从一个审计文件中抽取第1个和第5个域，并将其输出到一个临时文件中，如果这一操作未成功，我希望能够收到一个相应邮件： 
$ awk ‘{print $5}’ acc.qtr  > qtr.tmp || echo “Sorry the payroll extraction didn’t work” | mail dave
在这里不只可以使用系统命令；这里我们首先对month_end.txt文件执行了一个名为comet的shell脚本，如果该脚本未执行成功，该shell将结束。 
$ comet month_end.txt || exit
6.3 用（）和{}将命令结合在一起
如果希望把几个命令合在一起执行， shell提供了两种方法。既可以在当前shell也可以在子shell中执行一组命令。 
为了在当前shell中执行一组命令，可以用命令分隔符隔开每一个命令，并把所有的命令用圆括号（）括起来。 
它的一般形式为： 
（命令1;命令2;. . .） 
如果使用{ }来代替（），那么相应的命令将在子shell而不是当前shell中作为一个整体被执行，只有在{ }中所有命令的输出作为一个整体被重定向时，其中的命令才被放到子shell中执行，否则在当前shell执行。它的一般形式为： 
{命令1;命令2;. . . }
我很少单独使用这两种方法。我一般只和&&或||一起使用这两种方法。 
再回到前面那个comet脚本的例子，如果这个脚本执行失败了，我很可能会希望执行两个以上的命令，而不只是一个命令。我可以使用这两种方法。这是原先那个例子： 
$ comet month_end.txt || exit
现在如果该脚本执行失败了，我希望先给自己发个邮件，然后再退出，可以用下面的方法来实现： 
$ comet month_end || (echo “Hello,  guess what! Comet did not work”|mail dave;exit)
在上面的例子中，如果只使用了命令分隔符而没有把它们组合在一起，shell将直接执行最后一个命令（exit）。 
我们再回头来看看前面那个使用&&排序的例子，下面是原来的那个例子： 
$ sort quarter_end.txt >  quarter.sorted && lp quarter.sorted
使用命令组合的方法，如果sort命令执行成功了，可以先将输出文件拷贝到一个日志区，然后再打印。 
6.4 小结
在编写shell脚本时，使用&&和||对构造判断语句非常有用。如果希望在前一个命令执行失败的情况不执行后面的命令，那么本章所讲述的方法非常简单有效。使用这样的方法，可以根据&&或||前面命令的返回值来控制其后面命令的执行。
```

#### 暂未整理二

```sh

一、find 命令格式


1、find命令的一般形式为；

find pathname -options [-print -exec -ok ...]

2、find命令的参数；

pathname: find命令所查找的目录路径。例如用.来表示当前目录，用/来表示系统根目录。
-print： find命令将匹配的文件输出到标准输出。
-exec： find命令对匹配的文件执行该参数所给出的shell命令。相应命令的形式为'command' {} \;，注意{}和\；之间的空格。
-ok： 和-exec的作用相同，只不过以一种更为安全的模式来执行该参数所给出的shell命令，在执行每一个命令之前，都会给出提示，让用户来确定是否执行。

3、find命令选项

-name

按照文件名查找文件。

-perm
按照文件权限来查找文件。

-prune
使用这一选项可以使find命令不在当前指定的目录中查找，如果同时使用-depth选项，那么-prune将被find命令忽略。

-user
按照文件属主来查找文件。

-group
按照文件所属的组来查找文件。

-mtime -n +n
按照文件的更改时间来查找文件， - n表示文件更改时间距现在n天以内，+ n表示文件更改时间距现在n天以前。find命令还有-atime和-ctime 选项，但它们都和-m time选项。

-nogroup
查找无有效所属组的文件，即该文件所属的组在/etc/groups中不存在。

-nouser
查找无有效属主的文件，即该文件的属主在/etc/passwd中不存在。
-newer file1 ! file2

查找更改时间比文件file1新但比文件file2旧的文件。
-type

查找某一类型的文件，诸如：

b - 块设备文件。
d - 目录。
c - 字符设备文件。
p - 管道文件。
l - 符号链接文件。
f - 普通文件。

-size n：[c] 查找文件长度为n块的文件，带有c时表示文件长度以字节计。
-depth：在查找文件时，首先查找当前目录中的文件，然后再在其子目录中查找。
-fstype：查找位于某一类型文件系统中的文件，这些文件系统类型通常可以在配置文件/etc/fstab中找到，该配置文件中包含了本系统中有关文件系统的信息。

-mount：在查找文件时不跨越文件系统mount点。
-follow：如果find命令遇到符号链接文件，就跟踪至链接所指向的文件。
-cpio：对匹配的文件使用cpio命令，将这些文件备份到磁带设备中。
另外,下面三个的区别:

-amin n
查找系统中最后N分钟访问的文件

-atime n
查找系统中最后n*24小时访问的文件

-cmin n
查找系统中最后N分钟被改变文件状态的文件

-ctime n
查找系统中最后n*24小时被改变文件状态的文件

-mmin n
查找系统中最后N分钟被改变文件数据的文件

-mtime n
查找系统中最后n*24小时被改变文件数据的文件

4、使用exec或ok来执行shell命令

使用find时，只要把想要的操作写在一个文件里，就可以用exec来配合find查找，很方便的

在有些操作系统中只允许-exec选项执行诸如l s或ls -l这样的命令。大多数用户使用这一选项是为了查找旧文件并删除它们。建议在真正执行rm命令删除文件之前，最好先用ls命令看一下，确认它们是所要删除的文件。

exec选项后面跟随着所要执行的命令或脚本，然后是一对儿{ }，一个空格和一个\，最后是一个分号。为了使用exec选项，必须要同时使用print选项。如果验证一下find命令，会发现该命令只输出从当前路径起的相对路径及文件名。

例如：为了用ls -l命令列出所匹配到的文件，可以把ls -l命令放在find命令的-exec选项中

# find . -type f -exec ls -l {} \;
-rw-r--r--    1 root     root        34928 2003-02-25  ./conf/httpd.conf
-rw-r--r--    1 root     root        12959 2003-02-25  ./conf/magic
-rw-r--r--    1 root     root          180 2003-02-25  ./conf.d/README
上面的例子中，find命令匹配到了当前目录下的所有普通文件，并在-exec选项中使用ls -l命令将它们列出。
在/logs目录中查找更改时间在5日以前的文件并删除它们：

$ find logs -type f -mtime +5 -exec rm {} \;
记住：在shell中用任何方式删除文件之前，应当先查看相应的文件，一定要小心！当使用诸如mv或rm命令时，可以使用-exec选项的安全模式。它将在对每个匹配到的文件进行操作之前提示你。

在下面的例子中， find命令在当前目录中查找所有文件名以.LOG结尾、更改时间在5日以上的文件，并删除它们，只不过在删除之前先给出提示。

$ find . -name "*.log"  -mtime +5 -ok rm {} \;
< rm ... ./conf/httpd.conf > ? n
按y键删除文件，按n键不删除。

任何形式的命令都可以在-exec选项中使用。

在下面的例子中我们使用grep命令。find命令首先匹配所有文件名为“ passwd*”的文件，例如passwd、passwd.old、passwd.bak，然后执行grep命令看看在这些文件中是否存在一个sam用户。

# find /etc -name "passwd*" -exec grep "sam" {} \;
sam:x:501:501::/usr/sam:/bin/bash

二、find命令的例子；


1、查找当前用户主目录下的所有文件：

下面两种方法都可以使用

$ find $HOME -print
$ find ~ -print

2、让当前目录中文件属主具有读、写权限，并且文件所属组的用户和其他用户具有读权限的文件；

$ find . -type f -perm 644 -exec ls -l {} \;

3、为了查找系统中所有文件长度为0的普通文件，并列出它们的完整路径；

$ find / -type f -size 0 -exec ls -l {} \;

4、查找/var/logs目录中更改时间在7日以前的普通文件，并在删除之前询问它们；

$ find /var/logs -type f -mtime +7 -ok rm {} \;

5、为了查找系统中所有属于root组的文件；

$find . -group root -exec ls -l {} \;
-rw-r--r--    1 root     root          595 10月 31 01:09 ./fie1

6、find命令将删除当目录中访问时间在7日以来、含有数字后缀的admin.log文件。

该命令只检查三位数字，所以相应文件的后缀不要超过999。先建几个admin.log*的文件 ，才能使用下面这个命令

$ find . -name "admin.log[0-9][0-9][0-9]" -atime -7  -ok
rm {} \;
< rm ... ./admin.log001 > ? n
< rm ... ./admin.log002 > ? n
< rm ... ./admin.log042 > ? n
< rm ... ./admin.log942 > ? n

7、为了查找当前文件系统中的所有目录并排序；

$ find . -type d | sort

8、为了查找系统中所有的rmt磁带设备；

$ find /dev/rmt -print

三、xargs

xargs – build and execute command lines from standard input

在使用find命令的-exec选项处理匹配到的文件时， find命令将所有匹配到的文件一起传递给exec执行。但有些系统对能够传递给exec的命令长度有限制，这样在find命令运行几分钟之后，就会出现溢出错误。错误信息通常是“参数列太长”或“参数列溢出”。这就是xargs命令的用处所在，特别是与find命令一起使用。

find命令把匹配到的文件传递给xargs命令，而xargs命令每次只获取一部分文件而不是全部，不像-exec选项那样。这样它可以先处理最先获取的一部分文件，然后是下一批，并如此继续下去。

在有些系统中，使用-exec选项会为处理每一个匹配到的文件而发起一个相应的进程，并非将匹配到的文件全部作为参数一次执行；这样在有些情况下就会出现进程过多，系统性能下降的问题，因而效率不高；

而使用xargs命令则只有一个进程。另外，在使用xargs命令时，究竟是一次获取所有的参数，还是分批取得参数，以及每一次获取参数的数目都会根据该命令的选项及系统内核中相应的可调参数来确定。

来看看xargs命令是如何同find命令一起使用的，并给出一些例子。

下面的例子查找系统中的每一个普通文件，然后使用xargs命令来测试它们分别属于哪类文件

#find . -type f -print | xargs file
./.kde/Autostart/Autorun.desktop: UTF-8 Unicode English text
./.kde/Autostart/.directory:      ISO-8859 text\
......
在整个系统中查找内存信息转储文件(core dump) ，然后把结果保存到/tmp/core.log 文件中：

$ find / -name "core" -print | xargs echo "" >/tmp/core.log
上面这个执行太慢，我改成在当前目录下查找

#find . -name "file*" -print | xargs echo "" > /temp/core.log
# cat /temp/core.log
./file6
在当前目录下查找所有用户具有读、写和执行权限的文件，并收回相应的写权限：

# ls -l
drwxrwxrwx    2 sam      adm          4096 10月 30 20:14 file6
-rwxrwxrwx    2 sam      adm             0 10月 31 01:01 http3.conf
-rwxrwxrwx    2 sam      adm             0 10月 31 01:01 httpd.conf

# find . -perm -7 -print | xargs chmod o-w
# ls -l
drwxrwxr-x    2 sam      adm          4096 10月 30 20:14 file6
-rwxrwxr-x    2 sam      adm             0 10月 31 01:01 http3.conf
-rwxrwxr-x    2 sam      adm             0 10月 31 01:01 httpd.conf
用grep命令在所有的普通文件中搜索hostname这个词：

# find . -type f -print | xargs grep "hostname"
./httpd1.conf:#     different IP addresses or hostnames and have them handled by the
./httpd1.conf:# VirtualHost: If you want to maintain multiple domains/hostnames
on your
用grep命令在当前目录下的所有普通文件中搜索hostnames这个词：

# find . -name \* -type f -print | xargs grep "hostnames"
./httpd1.conf:#     different IP addresses or hostnames and have them handled by the
./httpd1.conf:# VirtualHost: If you want to maintain multiple domains/hostnames
on your
注意，在上面的例子中， \用来取消find命令中的*在shell中的特殊含义。

find命令配合使用exec和xargs可以使用户对所匹配到的文件执行几乎所有的命令。


四、find 命令的参数

下面是find一些常用参数的例子，有用到的时候查查就行了，像上面前几个贴子，都用到了其中的的一些参数，也可以用man或查看论坛里其它贴子有find的命令手册


1、使用name选项

文件名选项是find命令最常用的选项，要么单独使用该选项，要么和其他选项一起使用。

可以使用某种文件名模式来匹配文件，记住要用引号将文件名模式引起来。

不管当前路径是什么，如果想要在自己的根目录$HOME中查找文件名符合*.txt的文件，使用~作为 ‘pathname’参数，波浪号~代表了你的$HOME目录。

$ find ~ -name "*.txt" -print
想要在当前目录及子目录中查找所有的‘ *.txt’文件，可以用：

$ find . -name "*.txt" -print
想要的当前目录及子目录中查找文件名以一个大写字母开头的文件，可以用：

$ find . -name "[A-Z]*" -print
想要在/etc目录中查找文件名以host开头的文件，可以用：

$ find /etc -name "host*" -print
想要查找$HOME目录中的文件，可以用：

$ find ~ -name "*" -print 或find . -print
要想让系统高负荷运行，就从根目录开始查找所有的文件。

$ find / -name "*" -print
如果想在当前目录查找文件名以两个小写字母开头，跟着是两个数字，最后是.txt的文件，下面的命令就能够返回名为ax37.txt的文件：

$find . -name "[a-z][a-z][0--9][0--9].txt" -print

2、用perm选项

按照文件权限模式用-perm选项,按文件权限模式来查找文件的话。最好使用八进制的权限表示法。

如在当前目录下查找文件权限位为755的文件，即文件属主可以读、写、执行，其他用户可以读、执行的文件，可以用：

$ find . -perm 755 -print
还有一种表达方法：在八进制数字前面要加一个横杠-，表示都匹配，如-007就相当于777，-006相当于666

# ls -l
-rwxrwxr-x    2 sam      adm             0 10月 31 01:01 http3.conf
-rw-rw-rw-    1 sam      adm         34890 10月 31 00:57 httpd1.conf
-rwxrwxr-x    2 sam      adm             0 10月 31 01:01 httpd.conf
drw-rw-rw-    2 gem      group        4096 10月 26 19:48 sam
-rw-rw-rw-    1 root     root         2792 10月 31 20:19 temp

# find . -perm 006
# find . -perm -006
./sam
./httpd1.conf
./temp
-perm mode:文件许可正好符合mode

-perm +mode:文件许可部分符合mode

-perm -mode: 文件许可完全符合mode


3、忽略某个目录

如果在查找文件时希望忽略某个目录，因为你知道那个目录中没有你所要查找的文件，那么可以使用-prune选项来指出需要忽略的目录。在使用-prune选项时要当心，因为如果你同时使用了-depth选项，那么-prune选项就会被find命令忽略。

如果希望在/apps目录下查找文件，但不希望在/apps/bin目录下查找，可以用：

$ find /apps -path "/apps/bin" -prune -o -print

4、使用find查找文件的时候怎么避开某个文件目录

比如要在/usr/sam目录下查找不在dir1子目录之内的所有文件

find /usr/sam -path "/usr/sam/dir1" -prune -o -print
find [-path ..] [expression] 在路径列表的后面的是表达式
-path “/usr/sam” -prune -o -print 是 -path “/usr/sam” -a -prune -o
-print 的简写表达式按顺序求值, -a 和 -o 都是短路求值，与 shell 的 && 和 || 类似如果 -path “/usr/sam” 为真，则求值 -prune , -prune 返回真，与逻辑表达式为真；否则不求值 -prune，与逻辑表达式为假。如果 -path “/usr/sam” -a -prune 为假，则求值 -print ，-print返回真，或逻辑表达式为真；否则不求值 -print，或逻辑表达式为真。

这个表达式组合特例可以用伪码写为

if -path "/usr/sam"  then
-prune
else
-print
避开多个文件夹

find /usr/sam \( -path /usr/sam/dir1 -o -path /usr/sam/file1 \) -prune -o -print
圆括号表示表达式的结合。

\ 表示引用，即指示 shell 不对后面的字符作特殊解释，而留给 find 命令去解释其意义。
查找某一确定文件，-name等选项加在-o 之后

#find /usr/sam  \(-path /usr/sam/dir1 -o -path /usr/sam/file1 \) -prune -o -name "temp" -print

5、使用user和nouser选项

按文件属主查找文件，如在$HOME目录中查找文件属主为sam的文件，可以用：

$ find ~ -user sam -print
在/etc目录下查找文件属主为uucp的文件：

$ find /etc -user uucp -print
为了查找属主帐户已经被删除的文件，可以使用-nouser选项。这样就能够找到那些属主在/etc/passwd文件中没有有效帐户的文件。在使用-nouser选项时，不必给出用户名； find命令能够为你完成相应的工作。

例如，希望在/home目录下查找所有的这类文件，可以用：

$ find /home -nouser -print

6、使用group和nogroup选项

就像user和nouser选项一样，针对文件所属于的用户组， find命令也具有同样的选项，为了在/apps目录下查找属于gem用户组的文件，可以用：

$ find /apps -group gem -print
要查找没有有效所属用户组的所有文件，可以使用nogroup选项。下面的find命令从文件系统的根目录处查找这样的文件

$ find / -nogroup-print

7、按照更改时间或访问时间等查找文件

如果希望按照更改时间来查找文件，可以使用mtime,atime或ctime选项。如果系统突然没有可用空间了，很有可能某一个文件的长度在此期间增长迅速，这时就可以用mtime选项来查找这样的文件。

用减号-来限定更改时间在距今n日以内的文件，而用加号+来限定更改时间在距今n日以前的文件。

希望在系统根目录下查找更改时间在5日以内的文件，可以用：

$ find / -mtime -5 -print
为了在/var/adm目录下查找更改时间在3日以前的文件，可以用：

$ find /var/adm -mtime +3 -print

8、查找比某个文件新或旧的文件

如果希望查找更改时间比某个文件新但比另一个文件旧的所有文件，可以使用-newer选项。它的一般形式为：

newest_file_name ! oldest_file_name
其中，！是逻辑非符号。

查找更改时间比文件sam新但比文件temp旧的文件：

例：有两个文件

-rw-r--r--    1 sam      adm             0 10月 31 01:07 fiel
-rw-rw-rw-    1 sam      adm         34890 10月 31 00:57 httpd1.conf
-rwxrwxr-x    2 sam      adm             0 10月 31 01:01 httpd.conf
drw-rw-rw-    2 gem      group        4096 10月 26 19:48 sam
-rw-rw-rw-    1 root     root         2792 10月 31 20:19 temp

# find -newer httpd1.conf  ! -newer temp -ls
1077669    0 -rwxrwxr-x   2 sam      adm             0 10月 31 01:01 ./httpd.conf
1077671    4 -rw-rw-rw-   1 root     root         2792 10月 31 20:19 ./temp
1077673    0 -rw-r--r--   1 sam      adm             0 10月 31 01:07 ./fiel
查找更改时间在比temp文件新的文件：

$ find . -newer temp -print

9、使用type选项

在/etc目录下查找所有的目录，可以用：

$ find /etc -type d -print
在当前目录下查找除目录以外的所有类型的文件，可以用：

$ find . ! -type d -print
在/etc目录下查找所有的符号链接文件，可以用

$ find /etc -type l -print

10、使用size选项

可以按照文件长度来查找文件，这里所指的文件长度既可以用块（block）来计量，也可以用字节来计量。以字节计量文件长度的表达形式为N c；以块计量文件长度只用数字表示即可。

在按照文件长度查找文件时，一般使用这种以字节表示的文件长度，在查看文件系统的大小，因为这时使用块来计量更容易转换。
在当前目录下查找文件长度大于1 M字节的文件：

$ find . -size +1000000c -print
查找当前目录中大于10M的文件：

find . -size +10000k -exec ls -ld {} ;
将find出来的文件复制到另一个地方：

find *.c -exec cp '{}' /tmp ';'
在/home/apache目录下查找文件长度恰好为100字节的文件：

$ find /home/apache -size 100c -print
在当前目录下查找长度超过10块的文件（一块等于512字节）：

$ find . -size +10 -print

11、使用depth选项

在使用find命令时，可能希望先匹配所有的文件，再在子目录中查找。使用depth选项就可以使find命令这样做。这样做的一个原因就是，当在使用find命令向磁带上备份文件系统时，希望首先备份所有的文件，其次再备份子目录中的文件。

在下面的例子中， find命令从文件系统的根目录开始，查找一个名为CON.FILE的文件。

它将首先匹配所有的文件然后再进入子目录中查找。

$ find / -name "CON.FILE" -depth -print

12、使用mount选项

在当前的文件系统中查找文件（不进入其他文件系统），可以使用find命令的mount选项。

从当前目录开始查找位于本文件系统中文件名以XC结尾的文件：

$ find . -name "*.XC" -mount -print

```