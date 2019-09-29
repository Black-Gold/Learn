# **ssh-keyscan**

## 说明

**ssh-keyscan命令** 是一个收集大量主机公钥的使用工具

## 选项

```markdown
用法：ssh-keyscan [-46cHv] [-f file] [-p port] [-T timeout] [-t type]
		   [host | addrlist namelist] ...

-4：强制使用IPv4地址
-6：强制使用IPv6地址
-f：从指定文件中读取“地址列表/名字列表”
-p：指定连接远程主机的端口
-T：指定连接尝试的超时时间
-t：指定要创建的密钥类型
-v：信息模式，打印调试信息
```



