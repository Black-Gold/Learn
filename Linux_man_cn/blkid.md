# **blkid**

## 说明

在Linux下可以使用 **blkid命令** 对查询设备上所采用文件系统类型进行查询。blkid主要用来对系统的块设备（包括交换分区）所使用的文件系统类型、
LABEL、UUID等信息进行查询。要使用这个命令必须安装e2fsprogs软件包

## info

```markdown
用法：
blkid -L <label> | -U <uuid>

blkid [-c <file>] [-ghlLv] [-o <format>] [-s <tag>] 
      [-t <token>] [<dev>]

blkid -p [-s <tag>] [-O <offset>] [-S <size>] 
      [-o <format>] <dev>

blkid -i [-s <tag>] [-o <format>] <dev>

选项：
-c <file>   read from <file> instead of reading from the default cache file (-c /dev/null means no cache)
-d          don't encode non-printing characters
-h          print this usage message and exit
-g          garbage collect the blkid cache
-o <format> output format; can be one of:value, device, export or full; (default: full)
-k          list all known filesystems/RAIDs and exit
-s <tag>    show specified tag(s) (default show all tags)
-t <token>  find device with a specific token (NAME=value pair)
-l          look up only first device with token specified by -t
-L <label>  convert LABEL to device name
-U <uuid>   convert UUID to device name
-V          print version and exit
<dev>       specify device(s) to probe (default: all devices)

Low-level probing options:
 -p          low-level superblocks probing (bypass cache)
 -i          gather information about I/O limits
 -S <size>   overwrite device size
 -O <offset> probe at the given offset
 -u <list>   filter by "usage" (e.g. -u filesystem,raid)
 -n <list>   filter by filesystem type (e.g. -n vfat,ext3)

```

## 实例

```bash
blkid   # 列出当前系统中所有已挂载文件系统的类型
blkid -s UUID /dev/sda1     # 显示指定设备 UUID
blkid -s LABEL /dev/sda5    # 显示指定设备label
blkid -s TYPE   # 显示设备文件系统
blkid -o device # 显示所有设备
blkid -o list   # 以列表方式查看所有设备的相信信息

```
