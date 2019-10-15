#!/bin/bash
# 测试硬盘空间
DiskSpace=`df -h | awk '{print $5}' | grep % | sort -n | tail -1 | grep -v 已用 | cut -d "%" -f 1`

case $DiskSpace in 
[1-6]*)
    Message="nothing";;
[7-8]*)
    Message="Start thinking about cleaning out some stuff.  There's a partition that is $space % full.";;
9[1-8])
    Message="Better hurry with that new disk...  One partition is $space % full.";;
99)
    Message="I'm drowning here!  There's a partition at $space %!";;
*)
    Message="I seem to be running with an nonexistent amount of disk space...";;
esac

echo $Message