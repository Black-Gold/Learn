# **apt-get**

## 说明

**apt-get命令** 是Debian Linux发行版中的APT软件包管理工具。所有基于Debian的发行都使用这个包管理系统。deb包可以把一个
应用的文件包在一起，大体就如同Windows上的安装文件

## 选项

```markdown

```

## 实例

```markdown
使用apt-get命令的第一步就是引入必需的软件库，Debian的软件库也就是所有Debian软件包的集合，它们存在互联网上的一些公共
站点上。把它们的地址加入，apt-get就能搜索到我们想要的软件。/etc/apt/sources.list是存放这些地址列表的配置文件，其格式如下：
deb web或[ftp地址] [发行版名字] main/contrib/non-[free]

修改`/etc/apt/sources.list`或者`/etc/apt/preferences`之后运行该命令。需要定期运行这一命令以确保您的软件包列表是最新的：
apt-get update
```


```bash
apt-get dist-upgrade    # 将系统升级到新版本

# 卸载软件包，清除残余的配置文件
apt-get remove --purge -y
apt-get autoremove --purge -y
sudo apt-get clean
apt-get autoclean
dpkg -l |grep ^rc|awk '{print $2}' |sudo xargs dpkg -P
apt-get autoremove  # 要删除作为依赖项安装但不再具有父应用程序的软件包
dpkg --purge --force-remove-essential kernel-image-NNN  # 删除旧内核
dpkg --get-selections | grep PACKAGE_NAME | awk '{ print $1}'| xargs apt-get -y --purge autoremove  # 删除专用软件包

```
