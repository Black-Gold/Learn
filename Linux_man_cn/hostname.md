# **hostname**

## 说明

**hostname命令** 用于显示和设置系统的主机名称。环境变量HOSTNAME也保存了当前的主机名。在使用hostname命令设置主机名后，系
统并不会永久保存新的主机名，重新启动机器之后还是原来的主机名。如果需要永久修改主机名，需要同时修改`/etc/hosts`和
`/etc/sysconfig/network`的相关内容

```markdown
Usage: hostname [-b] {hostname|-F file}         set host name (from file)
       hostname [-a|-A|-d|-f|-i|-I|-s|-y]       display formatted name
       hostname                                 display host name

       {yp,nis,}domainname {nisdomain|-F file}  set NIS domain name (from file)
       {yp,nis,}domainname                      display NIS domain name

       dnsdomainname                            display dns domain name

Program name:
       {yp,nis,}domainname=hostname -y
       dnsdomainname=hostname -d

-a, --alias            显示主机别名
-A, --all-fqdns        all long host names (FQDNs)
-b, --boot             set default hostname if none available
-d, --domain           显示DNS域名
-f, --fqdn, --long     显示FQDN名称
-F, --file             read host name or NIS domain name from given file
-i, --ip-address       显示主机的ip地址
-I, --all-ip-addresses all addresses for the host
-s, --short            显示短主机名称，在第一个点处截断
-y, --yp, --nis        显示NIS/YP域名
```

## 实例

```bash
hostname -i     # 查寻本地主机的IP地址同等于host `hostname`
```
