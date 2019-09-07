# whois

## 说明

**whois**  whois目录服务的客户端

## 选项

```markdown
用法： whois 【选项】 …… 对象 …… 

-h HOST, --host HOST    连接到服务器 HOST
-p PORT, --port PORT    连接到端口 PORT
-H                      隐藏法律声明 
      --verbose         解释正在做什么 
      --help            显示帮助并退出 
      --version         输出版本信息并退出 

这些标志是由 whois.ript.net 和 RIPE-like 服务器支持的： 
 -l                     寻找有更少具体匹配的一个级别 
-L                     寻找所有更少具体匹配的级别 
-m                   寻找有更加具体匹配的一个级别 
-M                   寻找有更加具体的匹配的所有级别 
-c                     寻找包含 mnt-irt 属性的最小匹配 
-x                     精确匹配 
-b                     return brief IP address ranges with abuse contact
-B                     关闭对象过滤（显示 email 地址） 
-G                    关闭相关联对象的分组 
-d                     返回 DNS 反解授权对象 
-i ATTR[,ATTR]...      对特定的属性（ ATTR ）进行逆向查询 
-T TYPE[,TYPE]...      只寻找 TYPE 的对象 
-K                      只返回主键 
-r                      关闭联系信息的递归查询 
-R                     强制显示域对象的本地副本，即使 
                         它包含引用 
-a                     一并搜索所有的数据库镜像 
-s SOURCE[,SOURCE]...   从 SOURCE 中搜索数据库镜像 
-g SOURCE:FIRST-LAST   从串行的 FIRST 到 LAST 的 SOURCE 中查找更新 
-t TYPE                 请求 TYPE 对象的模板 
-v TYPE                 请求 TYPE 对象的详细模板 
-q [version|sources|types]   询问制定服务器信息 

```

## 实例

```bash
whois linuxde.net # 查询域名信息

```
