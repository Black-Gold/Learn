# **md5sum**

## 说明

**md5sum命令** 采用MD5报文摘要算法（128位）显示和检查文件的校验和。直接在命令行终端直接运行

MD5算法常常被用来验证网络文件传输的完整性，防止文件被人篡改。MD5 全称是报文摘要算法（Message-Digest Algorithm 5），此算法对任意长度的
信息逐位进行计算，产生一个二进制长度为128位（十六进制长度就是32位）的“指纹”（或称“报文摘要”），不同的文件产生相同的报文摘要极小可能性存在

```markdown
若没有文件选项，或者文件处为"-"，则从标准输入读取

-b, --binary   以二进制模式读取
-c, --check    从文件中读取MD5 的校验值并予以检查
    --tag      create a BSD-style checksum
-t, --text     以纯文本模式读取(默认)[注意：GNU系统上的二进制和文本模式选项没有区别]

以下四个选项对于验证校验和非常有用
--quiet          don't print OK for each successfully verified file
--status         don't output anything, status code shows success
--strict         exit non-zero for improperly formatted checksum lines
-w, --warn       warn about improperly formatted checksum lines

```

## 实例

```bash
md5sum insert.sql   # 生成一个文件insert.sql的md5值
md5sum file -c file.md  # 检查file是否被修改，file.md包含file文件的原始md5值

```
