# look

## 说明

**look命令** look实用程序显示文件中包含字符串的所有行。 当外观执行二进制搜索时，必须对文件中的行进行排序;如果未指定file，则使用文件/usr/share/dict/words，仅比较字母数字字符，并忽略字母字符的大小写



```info
用法：look [选项] 字符串 [文件]

选项：
-a,--alternative           使用备选词典(字典文件web2,该文件也位于/usr/dict目录下)
-d,--alphanum              只比较字母和数字
-f,--ignore-case           比较时忽略大小写
-t,--terminate <字符>      定义字符串终止字符

字符串：指定要查找的字符串
文件：指定要查找的目标文件
```
