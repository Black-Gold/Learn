# **dpkg**

## 说明

```markdown
-i：安装软件包
-r：删除软件包
-P：删除软件包的同时删除其配置文件
-L：显示于软件包关联的文件
-l：显示已安装软件包列表
--unpack：解开软件包
-c：显示软件包内文件列表
--confiugre：配置软件包
```

## 实例

```bash
dpkg-query -W -f='${Installed-Size;10}\t${Package}\n' | sort -k1,1n     # 显示所有在deb发布版上安装的包，并以KB包大小为序
dpkg -i package.deb                     #安装包
dpkg -r package                         #删除包
dpkg -P package                         #删除包（包括配置文件）
dpkg -L package                         #列出与该包关联的文件
dpkg -l package                         #显示该包的版本
dpkg --unpack package.deb               #解开deb包的内容
dpkg -S keyword                         #搜索所属的包内容
dpkg -l                                 #列出当前已安装的包
dpkg -c package.deb                     #列出deb包的内容
dpkg --configure package                #配置包
echo -e "$(( $(dpkg -l | wc -l) -5 ))"  # 所有已安装的包总数

# 清理debian旧内核
dpkg -l 'linux-*' | sed '/^ii/!d;/'"$(uname -r | sed "s/-/\1/")"'/d;s/^[^ ]* [^ ]* .*/\1/;/[0-9]/!d' | xargs sudo apt-get -y purge
```
