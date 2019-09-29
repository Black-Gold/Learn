# **systemctl**

## 说明

**systemctl命令** 是系统服务管理器指令，它实际上将 service 和 chkconfig 这两个命令组合到一起

## 选项

```markdown
   --system         Connect to system manager
-H --host=[USER@]HOST
                    Operate on remote host
-M --machine=CONTAINER
                    Operate on local container
-t --type=TYPE      List units of a particular type
   --state=STATE    List units with particular LOAD or SUB or ACTIVE state
-p --property=NAME  Show only properties by this name
-a --all            Show all loaded units/properties, including dead/empty
                    ones. To list all units installed on the system, use
                    the 'list-unit-files' command instead.
-l --full           Don't ellipsize unit names on output
-r --recursive      Show unit list of host and local containers
   --reverse        Show reverse dependencies with 'list-dependencies'
   --job-mode=MODE  Specify how to deal with already queued jobs, when
                    queueing a new job
   --show-types     When showing sockets, explicitly show their type
-i --ignore-inhibitors
                    When shutting down or sleeping, ignore inhibitors
   --kill-who=WHO   Who to send signal to
-s --signal=SIGNAL  Which signal to send
   --now            Start or stop unit in addition to enabling or disabling it
-q --quiet          Suppress output
   --no-block       Do not wait until operation finished
   --no-wall        Don't send wall message before halt/power-off/reboot
   --no-reload      Don't reload daemon after en-/dis-abling unit files
   --no-legend      Do not print a legend (column headers and hints)
   --no-pager       Do not pipe output into a pager
   --no-ask-password
                    Do not ask for system passwords
   --global         Enable/disable unit files globally
   --runtime        Enable unit files only temporarily until next reboot
-f --force          When enabling unit files, override existing symlinks
                    When shutting down, execute action immediately
   --preset-mode=   Apply only enable, only disable, or all presets
   --root=PATH      Enable unit files in the specified root directory
-n --lines=INTEGER  Number of journal entries to show
-o --output=STRING  Change journal output mode (short, short-iso,
                            short-precise, short-monotonic, verbose,
                            export, json, json-pretty, json-sse, cat)
   --plain          Print unit dependencies as a list instead of a tree

Unit Commands:
  list-units [PATTERN...]         List loaded units
  list-sockets [PATTERN...]       List loaded sockets ordered by address
  list-timers [PATTERN...]        List loaded timers ordered by next elapse
  start NAME...                   Start (activate) one or more units
  stop NAME...                    Stop (deactivate) one or more units
  reload NAME...                  Reload one or more units
  restart NAME...                 Start or restart one or more units
  try-restart NAME...             Restart one or more units if active
  reload-or-restart NAME...       Reload one or more units if possible,
                                  otherwise start or restart
  reload-or-try-restart NAME...   Reload one or more units if possible,
                                  otherwise restart if active
  isolate NAME                    Start one unit and stop all others
  kill NAME...                    Send signal to processes of a unit
  is-active PATTERN...            Check whether units are active
  is-failed PATTERN...            Check whether units are failed
  status [PATTERN...|PID...]      Show runtime status of one or more units
  show [PATTERN...|JOB...]        Show properties of one or more
                                  units/jobs or the manager
  cat PATTERN...                  Show files and drop-ins of one or more units
  set-property NAME ASSIGNMENT... Sets one or more properties of a unit
  help PATTERN...|PID...          Show manual for one or more units
  reset-failed [PATTERN...]       Reset failed state for all, one, or more
                                  units
  list-dependencies [NAME]        Recursively show units which are required
                                  or wanted by this unit or by which this
                                  unit is required or wanted

Unit File Commands:
  list-unit-files [PATTERN...]    List installed unit files
  enable NAME...                  Enable one or more unit files
  disable NAME...                 Disable one or more unit files
  reenable NAME...                Reenable one or more unit files
  preset NAME...                  Enable/disable one or more unit files
                                  based on preset configuration
  preset-all                      Enable/disable all unit files based on
                                  preset configuration
  is-enabled NAME...              Check whether unit files are enabled
  mask NAME...                    Mask one or more units
  unmask NAME...                  Unmask one or more units
  link PATH...                    Link one or more units files into
                                  the search path
  add-wants TARGET NAME...        Add 'Wants' dependency for the target
                                  on specified one or more units
  add-requires TARGET NAME...     Add 'Requires' dependency for the target
                                  on specified one or more units
  edit NAME...                    Edit one or more unit files
  get-default                     Get the name of the default target
  set-default NAME                Set the default target

Machine Commands:
  list-machines [PATTERN...]      List local containers and host

Job Commands:
  list-jobs [PATTERN...]          List jobs
  cancel [JOB...]                 Cancel all, one, or more jobs

Snapshot Commands:
  snapshot [NAME]                 Create a snapshot
  delete NAME...                  Remove one or more snapshots

Environment Commands:
  show-environment                Dump environment
  set-environment NAME=VALUE...   Set one or more environment variables
  unset-environment NAME...       Unset one or more environment variables
  import-environment [NAME...]    Import all or some environment variables

Manager Lifecycle Commands:
  daemon-reload                   Reload systemd manager configuration
  daemon-reexec                   Reexecute systemd manager

System Commands:
  is-system-running               Check whether system is fully running
  default                         Enter system default mode
  rescue                          Enter system rescue mode
  emergency                       Enter system emergency mode
  halt                            Shut down and halt the system
  poweroff                        Shut down and power-off the system
  reboot [ARG]                    Shut down and reboot the system
  kexec                           Shut down and reboot the system with kexec
  exit                            Request user instance exit
  switch-root ROOT [INIT]         Change to a different root file system
  suspend                         Suspend the system
  hibernate                       Hibernate the system
  hybrid-sleep                    Hibernate and suspend the system
```

