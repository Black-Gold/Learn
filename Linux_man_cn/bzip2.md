# **bzip2**

## 说明

**bzip2命令** 用于创建和管理（包括解压缩）“.bz2”格式的压缩包。我们遇见Linux压缩打包方法有很多种，以下讲解了Linux压缩打包方法中的Linux bzip2命令的多种范例供大家查看，相信大家看完后会有很多收获



```info
用法: bzip2 [flags and input files in any order]

-d --decompress     强制执行解压缩
-z --compress       强制执行压缩
-k --keep           bzip2在压缩或解压缩后，会删除原始文件。若要保留原始文件，请使用此参数
-f --force          bzip2在压缩或解压缩时，覆盖已存在文件或目录
-t --test           测试.bz2压缩文件的完整性
-c --stdout         将压缩与解压缩的结果送到标准输出
-q --quiet          suppress noncritical error messages
-v --verbose        be verbose (a 2nd -v gives more)
-L --license        显示软件version & license
-V --version        显示软件version & license
-s --small          降低程序执行时内存的使用量(at most 2500k)
-1 .. -9            set block size to 100k .. 900k
--fast              alias for -1
--best              alias for -9

```

## 实例

```sh
# 压缩指定文件filename
bzip2 filename
bzip2 -z filename
# 这里压缩的时候不会输出，会将原来的文件filename给删除，替换成filename.bz2.如果以前有filename.bz2则不会替换并提示错误（如果想要替换则指定-f选项，例如`bzip2 -f filename`；如果filename是目录则也提醒错误不做任何操作；如果filename已经是压过的了有bz2后缀就提醒一下，不再压缩，没有bz2后缀会再次压缩

# 解压指定的文件filename.bz2
bzip2 -d filename.bz2
bunzip2 filename.bz2
# 这里解压的时候没标准输出，会将原来的文件filename.bz2给替换成filename。如果以前有filename则不会替换并提示错误（如果想要替换则指定`-f`选项，例如`bzip2 -df filename.bz2`

# 压缩解压的时候将结果也输出;加上`-v`选项就会输出了,只用压缩举例了，解压的时候同理`bzip2 -dv filename.bz2`
bzip2 -v filename

bzip2 -tv filename.bz2  # 模拟解压实际并不解压
# `-t`指定要进行模拟解压，不实际生成结果，也就是说类似检查文件,当然就算目录下面有filename也不会有什么错误输出了，因为它根本不会真的解压文件。为了在屏幕上输出，这里加上`-v`选项了,如果是真的解压`bzip2 -dv filename.bz2`则输出的是把"ok"替换成了"done"

bzip2 -k filename   # 压缩解压的时候，除了生成结果文件，将原来的文件也保存;加上`-k`就保存原始的文件了，否则原始文件会被结果文件替代。只用压缩举例了，解压的时候同理`$bzip2 -dk filename.bz2`不再举例了

bzip2 -dc filename.bz2  # 解压到标准输出;使用`-c`指定到标准输出，输出的是文件filename的内容，不会将filename.bz2删除
bzip2 -dc dir.tar.bz2 | tar -x  # 展开压缩包,对tar.gz文件使用gzip而不是bzip2

bzip2 -c filename   # 压缩到标准输出;使用`-c`指定压缩到标准输出不删除原有文件，不同的是，压缩后的文件无法输出到标准输出
bzip2 -- -myfilename    # 使用bzip2的时候将所有后面的看作文件(即使文件名以'-'开头);为了防止文件名中`-`产生以为是选项的歧义
```