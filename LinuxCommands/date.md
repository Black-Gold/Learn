# date

## 说明

**date命令** 是显示或设置系统时间与日期。

很多shell脚本里面需要打印不同格式的时间或日期，以及要根据时间和日期执行操作。延时通常用于脚本执行过程中提供一段等待的时间。日期可以以多种格式去打印，也可以使用命令设置固定的格式。在类UNIX系统中，日期被存储为一个整数，其大小为自世界标准时间（UTC）1970年1月1日0时0分0秒起流逝的秒数。

## 语法  

用法：date [选项]... [+格式]

或：date [-u|--utc|--universal] [MMDDhhmm[[CC]YY][.ss]]

## 选项  

```sh
必选参数对长短选项同时适用

-d,--date=STRING 用STRING描述时间，而不是'NOW'
   --debug 注释解析日期,并警告stderr的可疑用法

-f,--file=DATEFILE 和--date相似,输出DATEFILE的每一行

-I[FMT],--iso-8601[=FMT] 以ISO 8601格式输出，FMT='date'默认只适用于日期，'hour'，'minutes'，'seconds'或'ns'，对于指定精度的日期和时间。 示例：2006-08-14T02：34：56-06：00

-R,--rfc-email 以RFC 5322格式输出，例如：Mon, 14 Aug 2006 02:34:56 -0600
   --rfc-3339=FMT 以RFC 3339格式输出，FMT='date'，'hour'，'minutes'，'seconds'或'ns'，对于指定精度的日期和时间。 示例： 2006-08-14 02:34:56-06:00

-r,--reference=FILE 显示文件最后的修改时间

-s,--set=STRING 以字符串方式设置时间

-u,--utc,--universal 打印或者设置协调世界时(UTC)

```

## 参数  

给定的格式FORMAT 控制着输出，解释序列如下：

```sh
%% 一个文字的%(即%不起到格式化的作用)
%a 当前locale 的星期名缩写(例如： 日，代表星期日)
%A 当前locale 的星期名全称 (如：星期日)
%b 当前locale 的月名缩写 (如：一，代表一月)
%B 当前locale 的月名全称 (如：一月)
%c 当前locale 的日期和时间 (如：2005年3月3日 
%C 世纪；比如 %Y，通常为省略当前年份的后两位
%d 按月计的日期(例如：01)
%D 按月计的日期；等于%m/%d/%y
%e 按月计的日期，添加空格，等于%_d
%F 完整日期格式，等价于 %Y-%m-%d
%g ISO-8601 格式年份的最后两位 (参见%G)
%G ISO-8601 格式年份 (参见%V)，一般只和 %V 结
%h 等于%b
%H 小时(00-23)
%I 小时(00-12)
%j 按年计的日期(001-366)
%k hour, space padded ( 0..23); same as %_H
%l hour, space padded ( 1..12); same as %_I
%m month (01..12)
%M minute (00..59)
%n a newline
%N nanoseconds (000000000..999999999)
%p locale's equivalent of either AM or PM; bla
%P like %p, but lower case
%q quarter of year (1..4)
%r locale's 12-hour clock time (e.g., 11:11:04
%R 24-hour hour and minute; same as %H:%M
%s seconds since 1970-01-01 00:00:00 UTC
%S 秒(00-60)
%t 输出制表符 Tab
%T 时间，等于%H:%M:%S
%u 星期，1 代表星期一
%U 一年中的第几周，以周日为每星期第一天(00-53
%V ISO-8601 格式规范下的一年中第几周，以周一
%w 一星期中的第几日(0-6)，0 代表周一
%W 一年中的第几周，以周一为每星期第一天(00-53
%x 当前locale 下的日期描述 (如：12/31/99)
%X 当前locale 下的时间描述 (如：23:13:48)
%y 年份最后两位数位 (00-99)
%Y 年份
%z +hhmm 数字时区(例如，-0400)
%:z +hh:mm 数字时区(例如，-04:00)
%::z +hh:mm:ss 数字时区(例如，-04:00:00)
%:::z 数字时区带有必要的精度 (例如，-04
%Z 按字母表排序的时区缩写 (例如，EDT)

默认情况下，日期的数字区域以0填充
以下可选标志可能跟在'％'后面：
- 连字符，不要填充字段
_ 下划线，用空格填充
0 用0填充
^ 如果可能的话，使用大写字母
# 尽可能使用相反的情况

在任何标记之后还允许一个可选的域宽度指定，它是一个十进制数字。
作为一个可选的修饰声明，它可以是E，在可能的情况下使用本地环境关联的
表示方式；或者是O，在可能的情况下使用本地环境关联的数字符号。
例如：
将数字从纪元(1970-01-01)UTC开始转换为日期
date --date='@2147483647'

显示美国西海岸的时间（使用tzselect（1）查找TZ）
TZ='America/Los_Angeles' date

显示下周五上午9点在美国西海岸的当地时间
date --date='TZ="America/Los_Angeles" 09:00 next Fri'
```

## 实例  

```sh
# 格式化输出并用-符号连接日期：
date +"%Y-%m-%d"
2009-12-07

# 输出昨天日期：
date -d "1 day ago" +"%Y-%m-%d"或date -d "yesterday" +"%Y-%m-%d"或date -d "-1 day" +"%Y-%m-%d"
2012-11-19

# 2秒后输出：
date -d "2 second" +"%Y-%m-%d %H:%M.%S"
2012-11-20 14:21.31

# 传说中的 1234567890 秒：
date -d "1970-01-01 1234567890 seconds" +"%Y-%m-%d %H:%m:%S"
2009-02-13 23:02:30

# 普通转格式：
date -d "2009-12-12" +"%Y/%m/%d %H:%M.%S"
2009/12/12 00:00.00

# apache格式转换：
date -d "Dec 5, 2009 12:00:37 AM" +"%Y-%m-%d %H:%M.%S"
2009-12-05 00:00.37

# 格式转换后时间游走：
date -d "Dec 5, 2009 12:00:37 AM 2 year ago" +"%Y-%m-%d %H:%M.%S"
2007-12-05 00:00.37

# 加减操作：
date +%Y%m%d                   //显示前天年月日
date -d "+1 day" +%Y%m%d       //显示前一天的日期
date -d "-1 day" +%Y%m%d       //显示后一天的日期
date -d "-1 month" +%Y%m%d     //显示上一月的日期
date -d "+1 month" +%Y%m%d     //显示下一月的日期
date -d "-1 year" +%Y%m%d      //显示前一年的日期
date -d "+1 year" +%Y%m%d      //显示下一年的日期

# 设定时间：
date -s                        //设置当前时间，只有root权限才能设置，其他只能查看
date -s 20120523               //设置成20120523，这样会把具体时间设置成空00:00:00
date -s 01:01:01               //设置具体时间，不会对日期做更改
date -s "01:01:01 2012-05-23"  //这样可以设置全部时间
date -s "01:01:01 20120523"    //这样可以设置全部时间
date -s "2012-05-23 01:01:01"  //这样可以设置全部时间
date -s "20120523 01:01:01"    //这样可以设置全部时间

# 有时需要检查一组命令花费的时间，举例：
#!/bin/bash

start=$(date +%s)
nmap man.linuxde.net &> /dev/null

end=$(date +%s)
difference=$(( end - start ))
echo $difference seconds.
```
