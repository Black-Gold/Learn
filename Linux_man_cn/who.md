# **who**

## 说明

**who命令** 是显示目前登录系统的用户信息。执行who命令可得知目前有那些用户登入系统，单独执行who命令会列出登入帐号，使用的终端机，登入
时间以及从何处登入或正在使用哪个X显示器

## 选项

```markdown
-a, --all		等于-b -d --login -p -r -t -T -u 选项的组合
-b, --boot		上次系统启动时间
-d, --dead		显示已死的进程
-H, --heading	输出头部的标题列
-l，--login		显示系统登录进程
    --lookup	尝试通过 DNS 查验主机名
-m			    只面对和标准输入有直接交互的主机和用户
-p, --process	显示由 init 进程衍生的活动进程
-q, --count		列出所有已登录用户的登录名与用户数量
-r, --runlevel	显示当前的运行级别
-s, --short		只显示名称、线路和时间(默认)
-T, -w, --mesg	用+，- 或 ? 标注用户消息状态
-u, --users		列出已登录的用户
    --message	等于-T
    --writable	等于-T

If FILE is not specified, use /var/run/utmp.  /var/log/wtmp as FILE is common.
If ARG1 ARG2 given, -m presumed: 'am i' or 'mom likes' are usual

```


## 实例

```bash
who -q
who -H
who -w

```


