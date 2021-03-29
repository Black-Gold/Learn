# **rpm**

## 说明

**rpm命令** 是RPM软件包的管理工具。rpm原本是Red Hat Linux发行版专门用来管理Linux各项套件的程序，由于它遵循GPL规则且功能强大方便
因而广受欢迎。逐渐受到其他发行版的采用。RPM套件管理方式的出现，让Linux易于安装，升级，间接提升了Linux的适用度

```markdown

用法: rpm [选项...]

查询/验证软件包选项：
  -a, --all                        查询/验证所有软件包
  -f, --file                       查询/验证文件属于的软件包
  -g, --group                      查询/验证组中的软件包
  -p, --package                    查询/验证一个软件包
  --pkgid                          query/verify package(s) with package identifier
  --hdrid                          query/verify package(s) with header identifier
  --triggeredby                    query the package(s) triggered by the package
  --whatrequires                   query/verify the package(s) which require a dependency
  --whatprovides                   查询/验证提供相关依赖的软件包
  --nomanifest                     不把非软件包文件作为清单处理

查询选项（用 -q 或 --query）：
  -c, --configfiles                列出所有配置文件
  -d, --docfiles                   列出所有程序文档
  -L, --licensefiles               list all license files
  --dump                           转储基本文件信息
  -l, --list                       列出软件包中的文件
  --queryformat=QUERYFORMAT        使用这种格式打印信息
  -s, --state                      显示列出文件的状态

验证选项（用 -V 或 --verify）：
  --nofiledigest                   不验证文件摘要
  --nofiles                        不验证软件包中文件
  --nodeps                         不验证包依赖
  --noscript                       不执行验证脚本

安装/升级/擦除选项：
  --allfiles                       安装全部文件，包含配置文件，否则配置文件会被跳过
  --allmatches                     移除所有符合 <package> 的软件包(如果 <package> 被指定未多个软件包，常常会导致错误出现)
  --badreloc                       对不可重定位的软件包重新分配文件位置
  -e, --erase=<package>+           清除 (卸载) 软件包
  --excludedocs                    不安装程序文档
  --excludepath=<path>             略过以 <path> 开头的文件
  --force                          --replacepkgs --replacefiles 的缩写
  -F, --freshen=<packagefile>+     如果软件包已经安装，升级软件包
  -h, --hash                       软件包安装的时候列出哈希标记 (和 -v 一起使用效果更好)
  --ignorearch                     不验证软件包架构
  --ignoreos                       不验证软件包操作系统
  --ignoresize                     在安装前不检查磁盘空间
  -i, --install                    安装软件包
  --justdb                         更新数据库，但不修改文件系统
  --nodeps                         不验证软件包依赖
  --nofiledigest                   不验证文件摘要
  --nocontexts                     不安装文件的安全上下文
  --noorder                        不对软件包安装重新排序以满足依赖关系
  --noscripts                      不执行软件包脚本
  --notriggers                     不执行本软件包触发的任何脚本
  --nocollections                  请不要执行任何动作集
  --oldpackage                     更新到软件包的旧版本(带 --force 自动完成这一功能)
  --percent                        安装软件包时打印百分比
  --prefix=<dir>                   如果可重定位，便把软件包重定位到 <dir>
  --relocate=<old>=<new>           将文件从 <old> 重定位到 <new>
  --replacefiles                   忽略软件包之间的冲突的文件
  --replacepkgs                    如果软件包已经有了，重新安装软件包
  --test                           不真正安装，只是判断下是否能安装
  -U, --upgrade=<packagefile>+     升级软件包
  --reinstall=<packagefile>+       reinstall package(s)

所有 rpm 模式和可执行文件的通用选项：
  -D, --define=“MACRO EXPR”        定义值为 EXPR 的 MACRO
  --undefine=MACRO                 undefine MACRO
  -E, --eval=“EXPR”                打印 EXPR 的宏展开
  --macros=<FILE:…>                从文件 <FILE:...> 读取宏，不使用默认文件
  --noplugins                      don't enable any plugins
  --nodigest                       不校验软件包的摘要
  --nosignature                    不验证软件包签名
  --rcfile=<FILE:…>                从文件 <FILE:...> 读取宏，不使用默认文件
  -r, --root=ROOT                  使用 ROOT 作为顶级目录 (default: "/")
  --dbpath=DIRECTORY               使用 DIRECTORY 目录中的数据库
  --querytags                      显示已知的查询标签
  --showrc                         显示最终的 rpmrc 和宏配置
  --quiet                          提供更少的详细信息输出
  -v, --verbose                    提供更多的详细信息输出
  --version                        打印使用的 rpm 版本号

Options implemented via popt alias/exec:
  --scripts                        list install/erase scriptlets from package(s)
  --setperms                       set permissions of files in a package
  --setugids                       set user/group ownership of files in a package
  --conflicts                      list capabilities this package conflicts with
  --obsoletes                      list other packages removed by installing this package
  --provides                       list capabilities that this package provides
  --requires                       list capabilities required by package(s)
  --info                           list descriptive information from package(s)
  --changelog                      list change logs for this package
  --xml                            list metadata in xml
  --triggers                       list trigger scriptlets from package(s)
  --last                           list package(s) by install time, most recent first
  --dupes                          list duplicated packages
  --filesbypkg                     list all files from each package
  --fileclass                      list file names with classes
  --filecolor                      list file names with colors
  --fscontext                      list file names with security context from file system
  --fileprovide                    list file names with provides
  --filerequire                    list file names with requires
  --filecaps                       list file names with POSIX1.e capabilities

```

