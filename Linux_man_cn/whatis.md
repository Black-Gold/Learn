## **whatis**

## 说明

**whatis命令** 是用于查询一个命令执行什么功能，并将查询结果打印到终端上。

whatis命令在用`catman -w`命令创建的数据库中查找command参数指定的命令、系统调用、库函数或特殊文件名。whatis命令显示手册部
分的页眉行。然后可以发出man命令以获取附加的信息。whatis命令等同于使用`man -f`命令

## 选项

```markdown
Usage: whatis [OPTION...] 关键词...

  -d, --debug                输出调试信息
  -v, --verbose              输出详细的警告信息
  -r, --regex                把每个关键词都当作正则表达式解读
  -w, --wildcard             关键词里包含通配符
  -l, --long                 不要把输出按终端宽度截断
  -C, --config-file=文件   使用该用户设置文件
  -L, --locale=区域        定义本次搜索所使用的区域设置
  -m, --systems=系统       use manual pages from other systems
  -M, --manpath=路径       设置搜索手册页的路径为“路径”
  -s, --sections=列表, --section=列表
                             search only these sections (colon-separated)
  -?, --help                 give this help list
      --usage                give a short usage message
  -V, --version              print program version

Mandatory or optional arguments to long options are also mandatory or optional
for any corresponding short options.
```



## 实例

```bash
whatis man
: << comment
输出详解：
man                  (1)  - format and display the on-line manual pages
man                  (1p)  - display system documentation
man                  (7)  - macros to format man pages
man                 (rpm) - A set of documentation tools: man, apropos and whatis.
man-pages           (rpm) - Man (manual) pages from the Linux Documentation Project.
man.config [man]     (5)  - configuration data for man

man页面所属的分类标识(常用的是分类1和分类3)

(1)、用户可以操作的命令或者是可执行文件
(2)、系统核心可调用的函数与工具等
(3)、一些常用的函数与数据库
(4)、设备文件的说明
(5)、设置文件或者某些文件的格式
(6)、游戏
(7)、惯例与协议等。例如Linux标准文件系统、网络协议、ASCⅡ，码等说明内容
(8)、系统管理员可用的管理条令
(9)、与内核有关的文件
comment

```


