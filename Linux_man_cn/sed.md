# **sed**

## 说明

**sed** 是一种流编辑器，它是文本处理中非常中的工具，能够完美的配合正则表达式使用，功能不同凡响。处理时，把当前处理的行存
储在临时缓冲区中，称为“模式空间”（pattern space），接着用sed命令处理缓冲区中的内容，处理完成后，把缓冲区的内容送往屏幕
接着处理下一行，这样不断重复，直到文件末尾。文件内容并没有 改变，除非你使用重定向存储输出。Sed主要用来自动编辑一个或多个
文件；简化对文件的反复操作；编写转换程序等

## 选项

```markdown
用法: sed [选项]   {脚本(如果没有其他脚本)} [输入文件]
-n, --quiet, --silent               取消自动打印模式空间
-e 脚本, --expression=脚本           添加“脚本”到程序的运行列表,指定script处理文本
-f 脚本文件, --file=脚本文件         添加“脚本文件”到程序的运行列表,指定脚本文件处理文本
--follow-symlinks                   直接修改文件时跟随软链接
-i[SUFFIX], --in-place[=SUFFIX]     edit files in place (makes backup if SUFFIX supplied)
-c, --copy        use copy instead of rename when shuffling files in -i mode
-b, --binary      什么也不做，用于与WIN32/CYGWIN/MSDOS/EMX兼容(二进制模式下的打开文件(CR+LF换行符未被特殊对待))
-l N, --line-length=N   指定“l”命令的换行期望长度
--posix                 关闭所有 GNU 扩展
-r, --regexp-extended   在脚本中使用扩展正则表达式
-s, --separate          将输入文件视为各个独立的文件而不是一个长的连续输入
-u, --unbuffered        从输入文件读取最少的数据，更频繁的刷新输出
-z, --null-data         separate lines by NUL characters

如果没有 -e, --expression, -f 或 --file 选项，那么第一个非选项参数被视为
sed脚本。其他非选项参数被视为输入文件，如果没有输入文件，那么程序将从标准
输入读取数据
```

### sed命令

```
a\         在当前行下面插入文本
i\         在当前行上面插入文本
c\         把选定的行改为新的文本
d          删除，删除选择的行
D          删除模板块的第一行
s          替换指定字符
h          拷贝模板块的内容到内存中的缓冲区
H          追加模板块的内容到内存中的缓冲区
g          获得内存缓冲区的内容，并替代当前模板块中的文本
G          获得内存缓冲区的内容，并追加到当前模板块文本的后面
l          列表不能打印字符的清单
n          读取下一个输入行，用下一个命令处理新的行而不是用第一个命令
N          追加下一个输入行到模板块后面并在二者间嵌入一个新行，改变当前行号码
p          打印模板块的行
P          (大写)打印模板块的第一行
q          退出Sed
b lable    分支到脚本中带有标记的地方，如果分支不存在则分支到脚本的末尾
r file     从file中读行
t label    if分支，从最后一行开始，条件一旦满足或者T，t命令，将导致分支到带有标号的命处，或者到脚本的末尾
T label    错误分支，从最后一行开始，一旦发生错误或者T，t命令，将导致分支到带有标号的令处，或者到脚本的末尾
w file     写并追加模板块到file末尾。  
W file     写并追加模板块的第一行到file末尾。  
!          表示后面的命令对所有没有被选定的行发生作用。  
=          打印当前行号码。  
#          把注释扩展到下一个换行符以前。  
```

### sed替换标记

```markdown
g   表示行内全面替换
p   表示打印行
w   表示把行写入一个文件
x   表示互换模板块中的文本和缓冲区中的文本
y   表示把一个字符翻译为另外的字符（但是不用于正则表达式）
\1  子串匹配标记
&   已匹配字符串标记
```

### sed元字符集

