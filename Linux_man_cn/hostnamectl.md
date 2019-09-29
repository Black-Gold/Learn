# **hostnamectl**

查询或更改系统hostname

## 选项

```markdown
hostnamectl [OPTIONS...] COMMAND ...

   --no-ask-password   Do not prompt for password
-H --host=[USER@]HOST  Operate on remote host
-M --machine=CONTAINER Operate on local container
   --transient         Only set transient hostname
   --static            Only set static hostname
   --pretty            Only set pretty hostname

Commands:
  status                 Show current hostname settings
  set-hostname NAME      Set system hostname
  set-icon-name NAME     Set icon name for host
  set-chassis NAME       Set chassis type for host
  set-deployment NAME    Set deployment environment for host
  set-location NAME      Set location for host

```

## 实例

```bash
hostnamectl set-hostname NAME   # 设置hostname为NAME
```
