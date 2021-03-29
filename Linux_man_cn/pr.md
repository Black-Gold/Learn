# **pr**

## 说明

**pr命令** 用来将文本文件转换成适合打印的格式，它可以把较大的文件分割成多个页面进行打印，并为每个页面添加标题

```markdown
用法：pr [选项] [文件]

Mandatory arguments to long options are mandatory for short options too.
+首页[:末页], --pages=首页[:末页]  在指定的首页/末页处开始/停止打印
-列数, --columns=列数  输出指定的列数。如果指定了-a 选项，则从上到下列印 程序会自动在每一页均衡每列占用的行数
-a, --across    设置每列从上到下输出，配合"-列数"选项一起使用
-c, --show-control-chars
      使用头标(^G)和八进制反斜杠标记
-d, --double-space  加倍输出空白区域
-D, --date-format=格式
      使用遵循指定格式的页眉日期
-e[字符[宽度]], --expand-tabs[=字符[宽度]]
      扩展输入的字符(制表符) 到制表符宽度(8)
-F, -f, --form-feed  使用出纸页页标代替新行作为页面间的分隔符
      (使用-F 选项时报头为3 行,不使用时为5 行)
-h, --header=页眉  在页眉中使用居中的指定字符代替文件名,-h "" 输出一个空行，不要使用 -h""  即为页指定标题
-i[字符[宽度]], --output-tabs[=字符[宽度]]
      使用指定字符(或制表符)代替空格不足到指定制表符宽度(默认8)
-J, --join-lines  合并整个行，关闭-W 选项的行截断，不使用栏调整，使用
        --sep-string[=字符串] 设置分隔符
-l, --length=页长     使用指定页长的行数(默认66)(默认文本行数为56，当启用-F 时为 63)
-m, --merge    在同一行显示所有文件，每个文件占用一栏，分割行，但是当
      使用-J 时将行合并到完整长度
-n[分隔符[位数]], --number-lines[=分隔符[位数]]
      显示行号，使用指定(默认5) 位数，后接分隔符(默认TAB)
      默认从输入文件的第一行开始计数
-N, --first-line-number=数字
      从首页的首行以指定数字开始计数(参看"+首页")
-o, --indent=缩进量
      将每行缩进(默认0)个空格，不影响-w 或-W 参数
      缩进亮的值将被加入页面宽度
-r, --no-file-warnings
      当文件无法打开时忽略警告
-s[CHAR], --separator[=CHAR]
      由单个字符分隔各列，未附加-w 时默认为制表符，否则为空
      另外除非-w 选项被指定，否则"-s[CHAR]"会屏蔽三个列相关
      的截行选项(-COLUMN|-a -COLUMN|-m)
-S[STRING], --sep-string[=STRING]
                  separate columns by STRING,
                  without -S: Default separator <TAB> with -J and <space>
                  otherwise (same as -S" "), no effect on column options
-t, --omit-header  omit page headers and trailers
-T, --omit-pagination
      按照输入文件中的设置忽略页眉和页脚并除去所有分页记号
-v, --show-nonprinting
      使用八进制反斜杠标记
-w, --width=页面宽度
      为多栏页面输出将设置为指定的字符数(默认72)
      仅当-s[char] 选项不启用时有效(即保持默认值 72)
-W, --page-width=页宽
      总是将页宽设置为指定的(默认72)字符数
      除非-J 选项启用总是截断行，此参数与-S 或-s 冲突

如果页长<=10 则使用-t 选项。如果FILE 没有定义，或者FILE 是"-"，则从标准输入读入

```

## 实例

```bash

```
