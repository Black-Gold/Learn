#!/bin/bash

LeapYear=`date +%Y`

# 方法一
# if [ $[$LeapYear % 400 ] -eq 0 ] ; then
#     echo "闰年"
# elif [ $[$LeapYear % 4 ] -eq 0 ] ; then
#     if [ $[$LeapYear % 100 ] -ne 0 ] ; then
#         echo "闰年"
#     else
#         echo "不是闰年"
#     fi
# else
#     echo "不是闰年"
# fi

# 方法二，利用布尔运算实现
if (( ("$LeapYear" % 400) == "0" )) || (( ("$LeapYear" % 4 == 0) && ("$LeapYear" % 100 != "0") )) ; then
    echo "闰年"
else
    echo "不是闰年"
fi

# 这相当于let语句。如果你尝试类似$ [$ year％400]的东西，你会在这里使用方括号卡住，因为在这里，方括号本身并不代表实际的命令。