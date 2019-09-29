# **rename**

## 说明

**rename命令** 用字符串替换的方式批量改变文件名

## 选项

```markdown
rename [选项] 表达式 替换文件...

-v, --verbose    解释正在进行的操作
-s, --symlink    在符号链接上执行
```

## 实例

```bash
rename main1.c main.c main1.c   # 将main1.c重命名为main.c

```

**rename支持通配符**

?  可替代单个字符
*  可替代多个字符
[charset]  可替代charset集中的任意单个字符

文件夹中有这些文件foo1, ..., foo9, foo10, ..., foo278

如果使用`rename foo foo0 foo?`，会把foo1到foo9的文件重命名为foo01到foo09，重命名的文件只是有4个字符长度名称的文件，foo被替换为foo0

如果使用`rename foo foo0 foo??`，foo01到foo99的所有文件都被重命名为foo001到foo099，只重命名5个字符长度名称的文件，foo被替换为foo0

如果使用`rename foo foo0 foo*`，foo001到foo278的所有文件都被重命名为foo0001到foo0278，所有以foo开头的文件都被重命名

如果使用`rename foo0 foo foo0[2]*`，从foo0200到foo0278的所有文件都被重命名为foo200到foo278，文件名中的foo0被替换为foo

**rename支持正则表达式**

```bash
rename "s/AA/aa/" *             # 把文件名中的AA替换成aa
rename "s//.html//.php/" *      # 把.html 后缀的改成 .php后缀
rename "s/$//.txt/" *     # 把所有的文件名都以txt结尾
rename "s//.txt//" *      # 把所有以.txt结尾的文件名的.txt删掉

```


