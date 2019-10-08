# chpasswd

## 说明

**chpasswd命令** 是批量更新用户口令的工具，是把一个文件内容重新定向添加到`/etc/shadow`中

## 选项

```markdown
-c, --crypt-method 方法        加密方法(NONE DES MD5 SHA256 SHA512 中的一个)
-e, --encrypted		          输入的密码已经加密的密文
-m, --md5		              使用 MD5 算法加密明文密码
-R, --root CHROOT_DIR         chroot 到的目录
-s, --sha-rounds		      SHA* 加密算法中的 SHA 旁边的数字

```

## 实例

```bash
chpasswd < user.txt # 先创建用户密码文件格式为username:password且不能有空行，保存成文本文件user.txt

```


