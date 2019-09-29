# zipinfo

## 说明

**zipinfo命令** 用来列出压缩文件信息。执行zipinfo指令可得知zip压缩文件的详细信息

## 选项

```markdown
-1：只列出文件名称
-2：此参数的效果和指定“-1”参数类似，但可搭配“-h”，“-t”和“-z”参数使用
-h：只列出压缩文件的文件名称
-l：此参数的效果和指定“-m”参数类似，但会列出原始文件的大小而非每个文件的压缩率
-m：此参数的效果和指定“-s”参数类似，但多会列出每个文件的压缩率
-M：若信息内容超过一个画面，则采用类似more指令的方式列出信息
-s：用类似执行“ls-l”指令的效果列出压缩文件内容
-t：只列出压缩文件内所包含的文件数目，压缩前后的文件大小及压缩率
-T：将压缩文件内每个文件的日期时间用年，月，日，时，分，秒的顺序列出
-v：详细显示压缩文件内每一个文件的信息
-x<范本样式>：不列出符合条件的文件的信息
-z：如果压缩文件内含有注释，就将注释显示出来

main listing-format options:             -s  short Unix "ls -l" format (def.)
  -1  filenames ONLY, one per line       -m  medium Unix "ls -l" format
  -2  just filenames but allow -h/-t/-z  -l  long Unix "ls -l" format
                                         -v  verbose, multi-page format
miscellaneous options:
  -h  print header line       -t  print totals for listed files or for all
  -z  print zipfile comment  -TM print file times in sortable decimal format
 -CJ be case-insensitive   20 April 2009  -U  use escapes for all non-ASCII Unicode
  -x  exclude filenames that follow from listing
  -O CHARSET  specify a character encoding for DOS, Windows and OS/2 archives
  -I CHARSET  specify a character encoding for UNIX and other archives


```



