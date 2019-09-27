# **du**

## 说明

**du命令** 也是查看使用空间的，但是与df命令不同的是Linux du命令是对文件和目录磁盘使用的空间的查看，还是和df命令有一些区别

## 选项

```markdown
-a或-all 显示目录中个别文件的大小
-b或-bytes 显示目录或文件大小时，以byte为单位
-c或--total 除了显示个别目录或文件的大小外，同时也显示所有目录或文件的总和
-k或--kilobytes 以KB(1024bytes)为单位输出
-m或--megabytes 以MB为单位输出
-s或--summarize 仅显示总计，只列出最后加总的值
-h或--human-readable 以K，M，G为单位，提高信息的可读性
-x或--one-file-xystem 以一开始处理时的文件系统为准，若遇上其它不同的文件系统目录则略过
-L<符号链接>或--dereference<符号链接> 显示选项中所指定符号链接的源文件大小
-S或--separate-dirs 显示个别目录的大小时，并不含其子目录的大小
-X<文件>或--exclude-from=<文件> 在<文件>指定目录或文件
--exclude=<目录或文件> 略过指定的目录或文件
-D或--dereference-args 显示指定符号链接的源文件大小
-H或--si 与-h参数相同，但是K，M，G是以1000为换算单位
-l或--count-links 重复计算硬件链接的文件
```

## 实例

```bash
du -sh * | sort -k1,1rh | head -n 10     # 当前目录下所占空间倒序排序前十个

# 统计目录下文件的大小（按M打印显示）
du $1 --max-depth=1 | sort -n|awk '{printf "%7.2fM ----> %s\n",$1/1024,$2}'|sed 's:/.*/\([^/]\{1,\}\)$:\1:g'
```



