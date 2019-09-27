# **grep**

## 说明

**grep**(global search regular expression(RE))and print out the line，全面搜索正则表达式并把行打印出来）是一种强大的文本
搜索工具，它能使用正则表达式搜索文本，并把匹配的行打印出来。用于过滤/搜索的特定字符。可使用正则表达式能多种命令配合使用

grep的工作方式是这样的，它在一个或多个文件中搜索字符串模板。如果模板包括空格，则必须被引用，模板后所有字符串被看作文件名
搜索的结果被送到屏幕，不影响原文件内容

grep可用于shell脚本，因为grep通过返回一个状态值来说明搜索的状态，如果模板搜索成功，则返回0，如果搜索不成功，则返回1，如
果搜索的文件不存在，则返回2。我们利用这些返回值就可进行一些自动化的文本处理工作

```markdown
用法: grep [选项]... PATTERN [FILE]...
在每个 FILE 或是标准输入中查找 PATTERN
默认的 PATTERN 是一个基本正则表达式(缩写为 BRE)
例如: grep -i 'hello world' menu.h main.c

正则表达式选择与解释:
  -E, --extended-regexp     PATTERN 是一个可扩展的正则表达式(缩写为 ERE)
  -F, --fixed-strings       PATTERN 是一组由断行符分隔的定长字符串
  -G, --basic-regexp        PATTERN 是一个基本正则表达式(缩写为 BRE)
  -P, --perl-regexp         PATTERN 是一个 Perl 正则表达式
  -e, --regexp=PATTERN      用 PATTERN 来进行匹配操作
  -f, --file=FILE           从 FILE 中取得 PATTERN
  -i, --ignore-case         忽略大小写
  -w, --word-regexp         强制 PATTERN 仅完全匹配字词
  -x, --line-regexp         强制 PATTERN 仅完全匹配一行
  -z, --null-data           一个 0 字节的数据行，但不是空行

杂项:
  -s, --no-messages         抑制错误消息
  -v, --invert-match        查看没有被匹配的行
  -V, --version             display version information and exit
      --help                display this help text and exit

输出控制:
  -m, --max-count=NUM       NUM 次匹配后停止
  -b, --byte-offset         输出的同时打印字节偏移
  -n, --line-number         输出匹配字符的同时打印行号
      --line-buffered       每行输出清空
  -H, --with-filename       为每一匹配项打印文件名
  -h, --no-filename         输出时不显示文件名前缀
      --label=LABEL         将LABEL 作为标准输入文件名前缀
  -o, --only-matching       仅打印匹配行的匹配（非空白）部分，每个这样的部分位于单独的输出行中
  -q, --quiet, --silent     suppress all normal output,不要向标准输出写任何东西
      --binary-files=TYPE   assume that binary files are TYPE;
                            TYPE is 'binary', 'text', or 'without-match'
  -a, --text                equivalent to --binary-files=text
  -I                        equivalent to --binary-files=without-match
  -d, --directories=ACTION  how to handle directories;
                            ACTION is 'read', 'recurse', or 'skip'
  -D, --devices=ACTION      how to handle devices, FIFOs and sockets;
                            ACTION is 'read' or 'skip'
    如果输入文件是设备，FIFO或套接字，则使用操作来处理它。默认情况下，操作是'读'，这意味着设备的读取就像是普通文件一样。如果行动是'跳跃'，设备，FIFO和套接字默默跳过
  -r, --recursive           like --directories=recurse 递归搜索，包括子目录下的文件
  -R, --dereference-recursive
                            likewise, but follow all symlinks
      --include=FILE_PATTERN
                            search only files that match FILE_PATTERN
      --exclude=FILE_PATTERN
                            skip files and directories matching FILE_PATTERN
      --exclude-from=FILE   skip files matching any file pattern from FILE
      --exclude-dir=PATTERN directories that match PATTERN will be skipped.
  -L, --files-without-match print only names of FILEs containing no match
  -l, --files-with-matches  只打印包含匹配的文件的名称
  -c, --count               只打印每个文件匹配字符串行的数量
  -T, --initial-tab         make tabs line up (if needed)
  -Z, --null                print 0 byte after FILE name

文件控制:
  -B, --before-context=NUM  打印以文本起始的NUM 行
  -A, --after-context=NUM   打印以文本结尾的NUM 行
  -C, --context=NUM         打印输出文本NUM 行
  -NUM                      same as --context=NUM
      --group-separator=SEP use SEP as a group separator
      --no-group-separator  use empty string as a group separator
      --color[=WHEN],
      --colour[=WHEN]       use markers to highlight the matching strings;
                            WHEN is 'always', 'never', or 'auto'
  -U, --binary              do not strip CR characters at EOL (MSDOS/Windows)
  -u, --unix-byte-offsets   report offsets as if CRs were not there
                            (MSDOS/Windows)

‘egrep’即‘grep -E’。‘fgrep’即‘grep -F’
直接使用‘egrep’或是‘fgrep’均已不可行了
egrep是grep的扩展，支持更多的re元字符， fgrep就是fixed grep或fast grep，它们把所有的字母都看作单词，也就是说，正则表达式中的元字符表示回其自身的字面意义，不再特殊
若FILE 为 -，将读取标准输入。不带FILE，读取当前目录，除非命令行中指定了-r选项
如果少于两个FILE 参数，就要默认使用-h 参数
如果有任意行被匹配，那退出状态为 0，否则为 1
如果有错误产生，且未指定 -q 参数，那退出状态为 2
```

