# **lsblk**

## 说明

**lsblk命令** 用于列出所有可用块设备的信息，而且还能显示他们之间的依赖关系，但是它不会列出RAM盘的信息。块设备有硬盘，闪存盘，cd-ROM等等
lsblk命令包含在util-linux-ng包中，现在该包改名为util-linux。这个包带了几个其它工具，如dmesg。要安装lsblk，请在此处下载util-linux包
Fedora用户可以通过命令`sudo yum install util-linux-ng`来安装该包

## 选项

```markdown
用法：lsblk [选项] [<设备> ...]

-a, --all            打印所有设备
-b, --bytes          以字节为单位而非易读的格式来打印 SIZE
-d, --nodeps         不打印从属设备(slave)或占位设备(holder)
-D, --discard        打印时丢弃能力
-e, --exclude <列表>  根据主设备号排除设备(默认：内存盘)
-I, --include <列表>  只显示有指定主设备号的设备
-f, --fs             输出文件系统信息
-h, --help           使用信息(此信息)
-i, --ascii          只使用 ascii 字符
-m, --perms          输出权限信息
-l, --list           使用列表格式的输出
-n, --noheadings     不打印标题
-o, --output <列表>   输出列
-p, --paths          打印完整设备路径
-P, --pairs          使用 key=“value” 输出格式
-r, --raw            使用原生输出格式
-s, --inverse        反向依赖
-t, --topology       输出拓扑信息
-S, --scsi           输出有关 SCSI 设备的信息

可用列(用于 --output)：
        NAME  设备名
       KNAME  internal kernel device name
     MAJ:MIN  主:次 设备号
      FSTYPE  文件系统类型
  MOUNTPOINT  where the device is mounted
       LABEL  filesystem LABEL
        UUID  filesystem UUID
   PARTLABEL  分区 LABEL
    PARTUUID  分区 UUID
          RA  read-ahead of the device
          RO  只读设备
          RM  removable device
       MODEL  device identifier
      SERIAL  disk serial number
        SIZE  size of the device
       STATE  设备的状态
       OWNER  user name
       GROUP  group name
        MODE  device node permissions
   ALIGNMENT  alignment offset
      MIN-IO  minimum I/O size
      OPT-IO  optimal I/O size
     PHY-SEC  物理扇区大小
     LOG-SEC  逻辑扇区大小
        ROTA  rotational device
       SCHED  I/O scheduler name
     RQ-SIZE  request queue size
        TYPE  device type
    DISC-ALN  discard alignment offset
   DISC-GRAN  discard granularity
    DISC-MAX  discard max bytes
   DISC-ZERO  忽略零数据
       WSAME  write same max bytes
         WWN  unique storage identifier
        RAND  adds randomness
      PKNAME  internal parent kernel device name
        HCTL  Host:Channel:Target:Lun for SCSI
        TRAN  device transport type
         REV  device revision
      VENDOR  device vendor

```

## 实例

```bash
lsblk   # lsblk命令默认情况下将以树状列出所有块设备

: << comment
NAME   MAJ:MIN rm   SIZE RO type mountpoint
sda      8:0    0 232.9G  0 disk 
├─sda1   8:1    0  46.6G  0 part /

输出详解如下：
NAME ：      块设备名
MAJ:MIN ：   显示主要和次要设备号
RM ：        显示设备是否可移动设备。注意，在本例中设备sdb和sr0的RM值等于1，这说明他们是可移动设备
SIZE ：      列出设备的容量大小信息。例如298.1G表明该设备大小为298.1GB，而1K表明该设备大小为1KB
RO ：        表明设备是否为只读。在本案例中，所有设备的RO值为0，表明他们不是只读的
TYPE ：      显示块设备是否是磁盘或磁盘上的一个分区。在本例中，sda和sdb是磁盘，而sr0是只读存储（rom）
MOUNTPOINT ：本栏指出设备挂载的挂载点
comment

lsblk -a    # 默认选项不会列出所有空设备。-a选项可查看这些空设备
lsblk -nl   # 以列表格式输出设备
lsblk -s    # -S列出SCSI设备，而-s是逆序选项（将设备和分区的组织关系逆转过来显示）

```

