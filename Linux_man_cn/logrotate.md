# **logrotate**

## 说明

**logrotate命令** 用于对系统日志进行轮转、压缩和删除，也可以将日志发送到指定邮箱。使用logrotate指令，可让你轻松管理系统所产生的
记录文件。每个记录文件都可被设置成每日，每周或每月处理，也能在文件太大时立即处理。您必须自行编辑，指定配置文件，预设的配置文件存放在
`/etc/logrotate.conf`文件中

## 选项

```markdown
-d, --debug               Don't do anything, just test (implies -v)
-f, --force               强制文件rotate
-m, --mail=command        Command to send mail (instead of `/bin/mail')
-s, --state=statefile     Path of state file
-v, --verbose             Display messages during rotation
-l, --log=STRING          Log file

```