## grep可用的规则表达式

```markdown
^         # 锚定行的开始 如：'^grep'匹配所有以grep开头的行
$         # 锚定行的结束 如：'grep$'匹配所有以grep结尾的行
\         # 转义符
.         # 匹配一个非换行符的字符 如：'gr.p'匹配gr后接一个任意字符，然后是p
*         # 匹配零个或多个先前字符 如：'*grep'匹配所有一个或多个空格后紧跟grep的行
.*        # 一起用代表任意字符
[]        # 匹配一个指定范围内的字符，如'[Gg]rep'匹配Grep和grep
[^]       # 匹配一个不在指定范围内的字符，如：'[^A-FH-Z]rep'匹配不包含A-R和T-Z的一个字母开头，紧跟rep的行
\(..\)    # 标记匹配字符，如'\(love\)'，love被标记为1
\<        # 锚定单词的开始，如:'\<grep'匹配包含以grep开头的单词的行
\>        # 锚定单词的结束，如'grep\>'匹配包含以grep结尾的单词的行
x\{m\}    # 重复字符x，m次，如：'0\{5\}'匹配包含5个o的行
x\{m,\}   # 重复字符x,至少m次，如：'o\{5,\}'匹配至少有5个o的行
x\{m,n\}  # 重复字符x，至少m次，不多于n次，如：'o\{5,10\}'匹配5--10个o的行
\w        # 匹配文字和数字字符，即[A-Za-z0-9]，如:'G\w*p'匹配以G后跟零个或多个文字或数字字符，然后是p
\W        # \w的反置形式，匹配一个或多个非单词字符，如点号句号等
\b        # 单词锁定符，如: '\bgrep\b'只匹配grep。  

# POSIX字符类

[:upper:]                   # 表示大写字母[A-Z]
[:lower:]                   # 表示小写字母[a-z]
[:digit:]                   # 表示阿拉伯数字[0-9]
[:alnum:]                   # 表示大小写字母和阿拉伯数字[0-9a-zA-Z]
[:space:]                   # 表示空格或tab键
[:alpha:]                   # 表示大小写字母[a-zA-Z]
[:cntrl:]                   # 表示Ctrl键
[:graph:]或[:print:]        # 表示ASCII码33-126之间的字符

grep    标准grep命令，支持基本正则表达式
egrep   扩展grep命令，支持基本和扩展正则表达式，与grep -E等价
fgrep   快速grep命令，不支持正则表达式，与grep -F等价
```

## grep命令常见用法