## 实例

```bash
rpm -ivh package.rpm   # 安装rpm包
rpm -ivh --force package.rpm   # 强制安装rpm包
rpm -ivh --nodeps package.rpm   # 忽略依赖安装rpm包
rpm -ivh --replacepkgs package.rpm  # 覆盖安装软件包
rpm -e 包名   # 卸载软件包，包名可以包含版本号等信息，但是不可以有后缀.rpm
rpm -ivh --excludedocs package.rpm # 安装rpm包时不安装帮助文档
rpm -ivh --prefix=/usr/local package.rpm    # 指定软件包安装的路径
rpm -ivh --test package.rpm # 只对软件包安装进行测试，不进行实际的安装
rpm -Uvh  包名    # 升级rpm包
rpm -qa     # 列出所有安装过的包
rpm -q mysql    # 获取mysql软件包全名
rpm -qa --qf '%10{SIZE}\t%{NAME}\n' | sort -k1,1n # 显示所有在rpm发布版上安装的包，并以包字节大小为序
rpm -qd vsftpd  # 查询软件包vsftpd帮助文件
rpm -qdp package.rpm       # 查询未安装的软件包的帮助文件
rpm -qc package.rpm # 查询软件包配置文件

# 有些软件包是以.src.rpm结尾的，这类软件包是包含了源代码的rpm包，在安装时需要进行编译。这类软件包有两种安装方法：
# 方法一：
rpm -i your-package.src.rpm
cd /usr/src/redhat/SPECS
rpmbuild -bp your-package.specs             #一个和你的软件包同名的specs文件
cd /usr/src/redhat/BUILD/your-package/      #一个和你的软件包同名的目录
./configure                                 #这一步和编译普通的源码软件一样，可以加上参数
make
make install

# 方法二：
rpm -i you-package.src.rpm
cd /usr/src/redhat/SPECS
rpmbuild -bb your-package.specs       #一个和你的软件包同名的specs文件
# /usr/src/redhat/RPM/i386/`（根据具体包的不同，也可能是i686,noarch等等）目录下执行安装命令
rpm -i new-package.rpm

# 使用工具rpm2cpio和cpio
rpm2cpio xxx.rpm | cpio -vi
rpm2cpio xxx.rpm | cpio -idmv
rpm2cpio xxx.rpm | cpio --extract --make-directories

# 一个rpm包中包含那些文件
rpm -qlp  **** .rpm     # 没有安装过的软件包
rpm -ql  **** .rpm      # 已经安装过的软件包，还可以使用``

# 获取关于一个软件包的版本，用途等相关信息
rpm -qip  **** .rpm     # 没有安装过的软件包
rpm -qi  **** .rpm      # 已经安装过的软件包

# 查看某个程序是哪个软件包安装的，或者哪个软件包包含这个程序，此方法只适用于可执行程序
rpm -qf `which nginx`       # 返回软件包nginx的全名
rpm -qif `which nginx`      # 返回软件包nginx的有关信息
rpm -qlf `which nginx`      # 返回软件包nginx的文件列表
rpm -qilf `which nginx`     # 同时输出软件包nginx信息和文件列表

# 查看某个文件是哪个软件包安装的，或者哪个软件包包含这个文件，此方法适用于可执行程序和任何普通文件
rpm -qf /usr/bin/ftptop
rpm -qf /var/log/dmesg

```