```markdown
^          匹配行开始，如：/^sed/匹配所有以sed开头的行
$          匹配行结束，如：/sed$/匹配所有以sed结尾的行
.          匹配一个非换行符的任意字符，如：/s.d/匹配s后接一个任意字符，最后是d
 *         匹配0个或多个字符，如：/*sed/匹配所有模板是一个或多个空格后紧跟sed的行
[]         匹配一个指定范围内的字符，如/[ss]ed/匹配sed和Sed。  
[^]        匹配一个不在指定范围内的字符，如：/[^A-RT-Z]ed/匹配不包含A-R和T-Z的一个字开头，紧跟ed的行
\(..\)     匹配子串，保存匹配的字符，如s/\(love\)able/\1rs，loveable被替换成lovers
&          保存搜索字符用来替换其他字符，如s/love/ & /，love这成 love
\<         匹配单词的开始，如:/\<love/匹配包含以love开头的单词的行
\>         匹配单词的结束，如/love\>/匹配包含以love结尾的单词的行
x\{m\}     重复字符x，m次，如：/0\{5\}/匹配包含5个0的行
x\{m,\}    重复字符x，至少m次，如：/0\{5,\}/匹配至少有5个0的行
x\{m,n\}   重复字符x，至少m次，不多于n次，如：/0\{5,10\}/匹配5~10个0的行
```

## 实例

```bash
ifconfig eth0 | grep "inet addr" | awk -F: '{print $2,$4}'| > awk '{print $1,$3}'   # 只显示IP地址和子网掩码
sed '2d' file       # 删除文件的第2行
sed '2,$d' file     # 删除文件的第2行到末尾所有行
sed '$d' file       # 删除文件最后一行
sed '/^test/'d file # 删除文件中所有开头是test的行
sed 's/book/books/' file        # 替换操作：s命令;替换文本中的字符串
sed 's/^192.168.0.1/&localhost/' file   # 所有以192.168.0.1开头的行都会被替换成它自已加localhost，输出：192.168.0.1localhost
sed -i 's/book/books/g' file    # 直接编辑文件选项-i，会匹配file文件中每一行book,g匹配全部，替换为books
sed -n 's/.*<title\>\.*\<\/title>.*/\1/ip;T;q' file  # 输出HTML文件的<title></title>字段中的 内容
sed -n 's/test/TEST/p' file     # -n选项和p命令一起使用表示只打印那些发生替换的行
sed -n 's/\(love\)able/\1rs/p' file     # love被标记为1，所有loveable会被替换成lovers，并打印出来
sed '/test/r file' filename     # r命令从文件读取，读取file内容并显示在与test匹配的行后，若匹配多行，则显示在所有匹配行后
sed -n '/test/w file' example   # w命令写入文件，在example中所有含有test的行都被写入file中
sed '/^this/i\test line' file   # i\命令表示追加到匹配行的行上面，将test line追加到以this开头的行的行上面
sed '/^this/a\test line' file # a\命令表示追加到匹配行的行下面，将test line追加到以this开头的行下面
sed -i '2a\test line' file  # 在file文件的第二行插入test line
sed -i '5i\test line' file  # 在file文件第5行插入test line
sed '/test/{ n; s/aa/bb/; }' file   # 若匹配到test，则移动到匹配行的下一行，替换这行的aa为bb并打印，接着继续执行
sed '1,10y/abcde/ABCDE/' file   # y变形命令，将1至10行所有abcde转为大写，但正则表达式元字符不能使用该命令
sed '10q' file  # q退出命令，打印完第10行后退出sed命令

# 关闭selinux
sed -i 's/SELINUX=enforcing/SELINUX=disabled/' /etc/selinux/config  # 方法一
setenforce 0    # 方法二

# 禁止root用户远程登录
sed -i 's/#PermitRootLogin yes/PermitRootLogin no/' /etc/ssh/sshd_config

# 已匹配字符串标记&；正则表达式\w\+匹配每一个单词，使用[&]替换它，&对应于之前所匹配到的单词,输出：[this] [is] [a] [test] [line]
echo this is a test line | sed 's/\w\+/[&]/g'

# 子串匹配标记\1；匹配给定样式的其中一部分,输出:this is 7 in a number
echo this is digit 7 in a number | sed 's/digit \([0-9]\)/\1/'

echo sksksksksksk | sed 's/sk/SK/2g' # 从第2个匹配项开始替换；当需要从第N处匹配开始替换时，可以使用/Ng
echo aaa BBB | sed 's/\([a-z]\+\) \([A-Z]\+\)/\2 \1/'   # 输出：BBB aaa

# 字符/在sed中作为定界符使用，也可以使用任意的定界符
sed 's:test:TEXT:g'     # 将test替换成TEXT，此处定界符为:
sed 's|test|TEXT|g'     # 将test替换成TEXT，此处定界符为|
sed 's/\/bin/\/usr\/local\/bin/g'   # 定界符出现在样式内部时，需要进行转义
sed '/test/,/west/s/$/aaa bbb/' file    # 对于模板test和west之间的行，每行的末尾用字符串aaa bbb替换

sed -e '1,5d' -e 's/test/check/' file   # -e选项允许在同一行里执行多条命令,此命令第一条删除1至5行，第二条check替换test
sed --expression='s/test/check/' --expression='/love/d' file    # 和-e 等价的命令是 --expression

sed -e '/test/h' -e '$G' file
: << comment
保持和获取：h命令和G命令
在sed处理文件的时候，每一行都被保存在一个叫模式空间的临时缓冲区中，除非行被删除或者输出被取消，否则所有被处理的行都将 打
印在屏幕上。接着模式空间被清空，并存入新的一行等待处理

此例子里，匹配test的行被找到后，将存入模式空间，h命令将其复制并存入一个称为保持缓存区的特殊缓冲区内。第二条语句的意思是
当到达最后一行后，G命令取出保持缓冲区的行，然后把它放回模式空间中，且追加到现在已经存在于模式空间中的行的末尾。此例中就
是追加到最后一行。简单来说，任何包含test的行都被复制并追加到该文件的末尾
comment

sed -e '/test/h' -e '/check/x' file
: << comment
保持和互换：h命令和x命令  
互换模式空间和保持缓冲区的内容。此例也就是把包含test与check的行互换
comment

: << comment
# 脚本scriptfile
sed [options] -f scriptfile file(s)

sed脚本是一个sed的命令清单，启动Sed时以-f选项引导脚本文件名。Sed对于脚本中输入的命令非常挑剔，在命令的末尾不能有任何空白
或文本，如果在一行中有多个命令，要用分号分隔。以#开头的行为注释行，且不能跨行
comment

# 打印奇数行或偶数行
# 方法1：
sed -n 'p;n' test.txt  #奇数行
sed -n 'n;p' test.txt  #偶数行

# 方法2：
sed -n '1~2p' test.txt  #奇数行
sed -n '2~2p' test.txt  #偶数行

# 打印匹配字符串的下一行
grep -A 1 SCC URFILE
sed -n '/SCC/{n;p}' URFILE
awk '/SCC/{getline; print}' URFILE
```

