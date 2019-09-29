# **man**

```markdown
用法： man[选项...] [章节] 手册页...
  -C, --config-file=文件            使用该用户设置文件
  -d, --debug                       输出调试信息
  -D, --default                     将所有选项都重置为默认值
      --warnings[=警告]             开启 groff 的警告

 主要运行模式：
  -f, --whatis                      等同于whatis，显示给定关键字的简短描述信息
  -k, --apropos                     等同于apropos
  -K, --global-apropos              search for text in all pages
  -l, --local-file                  把“手册页”参数当成本地文件名来解读
  -w, --where, --path, --location   输出手册页的物理位置
  -W, --where-cat, --location-cat   输出cat文件的物理位置
  -c, --catman                      由catman 使用，用来对过时的cat页重新排版
  -R, --recode=编码                 output source page encoded in ENCODING

 寻找手册页：
  -L, --locale=区域                 定义本次手册页搜索所采用的区域设置
  -m, --systems=系统                use manual pages from other systems
  -M, --manpath=路径                设置搜索手册页的路径为“路径”
  -S, -s, --sections=列表           使用以半角冒号分隔的章节列表
  -e, --extension=扩展              将搜索限制在扩展类型为“扩展”的手册页之内
  -i, --ignore-case                 查找手册页时不区分大小写字母(默认)
  -I, --match-case                  查找手册页时区分大小写字母
      --regex                       show all pages matching regex
      --wildcard                    show all pages matching wildcard
      --names-only                  make --regex and --wildcard match page names only,not descriptions
  -a, --all                         寻找所有匹配的手册页
  -u, --update                      强制进行缓存一致性的检查
      --no-subpages                 don't try subpages, e.g. 'man foo bar' => 'manfoo-bar'

 控制格式化的输出：
  -P, --pager=PAGER                使用 PAGER 程序显示输出文本
  -r, --prompt=字符串               给 less pager 提供一个提示行
  -7, --ascii                      显示某些 latin1 字符的 ASCII 翻译形式
  -E, --encoding=编码              use selected output encoding
      --no-hyphenation, --nh      turn off hyphenation
      --no-justification,--nj     turn off justification
  -p, --preprocessor=字符串        字符串表示要运行哪些预处理器：e - [n]eqn, p - pic, t - tbl,g - grap, r - refer, v - vgrind
  -t, --troff                     使用 groff 对手册页排版
  -T, --troff-device[=设备]        使用 groff 的指定设备
  -H, --html[=浏览器]              使用 www-browser 或指定浏览器显示 HTML输出
  -X, --gxditview[=分辨率]         使用groff并通过 gxditview (X11)来显示：-X = -TX75, -X100 = -TX100, -X100-12 = -TX100-12
  -Z, --ditroff                    使用 groff 并强制它生成 ditroff
```


### 数字所代表内容

1. 用户在shell环境可操作的命令或执行文件
2. 系统内核可调用的函数与工具等
3. 一些常用的函数(function)与函数库(library)，大部分为C的函数库(libc)
4. 设备文件说明，通常在/dev下的文件
5. 配置文件或某些文件格式
6. 游戏(games)
7. 惯例与协议等，如Linux文件系统，网络协议，ASCII code等说明
8. 系统管理员可用的管理命令
9. 跟kernel有关的文件


## 实例

```bash
man -t man | ps2pdf - > man.pdf     # 生成一个PDF格式的帮助文件
man 3 sleep                         # 显示sleep命令的手册并查看库函数sleep
```
