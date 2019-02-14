# **reboot**

## 选项  

```sh
-d --no-wtmp 重新开机时不把数据写入记录文件/var/tmp/wtmp，本参数具有“-n”参数效果
   --no-wall 在halt/power-off/reboot之前不发送wall信息
-f --force 强制立即重新开机，不调用shutdown指令的功能；
-n --no-sync 重开机之前不同步hard disks/storage media(检查是否有未结束的程序)
-w --wtmp-only 仅做测试，并不真正将系统重新开机，只会把重开机的数据写入/var/log目录下的wtmp记录文件。
```

## 实例  

```sh
reboot        //重开机。
reboot -w     //做个重开机的模拟（只有纪录并不会真的重开机）。
```