### sed one line

#### 文本间隔

```bash
sed G   # 在每行后增加一空行
sed '/^$/d' file    # 删除操作：d命令；删除空白行
sed '/^ *#/d; /^ *$/d'  # 删除空白行和注释
sed '/^$/d;G' # 将原来的所有空行删除并在每一行后面增加一空行,这样在输出的文本中每一行后面将有且只有一空行
sed 'G;G'   # 在每一行后面增加两行空行
sed 'n;d'   # 将第一个脚本所产生的所有空行删除（即删除所有偶数行）
sed '/regex/{x;p;x;}'   # 在匹配式样“regex”的行之前插入一空行
sed '/regex/G'  # 在匹配式样“regex”的行之后插入一空行
sed '/regex/{x;p;x;G;}' # 在匹配式样“regex”的行之前和之后各插入一空行
```

#### 编号

```bash

sed = filename | sed 'N;s/\n/\t/'   # 对每行进行编号（简单的左对齐方式）使用制表符tab而不是空格来对齐边缘
sed = filename | sed 'N; s/^/     /; s/ *\(.\{6,\}\)\n/\1  /'   # 对文件中的所有行编号（行号在左，文字右端对齐）
sed '/./=' filename | sed '/./N; s/\n/ /'   # 对文件中的所有行编号，但只显示非空白行的行号
sed -n '$=' # 计算行数 （模拟 "wc -l"）
```

