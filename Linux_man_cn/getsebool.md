# **getsebool**

## 说明

**getsebool命令** 是用来查询SElinux策略内各项规则的布尔值。SELinux的策略与规则管理相关命令：seinfo命令、sesearch命令、getsebool命令、setsebool命令、semanage命令

## 选项

```markdown
getsebool [-a] [布尔值条款]  -a：列出目前系统上面的所有布尔值条款设置为开启或关闭值
```

## 实例

```bash
getsebool -a    # 查询本系统内所有的布尔值设置

# 查询httpd_enable_homedirs是否为关闭，若没关闭，请关闭它
getsebool httpd_enable_homedirs
setsebool -P httpd_enable_homedirs=0    # 0是关闭  1是开启
```
