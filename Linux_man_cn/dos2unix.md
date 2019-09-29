# dos2unix

## 说明

**dos2unix命令** 用来将DOS格式的文本文件转换成UNIX格式的（DOS/MAC to UNIX text file format converter）。DOS下的文本文件是
以`\r\n`作为断行标志的，表示成十六进制就是0D 0A。而Unix下的文本文件是以\n作为断行标志的，表示成十六进制就是0A。DOS格式的文本文件在
Linux底下，用较低版本的vi打开时行尾会显示`^M`，而且很多命令都无法很好的处理这种格式的文件，如果是个shell脚本，。而Unix格式的文本文件
在Windows下用Notepad打开时会拼在一起显示。因此产生了两种格式文件相互转换的需求，对应的将UNIX格式文本文件转成成DOS格式的是unix2dos命令

## 选项

```markdown
-k：保持输出文件的日期不变
-q：安静模式，不提示任何警告信息
-V：查看版本
-c：转换模式，模式有：ASCII, 7bit, ISO, Mac, 默认是：ASCII
-o：写入到源文件
-n：写入到新文件
```

## 实例

```bash
dos2unix file   # 将dos文件file转换为unix文件
dos2unix -n oldfile newfile # 转换为新文件时保留源文件
dos2unix -k -o file1 file2 file3    # 转换多个文件，-o选项可省略
dos2unix -k file    # 转换时保持文件时间戳不变
```