#### 文本转换和替换

```bash
# Unix环境：转换DOS的新行符（CR/LF）为Unix格式
sed 's/.$//'                     # 假设所有行以CR/LF结束
sed 's/^M$//'                    # 在bash/tcsh中，将按Ctrl-M改为按Ctrl-V
sed 's/\x0D$//'                  # ssed、gsed 3.02.80，及更高版本
sed 's/^[ \t]*//'   # 将每一行前面的空白字符（空格，制表符）删除使其左对齐
sed 's/[ \t]*$//'   # 将每一行尾部的空白字符（空格，制表符）删除
sed 's/^[ \t]*//;s/[ \t]*$//'   # 将每一行中的前导和拖尾的空白字符删除
sed -e :a -e 's/^.\{1,78\}$/ &/;ta'  # 78个字符外加最后的一个空格,以79个字符为宽度，将所有文本右对齐
sed '/\n/!G;s/\(.\)\(.*\n\)/&\2\1/;//D;s/.//'   # 将行中的字符逆序排列，第一个字成为最后一字，……（模拟“rev”）
sed '$!N;s/\n/ /'   # 将每两行连接成一行（类似“paste”）
sed -e :a -e '/\\$/N; s/\\\n//; ta' # 如果当前行以反斜杠“\”结束，则将下一行并到当前行末尾并去掉原来行尾的反斜杠
sed -e :a -e '$!N;s/\n=/ /;ta' -e 'P;D' # 如果当前行以等号开头，将当前行并到上一行末尾并以单个空格代替原来行头的“=”
sed ':a; /\\$/N; s/\\\n//; ta'  # 连接结尾有\符号的行和其下一行
sed '/baz/s/foo/bar/g'  # 只在行中出现字串“baz”的情况下将“foo”替换成“bar”
sed '/baz/!s/foo/bar/g' # 将“foo”替换成“bar”，并且只在行中未出现字串“baz”的情况下替换
gsed -r ':a;s/(^|[^0-9.])([0-9]+)([0-9]{3})/\1\2,\3/g;ta'   # 为带有小数点和负号的数值增加逗号分隔符（GNU sed）
sed 's/\[\\`\\"$\\\\]\/\\\1/g'  # 在所有转义字符之前添加\符号

# Unix环境：转换Unix的新行符（LF）为DOS格式
sed "s/$/`echo -e \\\r`/"        # 在ksh下所使用的命令
sed 's/$'"/`echo \\\r`/"         # 在bash下所使用的命令
sed "s/$/`echo \\\r`/"           # 在zsh下所使用的命令
sed 's/$/\r/'                    # gsed 3.02.80 及更高版本

# DOS环境：转换Unix新行符（LF）为DOS格式
sed "s/$//"                      # 方法 1
sed -n p                         # 方法 2

# DOS环境：转换DOS新行符（CR/LF）为Unix格式。要识别UnxUtils版本的sed可以通过其特有的“--text”选项。看其中有无一个
# “--text”项以此来判断所使用的是否是UnxUtils版本,其它DOS版本的的sed则无法进行这一转换。但可以用“tr”来实现这一转换
sed "s/\r//" infile >outfile     # UnxUtils sed v4.0.7 或更高版本
tr -d \r <infile >outfile        # GNU tr 1.22 或更高版本

# 以79个字符为宽度，使所有文本居中。在方法1中，为了让文本居中每一行的前头和后头都填充了空格。 在方法2中，在居中文本的过
# 程中只在文本的前面填充空格，并且最终这些空格将有一半会被删除。此外每一行的后头并未填充空格
sed  -e :a -e 's/^.\{1,77\}$/ & /;ta'                     # 方法1
sed  -e :a -e 's/^.\{1,77\}$/ &/;ta' -e 's/\( *\)\1/\1/'  # 方法2

