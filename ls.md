warning: CRLF will be replaced by LF in Linux_man_cn/apt-get.md.
The file will have its original line endings in your working directory
warning: CRLF will be replaced by LF in Linux_man_cn/badblocks.md.
The file will have its original line endings in your working directory
warning: CRLF will be replaced by LF in Linux_man_cn/crontab.md.
The file will have its original line endings in your working directory
warning: CRLF will be replaced by LF in Linux_man_cn/gdb.md.
The file will have its original line endings in your working directory
warning: CRLF will be replaced by LF in Linux_man_cn/iostat.md.
The file will have its original line endings in your working directory
warning: CRLF will be replaced by LF in Linux_man_cn/kill.md.
The file will have its original line endings in your working directory
warning: CRLF will be replaced by LF in Linux_man_cn/ldd.md.
The file will have its original line endings in your working directory
warning: CRLF will be replaced by LF in Linux_man_cn/mv.md.
The file will have its original line endings in your working directory
warning: CRLF will be replaced by LF in Linux_man_cn/ps.md.
The file will have its original line endings in your working directory
warning: CRLF will be replaced by LF in Linux_man_cn/screen.md.
The file will have its original line endings in your working directory
warning: CRLF will be replaced by LF in Linux_man_cn/set.md.
The file will have its original line endings in your working directory
warning: CRLF will be replaced by LF in Linux_man_cn/tar.md.
The file will have its original line endings in your working directory
warning: CRLF will be replaced by LF in Linux_man_cn/top.md.
The file will have its original line endings in your working directory
warning: CRLF will be replaced by LF in Linux_man_cn/touch.md.
The file will have its original line endings in your working directory
warning: CRLF will be replaced by LF in Linux_man_cn/vmstat.md.
The file will have its original line endings in your working directory
[1mdiff --git a/Linux_man_cn/apt-get.md b/Linux_man_cn/apt-get.md[m
[1mindex 025c7f7..42e1a42 100644[m
[1m--- a/Linux_man_cn/apt-get.md[m
[1m+++ b/Linux_man_cn/apt-get.md[m
[36m@@ -2,79 +2,38 @@[m
 [m
 ## 说明[m
 [m
[31m-**apt-get命令** 是Debian Linux发行版中的APT软件包管理工具。所有基于Debian的发行都使用这个包管理系统。deb包可以把一个应用的文件包在一起，大体就如同Windows上的安装文件。[m
[32m+[m[32m**apt-get命令** 是Debian Linux发行版中的APT软件包管理工具。所有基于Debian的发行都使用这个包管理系统。deb包可以把一个[m
[32m+[m[32m应用的文件包在一起，大体就如同Windows上的安装文件[m
 [m
[31m-```[m
[31m--c：指定配置文件。[m
[31m-```[m
[31m-[m
[31m-### 参数  [m
[31m-[m
[31m-*   管理指令：对APT软件包的管理操作；[m
[31m-*   软件包：指定要操纵的软件包。[m
[31m-[m
[31m-### 实例  [m
[32m+[m[32m## 选项[m
 [m
[31m-使用apt-get命令的第一步就是引入必需的软件库，Debian的软件库也就是所有Debian软件包的集合，它们存在互联网上的一些公共站点上。把它们的地址加入，apt-get就能搜索到我们想要的软件。/etc/apt/sources.list是存放这些地址列表的配置文件，其格式如下：[m
[32m+[m[32m```markdown[m
 [m
[31m-```[m
[31m-deb web或[ftp地址] [发行版名字] main/contrib/non-[free][m
 ```[m
 [m
[31m-我们常用的Ubuntu就是一个基于Debian的发行，我们使用apt-get命令获取这个列表，以下是我整理的常用命令：[m
[32m+[m[32m## 实例[m
 [m
[31m-在修改`/etc/apt/sources.list`或者`/etc/apt/preferences`之后运行该命令。此外您需要定期运行这一命令以确保您的软件包列表是最新的：[m
[32m+[m[32m```markdown[m
[32m+[m[32m使用apt-get命令的第一步就是引入必需的软件库，Debian的软件库也就是所有Debian软件包的集合，它们存在互联网上的一些公共[m
[32m+[m[32m站点上。把它们的地址加入，apt-get就能搜索到我们想要的软件。/etc/apt/sources.list是存放这些地址列表的配置文件，其格式如下：[m
[32m+[m[32mdeb web或[ftp地址] [发行版名字] main/contrib/non-[free][m
 [m
[31m-```[m
[32m+[m[32m修改`/etc/apt/sources.list`或者`/etc/apt/preferences`之后运行该命令。需要定期运行这一命令以确保您的软件包列表是最新的：[m
 apt-get update[m
 ```[m
 [m
[31m-安装一个新软件包：[m
[31m-[m
[31m-```[m
[31m-apt-get install packagename[m
[31m-```[m
[31m-[m
[31m-卸载一个已安装的软件包（保留配置文件）：[m
[31m-[m
[31m-```[m
[31m-apt-get remove packagename[m
[31m-```[m
[31m-[m
[31m-卸载一个已安装的软件包（删除配置文件）：[m
[31m-[m
[31m-```[m
[31m-apt-get –purge remove packagename[m
[31m-```[m
[31m-[m
[31m-会把已装或已卸的软件都备份在硬盘上，所以如果需要空间的话，可以让这个命令来删除你已经删掉的软件：[m
[31m-[m
[31m-```[m
[31m-apt-get autoclean apt[m
[31m-```[m
[31m-[m
[31m-这个命令会把安装的软件的备份也删除，不过这样不会影响软件的使用的：[m
[31m-[m
[31m-```[m
[31m-apt-get clean[m
[31m-```[m
[31m-[m
[31m-更新所有已安装的软件包：[m
[31m-[m
[31m-```[m
[31m-apt-get upgrade[m
[31m-```[m
[31m-[m
[31m-将系统升级到新版本：[m
[31m-[m
[31m-```[m
[31m-apt-get dist-upgrade[m
[31m-```[m
 [m
[31m-定期运行这个命令来清除那些已经卸载的软件包的.deb文件。通过这种方式，您可以释放大量的磁盘空间。如果您的需求十分迫切，可以使用`apt-get clean`以释放更多空间。这个命令会将已安装软件包裹的.deb文件一并删除。大多数情况下您不会再用到这些.debs文件，因此如果您为磁盘空间不足 而感到焦头烂额，这个办法也许值得一试：[m
[32m+[m[32m```