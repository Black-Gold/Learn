# **xz**

## 说明

**xz命令** XZ Utils 是为 POSIX 平台开发具有高压缩率的工具。它使用 LZMA2 压缩算法，生成的压缩文件比 POSIX 平台传统使用的
gzip、bzip2 生成的压缩文件更小，而且解压缩速度也很快。最初 XZ Utils 的是基于 LZMA-SDK 开发，但是 LZMA-SDK 包含了一些
WINDOWS平台的特性，所以 XZ Utils 为以适应 POSIX 平台作了大幅的修改。XZ Utils 的出现也是为了取代 POSIX 系统中旧的 LZMA Utils

## 选项

```markdown
xz [OPTION]... [FILE]...

-z, --compress      强制压缩
-d, --decompress, --uncompress
                    force decompression
-t, --test          测试压缩文件的完整性
-l, --list          列出有关.xz文件的信息
-k, --keep          保留（不要删除）输入文件
-f, --force         强制覆盖输出文件和（解）压缩链接
-c, --stdout, --to-stdout
                    写入标准输出，不要删除输入文件
-0 ... -9           压缩预设; 默认为6; 取压缩机*和*
                    使用7-9之前解压缩内存使用量考虑在内！
-e, --extreme       尝试通过使用更多的CPU时间来提高压缩比;
                    要求不影响解压缩存储器
-T, --threads=NUM   最多使用NUM个线程; 默认值为1;  set to 0
                    设置为0，使用与处理器内核一样多的线程
-q, --quiet         抑制警告; 指定两次以抑制错误
-v, --verbose       冗长; 指定两次更详细
-h, --help          显示这个简洁的帮助并退出
-H, --long-help     显示更多帮助（还列出了高级选项）
-V, --version       显示版本号并退出
```

## 实例

```bash
xz test.txt     # 压缩一个文件 test.txt，压缩成功后生成 test.txt.xz, 原文件会被删除
xz -d -k test.txt.xz # 解压 test.txt.xz 文件，并使用参数 -k 保持原文件不被删除
xz -l index.txt.xz  # 显示压缩文件基本信息，包括压缩率、完整性验证等，可以与-v和-vv一起使用显示更详细信息
xz -k7 xz_pipe_decomp_mini.c # 使用参数-0...-9或参数--fast,--best设定压缩率。默认为-6
xz -H  | more   # 使用参数 -H 显示 xz 命令所有 options. 参数 -H 比使用参数 --help 显示的内容更详细
find /var/log -type f -iname "*.log" -print0 | xargs -P4 -n16 xz -T1 # 借助 xargs 命令并行压缩多文件,运行此命令须有 root 权限
```
