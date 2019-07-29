# **last**

## 说明

**last命令**  用于显示用户最后一次的登录信息。单独执行last命令，它会读取`/var/log/wtmp`的文件，并把该给文件的内容记录的登入系统的用户名单全部显示出来
**lastb命令** Lastb与last相同，但默认情况下它显示文件/var/log/btmp的日志，其中包含所有错误的登录尝试

## 选项

```markdown
-f file     让last指定记录文件替代默认的/var/log/wtmp
-num        指定last命令显示的行数
-n num      同上
-t YYYYMMDDHHMMSS   显示指定时间的登录状态。 例如：确定在特定时间登录的用户
-R     不显示hostname字段
-a     在最后一列显示主机名。 与下一个flag结合使用很有用
-d     对于非本地登录，Linux不仅存储远程主机的主机名，还存储其IP。 此选项将IP转换回主机名
-F     打印完整的登录和登出次数和日期
-i     和-d选项一样，但它以数字和点表示法显示IP号码
-o     读取旧类型的wtmp文件（由linux-libc5应用程序编写）
-w     在输出中显示完整的用户名和域名
-x    显示系统关闭条目并运行级别更改信息

```

## 实例

```bash
last reboot     # 显示上次用户登录列表
```


