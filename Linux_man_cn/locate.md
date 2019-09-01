# **locate**

## 说明

locate 让使用者可以很快速的搜寻档案系统内是否有指定的档案。其方法是先建立一个包括系统内所有档案名称及路径的数据库，之后当寻找时就只需查询这个数据库，而不必实际深入档案系统之中了。在一般的 distribution 之中，数据库的建立都被放在 crontab 中自动执行。

locate命令可以在搜寻数据库时快速找到档案，数据库（/var/lib/locatedb）由updatedb程序来更新，数据库含有本地所有的文件信息，updatedb是由cron daemon周期性建立的，locate命令在搜寻数据库时比由整个由硬盘资料来搜寻资料来得快，但较差劲的是locate所找到的档案若是最近才建立或 刚更名的，可能会找不到，为了避免这种情况，可以在使用locate之前，先使用updatedb命令，手动更新数据库。在内定值中，updatedb每天会跑一次，可以由修改crontab来更新设定值。(etc/crontab)

locate指定用在搜寻符合条件的档案，它会去储存档案与目录名称的数据库内，寻找合乎范本样式条件的档案或目录录，可以使用特殊字元（如”*” 或”?”等）来指定范本样式，如指定范本为kcpa*ner, locate 会找出所有起始字串为kcpa且结尾为ner的档案或目录，如名称为kcpartner若目录录名称为kcpa_ner则会列出该目录下包括 子目录在内的所有档案。

locate指令和find找寻档案的功能类似，但locate是透过update程序将硬盘中的所有档案和目录资料先建立一个索引数据库，在 执行loacte时直接找该索引，查询速度会较快，索引数据库一般是由操作系统管理，但也可以直接下达update强迫系统立即修改索引数据库



```info
Usage: locate [OPTION]... [PATTERN]...      在mlocate数据库中搜索条目
-A,--all              仅打印匹配所有模式的条目
-b,--basename         仅匹配路径名的基本名称
-c,--count            仅打印找到的条目数
-d,--database DBPATH  使用DBPATH而不是默认数据库(即/var/lib/mlocate/mlocate.db)
-e,--existing         仅打印当前现有文件的条目
-L,--follow           检查文件是否存在时跟踪尾随符号链接(default)
-i,--ignore-case      匹配模式时忽略大小写区别
-l,--limit, -n LIMIT  将输出（或计数）限制为LIMIT条目
-m,--mmap             忽略，以便向后兼容
-P,--nofollow, -H     检查文件是否存在时，不要跟随尾随符号链接
-0,--null             在输出上单独输入ZERO
-S,--statistics       不搜索全部，只打印每一个匹配的数据库
-q,--quiet            报告没有关于读取数据库的错误消息，不会显示任何错误讯息
-r,--regexp REGEXP    搜索基本的正则表达式REGEXP而不是模式
   --regex            模式是扩展的正则表达式
-s,--stdio            忽略，以便向后兼容
-w,--wholename        匹配整个路径名(default)

```

## 实例

```bash
locate pwd     # 查找和pwd相关的所有文件数据库
locate /etc/sh     # 搜索etc目录下所有以sh开头的文件
locate -r 'file[^/]*\.txt'  # 使用locate 查找所有符合*file*.txt的文件
```
