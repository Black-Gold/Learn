# **poweroff**

  

```sh
--halt       Halt the machine
-p --poweroff  Switch off the machine
   --reboot    Reboot the machine
-f --force     Force immediate halt/power-off/reboot(不调用shutdown)
-w --wtmp-only Don't halt/power-off/reboot, just write wtmp record(并不实际关闭系统，只是写入/var/log/wtmp文件中)
-d --no-wtmp   Don't write wtmp record
   --no-wall   Don't send wall message before halt/power-off/reboot
```
