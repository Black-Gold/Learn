# **scp**

## 说明

**scp命令** 用于在Linux下进行远程拷贝文件的命令，和它类似的命令有cp，不过cp只是在本机进行拷贝不能跨服务器，而且scp传输是
加密的。可能会稍微影响一下速度。当你服务器硬盘变为只读read only system时，用scp可以帮你把文件移出来。另外，scp还非常不
占资源，不会提高多少系统负荷，在这一点上，rsync就远远不及它了。虽然 rsync比scp会快一点，但当小文件众多的情况下，rsync会
导致硬盘I/O非常高，而scp基本不影响系统正常使用

## 选项

```markdown
scp [-12346BCpqrv] [-c cipher] [-F ssh_config] [-i identity_file]
           [-l limit] [-o ssh_option] [-P port] [-S program]
           [[user@]host1:]file1 ... [[user@]host2:]file2

-1      使用ssh协议版本1
-2      使用ssh协议版本2
-4      使用ipv4
-6      使用ipv6
-B      以批处理模式运行
-C      使用压缩
-F      指定ssh配置文件
-l      指定宽带限制
-o      指定使用的ssh选项
-P      指定远程主机的端口号
-p      保留文件的最后修改时间，最后访问时间和权限模式
-q      不显示复制进度
-r      以递归方式复制
```

## 实例

```bash
scp -r root@10.10.10.10:/opt/soft/mongodb /opt/soft/    # 从远端复制到本地
scp /opt/soft/file root@10.10.10.10:/opt/soft/scptest    # 上传本地文件到远程机器指定目录

```