```bash
grep MemTotal /proc/meminfo # 查看系统可见的总内存
grep bash /etc/passwd | cut -d: -f1   # 显示系统上使用Bash shell登录的所有用户
ls -algG --time-style=+%s | grep ^[^d] | awk -vlimit=$(date +%s -d '10 hours ago') '$4 > limit { print substr($0, index($0, $4) + length($4) + 1) }'    # 搜索目录下十小时前更改的文件，不包括文件夹，只使用grep实现。(更好的方式用find实现)
grep ^[[:upper:]] test.txt  # 搜索test.txt以大写字母开头的行，POSIX字符类作为模式的用法都类似，使用时注意用方括号将POSIX字符括起来就行了

# 精确匹配单词the的行
grep "\<the\>" test.txt
grep -w the test.txt

grep -E "zh|en" test.txt  # | (或)字符,grep需要加上-E选项才能支持使用它,例：匹配test.txt文件有zh或en的行

# 递归搜索含有某个关键字的文件目录
grep -iHR "关键字" ./*
: << comment
-i 对要搜索的字符忽略大小写
-H 同时打印包括搜索字符串的文件名
-R 递归搜索，当指定的搜索路径是一个目录时，加上-R的搜索会执行递归搜索
comment

grep ^/..../ test.txt   # 搜索文件test.txt以/字符开始，中间任意四个字符，第六个字符为/的行

# 在文件中搜索一个单词，命令会返回一个包含 **“match_pattern”** 的文本行
grep match_pattern file_name
grep "match_pattern" file_name

grep "match_pattern" file_1 file_2 file_3 ...   # 在多个文件中查找match_pattern
grep -v "match_pattern" file_name   # 输出除之外的所有行-v选项
grep "match_pattern" file_name --color=auto   # 标记匹配颜色--color=auto选项

# 使用正则表达式-E选项
grep -E "[1-9]+"
egrep "[1-9]+"

# 只输出文件中匹配到的部分-o选项
echo this is a test line. | grep -o -E "[a-z]+\."
echo this is a test line. | egrep -o "[a-z]+\."

grep -c "text" file_name  # 统计文件或者文本中包含匹配字符串的行数-c选项

# 输出包含匹配字符串的行数-n选项
grep "text" -n file_name
cat file_name | grep "text" -n
grep "text" -n file_1 file_2  # 多个文件

echo gun is not unix | grep -b -o "not"   # 打印样式匹配所位于的字符或字节偏移;一行中字符串的字符便宜是从该行的第一个字符开始计算，起始值为0。选项-b -o一般总是配合使用

grep -l "text" file1 file2 file3...   # 搜索多个文件并查找匹配文本在哪些文件中
grep "text" . -r -n   # 在多级目录中对文本进行递归搜索 .表示当前目录

# 在grep搜索结果中包括或者排除指定文件
grep "main()" . -r --include *.{php,html}   # 只在目录中所有的.php和.html文件中递归搜索字符"main()"
grep "main()" . -r --exclude "README"   # 在搜索结果中排除所有README文件
grep "main()" . -r --exclude-from filelist  # 在搜索结果中排除filelist文件列表里的文件

grep "aaa" file* -lZ | xargs -0 rm  # 使用0值字节后缀的grep与xargs,删除包含aaa字符文件名以file开头的文件，grep输出用-Z选项来指定以0值字节作为终结符文件名（\0），xargs -0 读取输入并用0值字节终结符分隔文件名，然后删除匹配文件，-Z通常和-l结合使用
grep -q "test" filename   # 不会输出任何信息，如果命令运行成功返回0，失败则返回非0值。一般用于条件测试

# 打印出匹配文本之前或者之后的行
seq 10 | grep "example" -A 3  # 显示匹配某个结果之后的3行，使用 -A 选项
grep -A 3 -i "example" demo_text

seq 10 | grep "5" -B 3    # 显示匹配某个结果之前的3行，使用 -B 选项
seq 10 | grep "5" -C 3   # 显示匹配某个结果的前三行和后三行，使用 -C 选项
echo -e "a\nb\nc\na\nb\nc" | grep a -A 1  # 如果匹配结果有多个，会用“--”作为各匹配结果之间的分隔符
```