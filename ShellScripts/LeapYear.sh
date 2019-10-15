#!/bin/bash

: '
方法一
LeapYear=`date +%Y`

if [ $[ $LeapYear % 400 ] -eq 0 ] ; then
    echo "闰年"
elif [ $[ $LeapYear % 4 ] -eq 0 ] ; then
    if [ $[ $LeapYear % 100 ] -ne 0 ] ; then
        echo "闰年"
    else
        echo "不是闰年"
    fi
else
    echo "不是闰年"
fi
'

: '
# 方法二，利用布尔运算实现
LeapYear=`date +%Y`

if (( ( "$LeapYear" % 400 ) == "0" )) || (( ( "$LeapYear" % 4 == 0 ) && ( "$LeapYear" % 100 != "0" ) )) ; then
    echo "闰年"
else
    echo "不是闰年"
fi

# 这相当于let语句。如果你尝试类似$ [$ year％400]的东西，你会在这里使用方括号卡住，因为在这里，方括号本身并不代表实际的命令。
'

# 利用read命令进行交互式判断实例
echo "请输入您想要判断是否为闰年的日期(四个数字),然后按enter："

read LeapYear

if (( ("$LeapYear" % 400 ) == 0 )) || (( ("$LeapYear" % 4 == 0 ) && ( "$LeapYear" % 100 != 0 ) )); then

    echo "闰年"
else
    echo "不是闰年"
fi