# 在每一行中查找字串“foo”，并将找到的“foo”替换为“bar”
sed 's/foo/bar/'  # 只替换每一行中的第一个“foo”字串
sed 's/foo/bar/4' # 只替换每一行中的第四个“foo”字串
sed 's/foo/bar/g' # 将每一行中的所有“foo”都换成“bar”
sed 's/\(.*\)foo\(.*foo\)/\1bar\2/' # 替换倒数第二个“foo”
sed 's/\(.*\)foo/\1bar/'  # 替换最后一个“foo”

# 不管是“scarlet”“ruby”还是“puce”，一律换成“red”
sed 's/scarlet/red/g;s/ruby/red/g;s/puce/red/g'  # 对多数的sed都有效
gsed 's/scarlet\|ruby\|puce/red/g'               # 只对GNU sed有效

# 倒置所有行，第一行成为最后一行，依次类推（模拟“tac”）。由于某些原因，使用下面命令时HHsed v1.5会将文件中的空行删除
sed '1!G;h;$!d'      # 方法1
sed -n '1!G;h;$p'    # 方法2

# 为数字字串增加逗号分隔符号，将“1234567”改为“1,234,567”
gsed ':a;s/\B[0-9]\{3\}\>/,&/;ta'                     # GNU sed
sed -e :a -e 's/\(.*[0-9]\)\([0-9]\{3\}\)/\1,\2/;ta'  # 其他sed

# 在每5行后增加一空白行 （在第5，10，15，20，等行后增加一空白行）
gsed '0~5G'                      # 只对GNU sed有效
sed 'n;n;n;n;G;'                 # 其他sed

```

#### 选择性显示特定行

```bash
sed 10q # 显示文件中的前10行 （模拟“head”的行为）
sed q   # 显示文件中的第一行 （模拟“head -1”命令）
sed -e :a -e '$q;N;11,$D;ba'    # 显示文件中的最后10行 （模拟“tail”）
sed '$!N;$!D'   # 显示文件中的最后2行（模拟“tail -2”命令）
sed -n '/regexp/{g;1!p;};h' # 查找“regexp”并将匹配行的上一行显示出来，但并不显示匹配行
sed -n '/regexp/{n;p;}' # 查找“regexp”并将匹配行的下一行显示出来，但并不显示匹配行
sed '/AAA/!d; /BBB/!d; /CCC/!d'  # 字串的次序不影响结果,显示包含“AAA”、“BBB”或“CCC”的行（任意次序）
sed '/AAA.*BBB.*CCC/!d' # 显示包含“AAA”、“BBB”和“CCC”的行（固定次序）
sed -e '/./{H;$!d;}' -e 'x;/AAA/!d;'    # 显示包含“AAA”的段落 （段落间以空行分隔）
sed -e '/./{H;$!d;}' -e 'x;/AAA/!d;/BBB/!d;/CCC/!d' # 显示包含“AAA”“BBB”和“CCC”三个字串的段落 （任意次序）
sed -e '/./{H;$!d;}' -e 'x;/AAA/b' -e '/BBB/b' -e '/CCC/b' -e d # 显示包含AAA、BBB、CCC三者中任一字串的段落（任意次序）
sed -n '/^.\{65\}/p'    # 显示包含65个或以上字符的行
sed -n '/regexp/,$p'    # 显示部分文本——从包含正则表达式的行开始到最后一行结束
sed -n '/Iowa/,/Montana/p'       # 区分大小写方式,显示两个正则表达式之间的文本（包含）

# 显示文件中的最后一行（模拟“tail -1”）
sed '$!d'                        # 方法1
sed -n '$p'                      # 方法2

# 显示文件中的倒数第二行
sed -e '$!{h;d;}' -e x              # 当文件中只有一行时，输入空行
sed -e '1{$q;}' -e '$!{h;d;}' -e x  # 当文件中只有一行时，显示该行
sed -e '1{$d;}' -e '$!{h;d;}' -e x  # 当文件中只有一行时，不输出

# 只显示匹配正则表达式的行（模拟“grep”）
sed -n '/regexp/p'               # 方法1
sed '/regexp/!d'                 # 方法2

# 只显示“不”匹配正则表达式的行（模拟“grep -v”）
sed -n '/regexp/!p'              # 方法1，与前面的命令相对应
sed '/regexp/d'                  # 方法2，类似的语法

