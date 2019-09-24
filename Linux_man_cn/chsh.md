# chsh

## 说明

**chsh命令** 用来更换登录系统时使用的shell。若不指定任何参数与用户名称，则chsh会以应答的方式进行设置

## 选项

```markdown
-s, --shell <shell>  更改指定登录 shell
-l, --list-shells    打印 shell 列表并退出

```

## 实例

```bash
chsh -s /bin/zsh    # 把我的shell改成zsh；chsh -s其实修改的是/etc/passwd文件里和你的用户名相对应的那一行

# 查看系统安装了哪些shell的两种方法
chsh -l # 第一种
cat /etc/shells # 第二种


```
