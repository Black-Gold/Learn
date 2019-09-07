# smbclient

## 说明

**smbclient命令** 属于samba套件，它提供一种命令行使用交互式方式访问samba服务器的共享资源

## 选项

```markdown
-B<ip地址>：传送广播数据包时所用的IP地址；
-d<排错层级>：指定记录文件所记载事件的详细程度；
-E：将信息送到标准错误输出设备；
-h：显示帮助；
-i<范围>：设置NetBIOS名称范围；
-I<IP地址>：指定服务器的IP地址；
-l<记录文件>：指定记录文件的名称；
-L：显示服务器端所分享出来的所有资源；
-M<NetBIOS名称>：可利用WinPopup协议，将信息送给选项中所指定的主机；
-n<NetBIOS名称>：指定用户端所要使用的NetBIOS名称；
-N：不用询问密码；
-O<连接槽选项>：设置用户端TCP连接槽的选项；
-p<TCP连接端口>：指定服务器端TCP连接端口编号；
-R<名称解析顺序>：设置NetBIOS名称解析的顺序；
-s<目录>：指定smb.conf所在的目录；
-t<服务器字码>：设置用何种字符码来解析服务器端的文件名称；
-T<tar选项>：备份服务器端分享的全部文件，并打包成tar格式的文件；
-U<用户名称>：指定用户名称；
-w<工作群组>：指定工作群组名称。
```

## 实例

```bash
smbclient -L 198.168.0.1 -U username%password   # 列出某个IP地址所提供的共享文件夹
smbclient //192.168.0.1/tmp  -U username%password   # 像ftp客户端一样使用smbclient,执行成功后，进入smbclient环境

smbclient -c "ls"  //192.168.0.1/tmp  -U username%password
: << comment
直接一次性使用smbclient命令
这里有许多命令和ftp命令相似，如cd 、lcd、get、megt、put、mput等。通过这些命令可以访问远程主机的共享资源
comment

# 创建一个共享文件夹.如果用户共享`//192.168.0.1/tmp`的方式是只读的，会提示"NT_STATUS_ACCESS_DENIED xxx"
smbclient -c "mkdir share1" //192.168.0.1/tmp -U username%password

```