# 显示包含“regexp”的行及其前后行，并在第一行之前加上“regexp”所在行的行号 （类似“grep -A1 -B1”）
sed -n -e '/regexp/{=;x;1!p;g;$!N;p;D;}' -e h

# 显示包含“AAA”“BBB”或“CCC”的行 （模拟“egrep”）
sed -e '/AAA/b' -e '/BBB/b' -e '/CCC/b' -e d    # 多数sed
gsed '/AAA\|BBB\|CCC/!d'                        # 对GNU sed有效

# 显示包含65个以下字符的行
sed -n '/^.\{65\}/!p'            # 方法1，与上面的脚本相对应
sed '/^.\{65\}/d'                # 方法2，更简便一点的方法

# 显示部分文本——指定行号范围（从第8至第12行，含8和12行）
sed -n '8,12p'                   # 方法1
sed '8,12!d'                     # 方法2

# 显示第52行
sed -n '52p'                     # 方法1
sed '52!d'                       # 方法2
sed '52q;d'                      # 方法3, 处理大文件时更有效率

# 从第3行开始，每7行显示一次
gsed -n '3~7p'                   # 只对GNU sed有效
sed -n '3,${p;n;n;n;n;n;n;}'     # 其他sed

```

#### 选择性的删除特定行

```bash
sed '/Iowa/,/Montana/d' # 显示通篇文档，除了两个正则表达式之间的内容
sed '$!N; /^\(.*\)\n\1$/!P; D'  # 删除文件中相邻的重复行（模拟“uniq”）只保留重复行中的第一行，其他行删除
sed -n 'G; s/\n/&&/; /^\([ -~]*\n\).*\n\1/d; s/\n//; h; P'  # 删除文件重复行不管有无相邻。注意hold space能支持缓存大小
sed '$!N; s/^\(.*\)\n\1$/\1/; t; D' # 删除除重复行外的所有行（模拟“uniq -d”）
sed '1,10d' # 删除文件中开头的10行
sed '$d'    # 删除文件中的最后一行
sed 'N;$!P;$!D;$d'  # 删除文件中的最后两行
sed '/^$/N;/\n$/N;//D'  # 只保留多个相邻空行的前两行
sed '/./,$!d'   # 删除文件顶部的所有空行
sed '/pattern/d'                      # 删除含pattern的行。当然pattern可以换成任何有效的正则表达式
sed -n '/^$/{p;h;};/./{x;/./p;}'    # 删除每个段落的最后一行

# 删除文件中的最后10行
sed -e :a -e '$d;N;2,10ba' -e 'P;D'   # 方法1
sed -n -e :a -e '1,10!{P;N;D;};N;ba'  # 方法2

# 删除8的倍数行
gsed '0~8d'                           # 只对GNU sed有效
sed 'n;n;n;n;n;n;n;d;'                # 其他sed

# 删除文件中的所有空行（与“grep '.' ”效果相同）
sed '/^$/d'                           # 方法1
sed '/./!d'                           # 方法2

# 只保留多个相邻空行的第一行。并且删除文件顶部和尾部的空行。（模拟“cat -s”）
sed '/./,/^$/!d'        #方法1，删除文件顶部的空行，允许尾部保留一空行
sed '/^$/N;/\n$/D'      #方法2，允许顶部保留一空行，尾部不留空行

