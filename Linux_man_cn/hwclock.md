# **hwclock**

## 说明

**hwclock命令**用于调整RTC(real_time clock)时间，Linux还有个系统时间(wall time)

RTC是电脑内建的硬件时间，执行这项指令可以显示现在时刻，调整硬件时钟的时间，将系统时间设成与硬件时钟之时间一致，或是把系
统时间回存到硬件时钟

在Linux中有硬件时钟与系统时钟等两种时钟。硬件时钟是指主机板上的时钟设备，也就是通常可在BIOS画面设定的时钟。系统时钟则是
指kernel中的时钟。当Linux启动时，系统时钟会去读取硬件时钟的设定，之后系统时钟即独立运作。所有Linux相关指令与函数都是读取
系统时钟的设定

```markdown
clock命令和hwclock相同

hwclock [功能] [选项...]

功能：
-h, --help           显示此帮助并退出
-r, --show           读取硬件时钟并打印结果
    --set            将 RTC 设置为--date指定的时间,设定硬件时钟；hwclock --set --date='28/3/2018 12:34:00'
-s, --hctosys        从硬件时钟设置系统时间,即将系统时钟调整为与目前的硬件时钟一致
-w, --systohc        从当前系统时间设置硬件时钟,即将硬件时钟调整为与目前的系统时钟一致
    --systz          基于当前时区设置系统时间
    --adjust         根据自上次时钟设置或调整后的系统漂移来调整RTC,hwclock每次更改硬件时钟都会记录在/etc/adjtime中
-c, --compare        定期将系统时钟与 CMOS 时钟相比较
    --getepoch       打印内核的硬件时钟纪元(epoch)值
    --setepoch       将内核的硬件时钟纪元(epoch)值设置为
                       --epoch 选项指定的值
    --predict        预测 --date 选项所指定时刻读取到的 RTC 值

选项：
-u, --utc            硬件时钟保持为 UTC 时间
    --localtime      硬件时钟保持为本地时间
-f, --rtc <文件>     代替默认文件的特殊 /dev/... 文件
    --directisa      直接访问 ISA 总线，而非 /dev/rtc,若无法存取时，可用此参数直接以I/O指令来存取硬件时钟
    --badyear        忽略  RTC 年份(由于 BIOS 损坏)
    --date <时间>    指定要设置的硬件时钟时间
    --epoch <年>     指定作为硬件纪元(epoch)值起始的年份
    --noadjfile      不访问 /etc/adjtime；需要使用 --utc 或 --localtime 选项
    --adjfile <文件> 指定调整文件的路径
                       默认为 /etc/adjtime
    --test           不更新，只显示将进行什么操作
-D, --debug          调试模式

```

## 实例

```bash
# 设置硬件时间要依赖于操作系统时间，具体方法如下：
hwclock -systohc
hwclock --systohc --utc

hwclock # 不加任何参数使用hwclock，可以查看当前的硬件日期和时间

# 查看clock文件，确认是否设置了UTC：UTC=yes表示已设置
cat /etc/default/rcS
cat /etc/sysconfig/clock    # 在其他一些版本的Linux（如RebHat）中可以这样查看

```
