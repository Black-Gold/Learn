# **at**

## 说明

**at命令** 用于在指定时间执行命令。at允许使用一套相当复杂的指定时间的方法。它能够接受在当天的hh:mm（小时:分钟）式的时间
指定。假如该时间已过去，那么就放在第二天执行。当然也能够使用midnight（深夜），noon（中午），teatime（饮茶时间，一般是下
午4点）等比较模糊的 词语来指定时间。用户还能够采用12小时计时制，即在时间后面加上AM（上午）或PM（下午）来说明是上午还是
下午。 也能够指定命令执行的具体日期，指定格式为month day（月 日）或mm/dd/yy（月/日/年）或dd.mm.yy（日.月.年）。指定的
日期必须跟在指定时间的后面

上面介绍的都是绝对计时法，其实还能够使用相对计时法，这对于安排不久就要执行的命令是很有好处的。指定格式为：
`now + count time-units`，now就是当前时间，time-units是时间单位，这里能够是minutes（分钟）、hours（小时）、days（天）
、weeks（星期）。count是时间的数量，究竟是几天，还是几小时，等等。 更有一种计时方法就是直接使用today（今天）、tomorrow
（明天）来指定完成命令的时间

## 选项

```markdown
-f：指定包含具体指令的任务文件
-q：指定新任务的队列名称
-l：显示待执行任务的列表
-d：删除指定的待执行任务
-m：任务执行完成后向用户发送E-mail
```

## 实例

```bash
echo "mail -s 'get the train' P@draigBrady.com < /dev/null" | at 17:45  # 在指定的时间发送邮件
/bin/ls | at 5pm+3 days   # 三天后的下午5点锺执行/bin/ls
date >/root/2013.log | at 17:20 tomorrow   # 明天17点钟，输出时间到指定文件内
atq # 计划任务设定后，在没有执行之前我们可以用atq命令来查看系统没有执行工作任务
at -c 8     # 显示已经设置的任务内容
echo "DISPLAY=$DISPLAY xmessage cooker" | at "NOW + 30 minutes" # 在给定的时间弹出对话框

# 指定时间的方式分为绝对计时方法和相对计时方法
# 默认情况下书写的计划任务都存放在/var/spool/目录中
: << comment
hh:mm:today
hh:mm:tomorrow
hh:mm:星期
hh:mm:MM/DD/YY;MMDDYY;DD.MM.YY

now +n minutes
now +n hours
now +n days

实例：指定今天下午17:30执行某命令；此时为下午14:30,2013.5.8
多个书写方式：（仅供参考学习）
at 5:30pm
at 17:30
at 17:30 today
at now +3 hours
at now +180 minutes
at 17:30 05.08.13
at 17:30 05/08/13
使用ctrl+d提交任务
comment

```