# 删除文件尾部的所有空行
sed -e :a -e '/^\n*$/{$d;N;ba' -e '}'  # 对所有sed有效
sed -e :a -e '/^\n*$/N;/\n$/ba'        # 同上，但只对 gsed 3.02.*有效
```

#### 特殊应用

```bash
# 移除手册页（man page）中的nroff标记。在Unix System V或bash shell下使用'echo'命令时可能需要加上 -e 选项
sed "s/.`echo \\\b`//g"    # 外层的双括号是必须的（Unix环境）
sed 's/.^H//g'             # 在bash或tcsh中, 按 Ctrl-V 再按 Ctrl-H
sed 's/.\x08//g'           # sed 1.5，GNU sed，ssed所使用的十六进制的表示方法
sed '/^$/q'                # 删除第一行空行后的所有内容，可用于提取新闻组或 e-mail 的邮件头
sed '1,/^$/d'              # 删除第一行空行之前的所有内容,可用于提取新闻组或e-mail的正文部分
sed '/^Subject: */!d; s///;q'  # 从邮件头提取“Subject”（标题栏字段），并移除开头的“Subject:”字样
sed '/^Reply-To:/q; /^From:/h; /./d;g;q' # 从邮件头获得回复地址 
sed 's/ *(.*)//; s/>.*//; s/.*[:<] *//' # 获取邮件地址。在上一个脚本所产生的那一行邮件头的基础上进一步的将非电邮地址的部分剃除。（见上一脚本）
sed 's/^/> /' # 在每一行开头加上一个尖括号和空格（引用信息）
sed 's/^> //' # 将每一行开头处的尖括号和空格删除（解除引用）
sed -e :a -e 's/<[^>]*>//g;/</N;//ba' # 移除大部分的HTML标签（包括跨行标签）

# 将分成多卷的uuencode文件解码。移除文件头信息，只保留uuencode编码部分。文件必须以特定顺序传给sed。下面第一种版本的脚本
# 可以直接在命令行下输入
# 第二种版本则可以放入一个带执行权限的shell脚本中。（由Rahul Dhesi的一个脚本修改而来。）
sed '/^end/,/^begin/d' file1 file2 ... fileX | uudecode   # vers1
sed '/^end/,/^begin/d' "$@" | uudecode                    # vers2

# 将文件中的段落以字母顺序排序。段落间以（一行或多行）空行分隔。GNU sed使用字元“\v”来表示垂直制表符，这里用它来作为换
# 行符的占位符——当然你也可以用其他未在文件中使用的字符来代替它
sed '/./{H;d;};x;s/\n/={NL}=/g' file | sort | sed '1s/={NL}=//;s/={NL}=/\n/g'
gsed '/./{H;d};x;y/\n/\v/' file | sort | sed '1s/\v//;y/\v/\n/'

# 分别压缩每个.TXT文件，压缩后删除原来的文件并将压缩后的.ZIP文件命名为与原来相同的名字（只是扩展名不同）
# （DOS环境：“dir /b”显示不带路径的文件名）
echo @echo off >zipup.bat
dir /b *.txt | sed "s/^\(.*\)\.TXT/pkzip -mo \1 \1.TXT/" >>zipup.bat

: << comment
使用SED：Sed接受一个或多个编辑命令，并且每读入一行后就依次应用这些命令。当读入第一行输入后，sed对其应用所有的命令，然后
将结果输出。接着再读入第二行输入，对其应用所有的命令……并重复这个过程。上一个例子中sed由标准输入设备（即命令解释器，通
常是以管道输入的形式）获得输入。在命令行给出一个或多个文件名作为参数时，这些文件取代标准输入设备成为sed的输入。sed的输出
将被送到标准输出（显示器）。因此：
comment
cat filename | sed '10q'         # 使用管道输入
sed '10q' filename               # 同样效果，但不使用管道输入
sed '10q' filename > newfile     # 将输出转移（重定向）到磁盘上

```

#### 其他

```bash
# 速度优化：当由于某种原因（比如输入文件较大、处理器或硬盘较慢等）需要提高命令执行速度时，可以考虑在替换命令（s/.../.../）
# 前面加上地址表达式来提高速度。举例来说：
sed 's/foo/bar/g' filename         # 标准替换命令
sed '/foo/ s/foo/bar/g' filename   # 速度更快
sed '/foo/ s//bar/g' filename      # 简写形式

# 只需显示文件前面的部分或需要删除后面的内容时，可以在脚本中使用q命令（退出命令）。在处理大文件时，会节省大量时间。因此：
sed -n '45,50p' filename           # 显示第45到50行
sed -n '51q;45,50p' filename       # 一样，但快得多

sed -n '1000p;1000q'    # 输出第一千行
sed -n '10,20p;20q'     # 输出第10-20行

```
