# col

## 说明

**col命令** 是一个标准输入文本过滤器，它从标注输入设备读取文本内容，并把内容显示到标注输出设备。在许多UNIX说明文件里，都有RLF控制字符。
当我们运用shell特殊字符`>`和`>>`，把说明文件的内容输出成纯文本文件时，控制字符会变成乱码，col命令则能有效滤除这些控制字符

## 选项

```markdown
-b, --no-backspaces    不显示空格包括RLF和HRLF
-f, --fine             滤掉RLF字符，但允许将HRLF字符呈现出来
-p, --pass             pass unknown control sequences
-h, --tabs             convert spaces to tabs
-x, --spaces           convert tabs to spaces
-l, --lines NUM        buffer at least NUM lines,预设的内存缓冲区有128列

```


