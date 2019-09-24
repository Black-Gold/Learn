# **chage**

## 说明

**chage命令** 是用来修改帐号和密码的有效期限

## 选项

```markdown
-d, --lastday 最近日期        将最近一次密码设置时间设为“最近日期”
-E, --expiredate 过期日期     将帐户过期时间设为“过期日期”
-I, --inactive INACITVE       过期 INACTIVE 天数后，设定密码为失效状态
-l, --list                    显示帐户年龄信息
-m, --mindays 最小天数        将两次改变密码之间相距的最小天数设为“最小天数”
-M, --maxdays 最大天数        将两次改变密码之间相距的最大天数设为“最大天数”
-R, --root CHROOT_DIR         chroot 到的目录
-W, --warndays 警告天数       将过期警告天数设为“警告天数”

```

### 实例  

```bash
: << comment
可以编辑`/etc/login.defs`来设定几个参数，设置口令默认按照参数设定为准：
PASS_MAX_DAYS   99999
PASS_MIN_DAYS   0
PASS_MIN_LEN    5
PASS_WARN_AGE   7
comment

chage -l root       # 查看root帐户密码策略信息
chage -M 60 root    # 修改root密码过期时间
chage -I 5 root     # 设置密码失效时间：


```


