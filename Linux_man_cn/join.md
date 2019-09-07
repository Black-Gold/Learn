# join

## 说明

**join命令** 用来将两个文件中，制定栏位内容相同的行连接起来。找出两个文件中，指定栏位内容相同的行，并加以合并，再输出到
标准输出设备

## 选项

```markdown
-a FILENUM              除了显示原来的输出内容之外，还显示指令文件中没有相同栏位的行
-e EMPTY                若[文件1]与[文件2]中找不到指定的栏位，则在输出中填入选项中的字符串
-i, --ignore-case       比较栏位内容时，忽略大小写的差异
-j FIELD                equivalent to '-1 FIELD -2 FIELD'
-o FORMAT               按照指定的格式来显示结果
-t CHAR                 使用栏位的分割字符
-v 文件编号        	    类似 -a 文件编号，但禁止组合输出行
-1 域          	        在文件1 的此域组合
-2 域          	        在文件2 的此域组合
--check-order     	    检查输入行是否正确排序，即使所有输入行均是成对的
--nocheck-order   	    不检查输入是否正确排序
--header          	    将首行视作域的头部，直接输出而不对其进行匹配
-z, --zero-terminated	以0 字节而非新行作为行尾标志

```

## 实例

```bash
# 以下如果是英文文本的话export LANG=C可以提高速度
join -t'\0' -a1 -a2 file1 file2     # 两个有序文件的并集
join -t'\0' file1 file2             # 两个有序文件的交集
join -t'\0' -v2 file1 file2         # 两个有序文件的差集
join -t'\0' -v1 -v2 file1 file2     # 两个有序文件的对称差集

```
