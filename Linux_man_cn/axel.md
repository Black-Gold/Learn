# axel

## 说明

**axel** 是Linux下一个不错的HTTP/ftp高速下载工具。支持多线程下载、断点续传，且可以从多个地址或者从一个地址的多个连接来下载同一个文件。
适合网速不给力时多线程下载提高下载速度。比如在国内VPS或服务器上下载lnmp一键安装包用Axel就比wget快

## 安装

```bash
# 网址：http://pkgs.repoforge.org/axel/
rpm -iUvh http://pkgs.repoforge.org/axel/axel-2.4-1.el5.rf.i386.rpm # 32位CentOS
rpm -iUvh http://pkgs.repoforge.org/axel/axel-2.4-1.el5.rf.x86_64.rpm   # 64位CentOS
apt-get install axel    # Debian/Ubuntu

```

## 选项

```markdown
--max-speed=x , -s x         最高速度x
--num-connections=x , -n x   连接数x
--output=f , -o f            下载为本地文件f
--search[=x] , -S [x]        搜索镜像
--header=x , -H x            添加头文件字符串x（指定 HTTP header）
--user-agent=x , -U x        设置用户代理（指定 HTTP user agent）
--no-proxy ， -N             不使用代理服务器
--quiet ， -q                静默模式
--verbose ，-v               更多状态信息
--alternate ， -a            Alternate progress indicator

```

## 实例

```bash
axel -n 10 -o /tmp/ http://www.jsdig.com/lnmp.tar.gz    # 默认支持断点续传，下载lnmp安装包指定10个线程并存到/tmp/

```



