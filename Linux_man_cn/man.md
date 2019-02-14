man
===

查看Linux中的指令帮助

## 补充说明

**man命令** 是Linux下的帮助指令，通过man指令可以查看Linux中的指令帮助、配置文件帮助和编程帮助等信息。

### 语法  

```

 man [OPTION...] [章节] 手册页...

  -C, --config-file=文件   使用该用户设置文件
  -d, --debug                输出调试信息
  -D, --default              将所有选项都重置为默认值
      --warnings[=警告]    开启 groff 的警告

 主要运行模式：
  -f, --whatis               等同于 whatis
  -k, --apropos              等同于 apropos
  -K, --global-apropos       search for text in all pages
  -l, --local-file
                             把“手册页”参数当成本地文件名来解读
  -w, --where, --path, --location
                             输出手册页的物理位置
  -W, --where-cat, --location-cat
                             输出 cat 文件的物理位置

  -c, --catman               由 catman 使用，用来对过时的 cat
                             页重新排版
  -R, --recode=编码        output source page encoded in ENCODING

 寻找手册页：
  -L, --locale=区域
                             定义本次手册页搜索所采用的区域设置
  -m, --systems=系统       use manual pages from other systems
  -M, --manpath=路径       设置搜索手册页的路径为“路径”

  -S, -s, --sections=列表  使用以半角冒号分隔的章节列表

  -e, --extension=扩展
                             将搜索限制在扩展类型为“扩展”的手册页之内

  -i, --ignore-case          查找手册页时不区分大小写字母
                             (默认)
  -I, --match-case           查找手册页时区分大小写字母。

      --regex                show all pages matching regex
      --wildcard             show all pages matching wildcard

      --names-only           make --regex and --wildcard match page names only,
                             not descriptions

  -a, --all                  寻找所有匹配的手册页
  -u, --update               强制进行缓存一致性的检查

      --no-subpages          don't try subpages, e.g. 'man foo bar' => 'man
                             foo-bar'

 控制格式化的输出：
  -P, --pager=PAGER          使用 PAGER 程序显示输出文本
  -r, --prompt=字符串        给 less pager 提供一个提示行

  -7, --ascii                显示某些 latin1 字符的 ASCII 翻译形式
  -E, --encoding=编码      use selected output encoding
      --no-hyphenation, --nh turn off hyphenation
      --no-justification,                              --nj   turn off justification
  -p, --preprocessor=字符串   字符串表示要运行哪些预处理器：
                             e - [n]eqn, p - pic, t - tbl,
g - grap, r - refer, v - vgrind

  -t, --troff                使用 groff 对手册页排版
  -T, --troff-device[=设备]   使用 groff 的指定设备

  -H, --html[=浏览器]     使用 elinks 或指定浏览器显示 HTML
                             输出
  -X, --gxditview[=分辨率]   使用 groff 并通过 gxditview (X11)
                             来显示：
                             -X = -TX75, -X100 = -TX100, -X100-12 = -TX100-12
  -Z, --ditroff              使用 groff 并强制它生成 ditroff

  -?, --help                 give this help list
      --usage                give a short usage message
  -V, --version              print program version

Mandatory or optional arguments to long options are also mandatory or optional
for any corresponding short options.
```

### 选项  

```
-a：在所有的man帮助手册中搜索；
-f：等价于whatis指令，显示给定关键字的简短描述信息；
-P：指定内容时使用分页程序；
-M：指定man手册搜索的路径。
```

### 参数  

*   数字：指定从哪本man手册中搜索帮助；
*   关键字：指定要搜索帮助的关键字。

### 数字代表内容

```
1：用户在shell环境可操作的命令或执行文件；
2：系统内核可调用的函数与工具等
3：一些常用的函数(function)与函数库(library)，大部分为C的函数库(libc)
4：设备文件说明，通常在/dev下的文件
5：配置文件或某些文件格式
6：游戏(games)
7：惯例与协议等，如Linux文件系统，网络协议，ASCII code等说明
8：系统管理员可用的管理命令
9：跟kernel有关的文件
```

### 实例  

我们输入`man ls`，它会在最左上角显示“LS（1）”，在这里，“LS”表示手册名称，而“（1）”表示该手册位于第一节章，同样，我们输`man ifconfig`它会在最左上角显示“IFCONFIG（8）”。也可以这样输入命令：“man [章节号] 手册名称”。

man是按照手册的章节号的顺序进行搜索的，比如：

```
man sleep
```

只会显示sleep命令的手册,如果想查看库函数sleep，就要输入:

```
man 3 sleep
```




<!-- Linux命令行搜索引擎：https://jaywcjlove.github.io/linux-command/ -->
