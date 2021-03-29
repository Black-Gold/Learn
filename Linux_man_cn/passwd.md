# **passwd**

## 说明

**passwd命令** 用于设置用户的认证信息，包括用户密码、密码过期时间等。系统管理者则能用它管理系统用户的密码。只有管理者可
以指定用户名称，一般用户只能变更自己的密码

```markdown
用法: passwd [选项...] <帐号名称>
  -k, --keep-tokens       保持身份验证令牌不过期
  -d, --delete            删除已命名帐号的密码(只有根用户才能进行此操作)
  -l, --lock              锁定指名帐户的密码(仅限 root 用户)
  -u, --unlock            解锁指名账户的密码(仅限 root 用户)
  -e, --expire            终止指名帐户的密码(仅限 root 用户)
  -f, --force             强制执行操作
  -x, --maximum=DAYS      密码的最长有效时限(只有根用户才能进行此操作)
  -n, --minimum=DAYS      密码的最短有效时限(只有根用户才能进行此操作)
  -w, --warning=DAYS      在密码过期前多少天开始提醒用户(只有根用户才能进行此操作)
  -i, --inactive=DAYS     当密码过期后经过多少天该帐号会被禁用(只有根用户才能进行此操作)
  -S, --status            报告已命名帐号的密码状态(只有根用户才能进行此操作)
  --stdin                 从标准输入读取令牌(只有根用户才能进行此操作)
```

### 知识扩展

```bash
# 存放用户信息
/etc/passwd
/etc/shadow

# 存放组信息
/etc/group
/etc/gshadow

: << comment
# 用户信息文件分析（每项用`:`隔开)

例如：jack:X:503:504:::/home/jack/:/bin/bash
jack　　//用户名
X　　//口令、密码
503　　//用户id（0代表root、普通新建用户从500开始）
504　　//所在组
:　　//描述
/home/jack/　　//用户主目录
/bin/bash　　//用户缺省Shell
comment

: << comment
# 组信息文件分析

例如：jack:$!$:???:13801:0:99999:7:*:*:
jack　　//组名
$!$　　//被加密的口令
13801　　//创建日期与今天相隔的天数
0　　//口令最短位数
99999　　//用户口令
7　　//到7天时提醒
*　　//禁用天数
*　　//过期天数
comment

```

## 实例

```bash
# 如果是普通用户执行passwd只能修改自己的密码。如果新建用户后，要为新用户创建密码,则用passwd 用户名，注意要以root用户的权限来创建

passwd -l linuxde   # 锁定用户linuxde不能更改密码
passwd -d linuxde   # 清除linuxde用户密码,注意：当我们清除一个用户的密码时，登录时就无需密码，这一点要加以注意
echo "666666" | passwd --stdin ww &> /dev/null  # 设置用户ww密码为666666
```
