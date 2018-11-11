设置记住密码（默认15分钟）：
git config -–global credential.helper cache
如果想自己设置时间，以秒为单位：
git config credential.helper ‘cache –timeout=3600’

长期存储密码：
git config –-global credential.helper store
