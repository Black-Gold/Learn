# split

## 说明

**split命令** 可以将一个大文件分割成很多个小文件，有时需要将文件分割成更小的片段，比如为提高可读性，生成日志等

```markdown
-b：，
-C：每一输出档中，单行的最大 byte 数
-d：
-l：
-a：(默认为2)

用法：split [选项] [输入 [前缀]]
输出固定大小的INPUT到PREFIX; 默认大小为1000行，默认PREFIX为“x”。 没有INPUT，或INPUT为 - 时，读取标准输入

-a, --suffix-length=N           指定后缀长度 (default 2)
    --additional-suffix=SUFFIX  append an additional SUFFIX to file names
-b, --bytes=SIZE                值为每一输出档案的大小;单位为 byte
-C, --line-bytes=SIZE           每个输出文件最多放置SIZE字节行数,单行最大byte数
-d, --numeric-suffixes[=FROM]   取代字母，使用数字作为后缀，FROM changes the start value (default 0)
-e, --elide-empty-files         do not generate empty output files with '-n'
    --filter=COMMAND            write to shell COMMAND; file name is $FILE
-l, --lines=NUMBER              值为每一输出档的列数大小
-n, --number=CHUNKS             generate CHUNKS output files; see explanation below
-u, --unbuffered                immediately copy input to output with '-n r/...'
    --verbose		            在每个输出文件打开前输出文件特征


SIZE是一个整数加上可选的单位(例如: 10M is 10*1024*1024)
单位有：K, M, G, T, P, E, Z, Y (powers of 1024) or KB, MB, ... (powers of 1000).

CHUNKS may be:
N       split into N files based on size of input
K/N     output Kth of N to stdout
l/N     split into N files without splitting lines
l/K/N   output Kth of N to stdout without splitting lines
r/N     like 'l' but use round robin distribution
r/K/N   likewise but only output Kth of N to stdout

```

## 实例

```bash
dd if=/dev/zero bs=100k count=1 of=date.file    # 生成一个大小为100KB的测试文件
split -b 10k date.file  # 使用split命令将上面创建的date.file文件分割成大小为10KB的小文件
split -b 10k date.file -d -a 3  # file分割成多个后缀文件，若想用数字后缀可使用-d参数，同时可使用-a length来指定后缀长度
split -b 10k date.file -d -a 3 split_file   # 为分割后的文件指定文件名的前缀

# 使用-l选项根据文件的行数来分割文件，例如把文件分割成每个包含100行的小文件
split -l 100 test.sql -d -a 2 --additional-suffix=.sql test

```
