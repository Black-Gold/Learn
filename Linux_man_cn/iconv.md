# **iconv**

## 说明

**iconv命令** 是用来转换给定文件的编码，比如它可以将UTF8编码的转换成GB18030的编码，反过来也行。JDK中也提供了类似的工具native2ascii。
Linux下的iconv开发库包括iconv_open,iconv_close,iconv等C函数，可以用来在C/C++程序中很方便的转换字符编码，这在抓取网页的程序中很有用处，
而iconv命令在调试此类程序时用得着

```markdown
输入/输出格式规范：
 -f, --from-code=名称     原始文本编码
 -t, --to-code=名称       输出编码

信息：
 -l, --list                 列举所有已知的字符集

输出控制：
 -c                         从输出中忽略无效的字符
 -o, --output=FILE          输出文件
 -s, --silent               关闭警告
     --verbose              打印进度信息
```

## 实例

```bash
iconv -l    # 列出当前支持的字符编码
iconv file1 -f EUC-JP-MS -t UTF-8 -o file2  # 将文件file1转码，转后文件输出到fil2中。没`-o`那么会输出到标准输出
```