## 实例

```bash
systemctl reboot        # 重启系统
systemctl poweroff      # 关闭系统，切断电源
systemctl halt          # 关机
systemctl suspend       # 暂停系统
systemctl hibernate     # 休眠系统
systemctl hybrid-sleep  # 让系统进入交互式休眠状态
systemctl rescue        # 启动进入救援状态（单用户状态）
systemctl list-units --type=service    # 查看所有服务单元

systemd-analyze blame # 显示瀑布状的启动过程流
systemd-analyze critical-chain atd.service  # 显示指定服务的启动流

localectl set-locale LANG=en_GB.utf8 localectl set-keymap en_GB # 设置本地化参数

timedatectl list-timezones # 显示所有可用的时区

# 设置当前时区
timedatectl set-timezone America/New_York
timedatectl set-time YYYY-MM-DD
timedatectl set-time HH:MM:SS

loginctl list-sessions # 列出当前session
loginctl list-users # 列出当前登录用户
loginctl show-user ruanyf # 列出显示指定用户的信息

systemctl is-active application.service # 显示某个 Unit 是否正在运行
systemctl is-failed application.service # 显示某个 Unit 是否处于启动失败状态
systemctl is-enabled application.service # 显示某个 Unit 服务是否建立了启动链接

systemctl daemon-reload # 重载所有修改过的配置文件
systemctl show httpd.service # 显示某个 Unit 的所有底层参数
systemctl set-property httpd.service CPUShares=500 # 设置某个 Unit 的指定属性
systemctl list-dependencies nginx.service # 列出一个unit的所有依赖
systemctl list-unit-files # 列出所有systemctl配置文件
systemctl list-unit-files --type=service # 列出指定类型的配置文件
systemctl list-unit-files --type=target # 查看当前系统的所有 Target
systemctl list-dependencies multi-user.target # 查看一个 Target 包含的所有 Unit
systemctl get-default # 查看启动时的默认 Target
systemctl set-default multi-user.target # 设置启动时的默认 Target

journalctl -k # 查看内核日志（不显示应用日志）
journalctl -b -0 # 查看系统本次启动的日志
journalctl -b -1 # 查看上一次启动的日志（需更改设置）

# 查看指定时间的日志
journalctl --since="2012-10-30 18:17:16"
journalctl --since "20 min ago"
journalctl --since yesterday
journalctl --since "2015-01-10" --until "2015-01-11 03:00" journalctl --since 09:00 --until "1 hour ago"
journalctl -n 20 # 显示尾部指定行数的日志
journalctl -f # 实时滚动显示最新日志
journalctl _PID=1 # 查看指定进程的日志
journalctl _UID=33 --since today # 查看指定用户的日志
journalctl -u nginx.service --since today # 查看某个 Unit 的日志
journalctl -u nginx.service -f # 实时滚动显示某个 Unit 的最新日志
journalctl -u nginx.service -u php-fpm.service --since today # 合并显示多个 Unit 的日志

journalctl -p err -b
# 查看指定优先级（及其以上级别）的日志，共有8级
0: emerg
1: alert
2: crit
3: err
4: warning
5: notice
6: info
7: debug

journalctl --no-pager # 日志默认分页输出，--no-pager 改为正常的标准输出
journalctl -b -u nginx.service -o json # 以 JSON 格式（单行）输出
journalctl -b -u nginx.serviceqq -o json-pretty # 以 JSON 格式（多行）输出，可读性更好
journalctl --disk-usage # 显示日志占据的硬盘空间
journalctl --vacuum-size=1G # 指定日志文件占据的最大空间
journalctl --vacuum-time=1years # 指定日志文件保存多久
```

