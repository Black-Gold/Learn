# **ssh**

## 说明

**ssh命令** 是openssh套件中的客户端连接工具，可以给予ssh加密协议实现安全的远程登录服务器

## 选项

```markdown
ssh [-1246AaCfGgKkMNnqsTtVvXxYy] [-b bind_address] [-c cipher_spec]
           [-D [bind_address:]port] [-E log_file] [-e escape_char]
           [-F configfile] [-I pkcs11] [-i identity_file]
           [-J [user@]host[:port]] [-L address] [-l login_name] [-m mac_spec]
           [-O ctl_cmd] [-o option] [-p port] [-Q query_option] [-R address]
           [-S ctl_path] [-W host:port] [-w local_tun[:remote_tun]]
           [user@]hostname [command]

-1      强制使用ssh协议版本1
-2      强制使用ssh协议版本2
-4      强制使用IPv4地址
-6      强制使用IPv6地址
-A      开启认证代理连接转发功能
-a      关闭认证代理连接转发功能
-b      使用本机指定地址作为对应连接的源ip地址
-C      请求压缩所有数据
-F      指定ssh指令的配置文件
-f      后台执行ssh指令
-g      允许远程主机连接主机的转发端口
-i      指定身份文件
-l      指定连接远程服务器登录用户名
-N      不执行远程指令
-o      指定配置选项
-p      指定远程服务器上的端口
-q      静默模式
-X      开启X11转发功能
-x      关闭X11转发功能
-y      开启信任X11转发功能
```

## 实例

```bash
ssh $USER@$HOST command     # 在$Host主机上以$User用户运行命令默认命令为Shell
ssh -f -Y $USER@$HOSTNAME xeyes     # 在名为$HOSTNAME的主机上以$USER用户运行GUI命令
scp -p -r $USER@$HOST: file dir/    # 拷贝到$HOST主机$USER'用户的目录下
ssh -g -L 8080:localhost:80 root@$HOST  # 由本地主机的8080端口转发到$HOST主机的80端口
ssh -R 1434:imap:143 root@$HOST     # 由主机的1434端口转发到imap的143端口
```


