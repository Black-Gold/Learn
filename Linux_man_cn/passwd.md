# **passwd**

## 说明

**passwd命令** 用于设置用户的认证信息，包括用户密码、密码过期时间等。系统管理者则能用它管理系统用户的密码。只有管理者可以指定用户名称，一般用户只能变更自己的密码。

```info
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

## 知识扩展

与用户、组账户信息相关的文件

存放用户信息：

```
/etc/passwd
/etc/shadow
```

存放组信息：

```
/etc/group
/etc/gshadow
```

用户信息文件分析（每项用`:`隔开）

```
例如：jack:X:503:504:::/home/jack/:/bin/bash
jack　　//用户名
X　　//口令、密码
503　　//用户id（0代表root、普通新建用户从500开始）
504　　//所在组
:　　//描述
/home/jack/　　//用户主目录
/bin/bash　　//用户缺省Shell
```

组信息文件分析

```
例如：jack:$!$:???:13801:0:99999:7:*:*:
jack　　//组名
$!$　　//被加密的口令
13801　　//创建日期与今天相隔的天数
0　　//口令最短位数
99999　　//用户口令
7　　//到7天时提醒
*　　//禁用天数
*　　//过期天数
```

### 实例  

如果是普通用户执行passwd只能修改自己的密码。如果新建用户后，要为新用户创建密码，则用passwd用户名，注意要以root用户的权限来创建。

```
[root@localhost ~]# passwd linuxde    //更改或创建linuxde用户的密码；
Changing password for user linuxde.
New UNIX password:          //请输入新密码；
Retype new UNIX password:   //再输入一次；
passwd: all authentication tokens updated successfully. //成功；
```

普通用户如果想更改自己的密码，直接运行passwd即可，比如当前操作的用户是linuxde。

```
[linuxde@localhost ~]$ passwd
Changing password for user linuxde. //更改linuxde用户的密码；
(current) UNIX password:   //请输入当前密码；
New UNIX password:         //请输入新密码；
Retype new UNIX password:  //确认新密码；
passwd: all authentication tokens updated successfully. //更改成功；
```

比如我们让某个用户不能修改密码，可以用`-l`选项来锁定：

```
[root@localhost ~]# passwd -l linuxde    //锁定用户linuxde不能更改密码；
Locking password for user linuxde.
passwd: Success           //锁定成功；

[linuxde@localhost ~]# su linuxde   //通过su切换到linuxde用户；
[linuxde@localhost ~]$ passwd      //linuxde来更改密码；
Changing password for user linuxde.
Changing password for linuxde
(current) UNIX password:          //输入linuxde的当前密码；
passwd: Authentication token manipulation error     //失败，不能更改密码；
```

再来一例：

```
[root@localhost ~]# passwd -d linuxde  //清除linuxde用户密码；
Removing password for user linuxde.
passwd: Success                         //清除成功；

[root@localhost ~]# passwd -S linuxde    //查询linuxde用户密码状态；
Empty password.                         //空密码，也就是没有密码；
```

注意：当我们清除一个用户的密码时，登录时就无需密码，这一点要加以注意。



