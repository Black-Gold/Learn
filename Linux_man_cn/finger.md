# finger

## 说明

**finger命令** 用于查找并显示用户信息。包括本地与远端主机的用户皆可，帐号名称没有大小写的差别。单独执行finger指令，它会显示本地主机
现在所有的用户的登陆信息，包括帐号名称，真实姓名，登入终端机，闲置时间，登入时间以及地址和电话

## 选项

```markdown
-l：列出该用户的帐号名称，真实姓名，用户专属目录，登入所用的Shell，登入时间，转信地址，电子邮件状态，还有计划文件和方案文件内容
-m：排除查找用户的真实姓名
-s：列出该用户的帐号名称，真实姓名，登入终端机，闲置时间，登入时间以及地址和电话
-p：列出该用户的帐号名称，真实姓名，用户专属目录，登入所用的Shell，登入时间，转信地址，电子邮件状态，但不显示该用户的计划文件和方案文件内容

不指定finger的选项如果提供操作者的话，缺省设为`-l`输出风格，否则为`-s`风格，注意在两种格式中，如果信息不足，都有一些域可能丢失，如果没有
指定参数finger会为当前登录的每个用户打印一个条目
```

## 实例



