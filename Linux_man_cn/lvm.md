# *LVM*

## **pvcreate**

## 选项

```info
-f  强制创建物理卷，不需要用户确认
-u  指定设备的UUID
-y  所有的问题都回答“yes”
-Z  是否利用前4个扇区
```

### 参数  

物理卷：指定要创建的物理卷对应的设备文件名。

### 实例  

查看磁盘信息：

```
[root@localhost ~]# fdisk -l
Disk /dev/hda: 41.1 GB, 41174138880 bytes
255 heads, 63 sectors/track, 5005 cylinders
Units = cylinders of 16065 * 512 = 8225280 bytes

   Device Boot      Start         End      Blocks   id  System
/dev/hda1   *           1          13      104391   83  Linux
/dev/hda2              14        1288    10241437+  83  Linux
/dev/hda3            1289        1925     5116702+  83  Linux
/dev/hda4            1926        5005    24740100    5  Extended
/dev/hda5            1926        2052     1020096   82  Linux swap / Solaris
/dev/hda6            2053        2235     1469916   8e  Linux LVM
/dev/hda7            2236        2418     1469916   8e  Linux LVM
/dev/hda8            2419        2601     1469916   8e  Linux LVM
/dev/hda9            2602        2784     1469916   8e  Linux LVM

```

检查有无 PV 在系统上，然后将`/dev/hda6`到`/dev/hda9`建立成为PV格式

```
[root@localhost ~]# pvscan
No matching physical volumes found    #找不到任何的 PV 存在！
```

将6-9分区转成pv，注意大括号的用途：

```
[root@localhost ~]# pvcreate /dev/hda{6,7,8,9}
  Physical volume "/dev/hda6" successfully created
  Physical volume "/dev/hda7" successfully created
  Physical volume "/dev/hda8" successfully created
  Physical volume "/dev/hda9" successfully created
```

这就分別表示每个 PV 的信息与系统所有 PV 的信息：

```
[root@localhost ~]# pvscan
  PV /dev/hda6         lvm2 [1.40 GB]
  PV /dev/hda7         lvm2 [1.40 GB]
  PV /dev/hda8         lvm2 [1.40 GB]
  PV /dev/hda9         lvm2 [1.40 GB]
  Total: 4 [5.61 GB] / in use: 0 [0   ] / in no VG: 4 [5.61 GB]
```

更详细的列示出系统上面每个 PV 信息：

```
[root@localhost ~]# pvdisplay
  "/dev/hda6" is a new physical volume of "1.40 GB"
  --- NEW Physical volume ---
  PV Name               /dev/hda6  #实际的 partition 分区名称
  VG Name                          #因为尚未分配出去，所以空白！
  PV Size               1.40 GB    #就是容量说明
  Allocatable           NO         #是否已被分配，结果是 NO
  PE Size (KByte)       0          #在此 PV 內的 PE 大小
  Total PE              0          #共分割出几个 PE
  free PE               0          #沒被 LV 用掉的 PE
  Allocated PE          0          #尚可分配出去的 PE 数量
  PV UUID               Z13Jk5-RCls-UJ8B-HzDa-Gesn-atku-rf2biN
....(底下省略)....
```

删除物理卷：

```
[root@localhost ~]# pvremove /dev/sdb2
Labels on physical volume "/dev/sdb2" successfully wiped

```

修改物理卷属性：

```
[root@localhost ~]# pvchange -x n /dev/sdb1    #禁止分配指定物理卷上的PE
Physical volume "/dev/sdb1" changed  
1 physical volume changed / 0 physical volumes not changed 
```

**pvscan命令** 会扫描系统中连接的所有硬盘，列出找到的物理卷列表。使用pvscan命令的`-n`选项可以显示硬盘中的不属于任何卷组的物理卷，这些物理卷是未被使用的。

### 语法  

```
pvscan(选项)
```

### 选项  

```
-d：调试模式；
-e：仅显示属于输出卷组的物理卷；
-n：仅显示不属于任何卷组的物理卷；
-s：短格式输出；
-u：显示UUID。
```

### 实例  

使用pvscan命令扫描当前系统中所有硬盘的物理卷，在命令行中输入下面的命令：

```
[root@localhost ~]# pvscan     #扫描所有硬盘上的物理卷 
```

输出信息如下：

```
PV /dev/sdb1         lvm2 [101.94 MB]  
PV /dev/sdb2         lvm2 [101.98 MB]  
Total: 2 [203.92 MB] / in use: 0 [0   ] / in no VG: 2 [203.92  
MB] 
```

说明：本例中，输出了两个物理卷，它们不属于任何卷组，是可被利用的物理卷。

**pvdisplay命令** 用于显示物理卷的属性。pvdisplay命令显示的物理卷信息包括：物理卷名称、所属的卷组、物理卷大小、PE大小、总PE数、可用PE数、已分配的PE数和UUID。

## 选项

```info
-s  以短格式输出；
-m  显示PE到LE的映射。
```

## LVM(逻辑卷管理)

```sh
概念介绍：
LVM （logical volume Manager）逻辑卷管理通过将底层物理硬盘抽象封装起来，以逻辑卷的形式表现给上层系统，逻辑卷的大小可以动态调整的而且不会丢失数据。新加入的硬盘也不会改变现有上层的逻辑卷；

LVM特点：
1.作为一个动态磁盘管理机制，逻辑卷技术大大提高了磁盘管理的灵活性；
2.LVM屏蔽了底层磁盘布局，便于动态的调整磁盘空间大小；

相关概念：
PE（物理拓展单元)   #逻辑卷空间管理的基本单位，默认是4M的大小；
PV 物理卷
VG 卷组
LV 逻辑卷

LVM原理解析：
1.物理磁盘被格式化为PV，空间被分为一个个的PE
2.不同的PV加入同一个VG，不同的PV的PE全部进入VG的PE池；
3.LV基于PE创建，大小为PE的整数倍，组成LV的PE可能来自不同物理磁盘；
4.LV格式化完成后挂载就可以使用了
5.LV的扩充缩减实际上就是增加了或者减少了组成该LV的PE的数量。其过程不会丢失数据信息；
```

FAQ:(Frequently Asked Question)
1.LV的大小应该由PE大小和PE数量决定;默认PE为4M大小的情况下一个逻辑卷最大可以支持256G
2.逻辑卷可以动态扩充的大小取决于卷组的大小
3.PE的大小最终影响 逻辑卷的最大大小，逻辑卷的大小一定是PE的整数倍
5.一个逻辑卷只能属于一个卷组

## LVM拉伸逻辑卷

```sh
(可在线扩容，无需卸载逻辑卷)
vgdisplay或vgs  # 确保VG中有足够的空闲空间，通过以下指令查询即可
lvextend -L +5G /dev/vg01/lv01     # 扩充逻辑卷,增大5G的大小
resize2fs /dev/vg01/lv01      # 更新文件系统(检测磁盘的大小)
df -hT     # 查看更新后文件系统

备注：在没有使用命令resize2fs命令之前，使用df -hT 命令看到逻辑卷的大小并没有变化，为什么？
逻辑卷是底层的东西，操作系统要使用底层的空间需要创建文件系统，创建文件系统（格式化操作）的时候大小就固定下来，因此逻辑卷的大小也是固定的。在拉伸逻辑卷空间时，并没有更新文件系统，所以要要执行更新文件系统的操作，要操作系统识别固定的大小；
```

## LVM缩小逻辑卷

```sh
(在实际运作当中很少使用且这种操作及其危险,容易导致数据丢失)备注:逻辑卷的缩小必须是离线操作，要卸载逻辑卷；
umount /dev/vg01/lv01   # 卸载已经挂载的逻辑卷
e2fsck -f /dev/vg01/lv01    # 强制检测文件系统信息
resize2fs /dev/vg01/lv01 10G # 缩小文件系统(一般都有提示信息)指定逻辑卷大小为10G大小；
lvreduce -L 10G /dev/vg01/lv01      # 缩小LV
lvdisplay； lvs ; lvscan    # 查看缩小后的LV
mount /dev/vg01/lv01 /mnt   # 挂载

切记：严格按照顺序执行命令。先缩小文件系统，后缩小底层空间
```

## LVM拉伸卷组

```sh
pvcreate /dev/sdd    # 创建新的物理卷
vgextend vg01 /dev/sdd  # 向vg01卷组中添加物理卷/dev/sdd
vgs, vgdisplay     # 查看卷组信息
```

## LVM缩小卷组

```sh
vgreduce vg01 /dev/sdd    # 将一个PV从指定卷组中移除
vgdisplay或vgs  # 查看缩小后的卷组大小
```

**pvchange命令** 允许管理员改变物理卷的分配许可。如果物理卷出现故障，可以使用pvchange命令禁止分配物理卷上的PE。

### 语法  

```
pvchange(选项)(参数)
```

### 选项  

```
-u：生成新的UUID；
-x：是否允许分配PE。
```

### 参数  

物理卷：指定要修改属性的物理卷所对应的设备文件。

### 实例  

使用pvchange命令禁止分配指定物理卷上的PE。在命令行中输入下面的命令：

```
pvchange -x n /dev/sdb1     #禁止分配"/dev/sdb1"上的PE
```

输出信息如下：

```
Physical volume "/dev/sdb1" changed  
1 physical volume changed / 0 physical volumes not changed
```

**pvremove命令** 用于删除一个存在的物理卷。使用pvremove指令删除物理卷时，它将LVM分区上的物理卷信息删除，使其不再被视为一个物理卷。

### 语法  

```
pvremove(选项)(参数)
```

### 选项  

```
-d：调试模式；
-f：强制删除；
-y：对提问回答“yes”。
```

### 参数  

物理卷：指定要删除的物理卷对应的设备文件名。

### 实例  

使用pvremove指令删除物理卷`/dev/sdb2`。在命令行中输入下面的命令：

```
pvremove /dev/sdb2 #删除物理卷
Labels on physical volume "/dev/sdb2" successfully wiped

```

**pvdisplay命令** 用于显示物理卷的属性。pvdisplay命令显示的物理卷信息包括：物理卷名称、所属的卷组、物理卷大小、PE大小、总PE数、可用PE数、已分配的PE数和UUID。

## 选项

```info
-s  以短格式输出；
-m  显示PE到LE的映射。
```

## LVM(逻辑卷管理)

```sh
概念介绍：
LVM （logical volume Manager）逻辑卷管理通过将底层物理硬盘抽象封装起来，以逻辑卷的形式表现给上层系统，逻辑卷的大小可以动态调整的而且不会丢失数据。新加入的硬盘也不会改变现有上层的逻辑卷；

LVM特点：
1.作为一个动态磁盘管理机制，逻辑卷技术大大提高了磁盘管理的灵活性；
2.LVM屏蔽了底层磁盘布局，便于动态的调整磁盘空间大小；

相关概念：
PE（物理拓展单元)   #逻辑卷空间管理的基本单位，默认是4M的大小；
PV 物理卷
VG 卷组
LV 逻辑卷

LVM原理解析：
1.物理磁盘被格式化为PV，空间被分为一个个的PE
2.不同的PV加入同一个VG，不同的PV的PE全部进入VG的PE池；
3.LV基于PE创建，大小为PE的整数倍，组成LV的PE可能来自不同物理磁盘；
4.LV格式化完成后挂载就可以使用了
5.LV的扩充缩减实际上就是增加了或者减少了组成该LV的PE的数量。其过程不会丢失数据信息；
```

FAQ:(Frequently Asked Question)
1.LV的大小应该由PE大小和PE数量决定;默认PE为4M大小的情况下一个逻辑卷最大可以支持256G
2.逻辑卷可以动态扩充的大小取决于卷组的大小
3.PE的大小最终影响 逻辑卷的最大大小，逻辑卷的大小一定是PE的整数倍
5.一个逻辑卷只能属于一个卷组

## LVM拉伸逻辑卷

```sh
(可在线扩容，无需卸载逻辑卷)
vgdisplay或vgs  # 确保VG中有足够的空闲空间，通过以下指令查询即可
lvextend -L +5G /dev/vg01/lv01     # 扩充逻辑卷,增大5G的大小
resize2fs /dev/vg01/lv01      # 更新文件系统(检测磁盘的大小)
df -hT     # 查看更新后文件系统

备注：在没有使用命令resize2fs命令之前，使用df -hT 命令看到逻辑卷的大小并没有变化，为什么？
逻辑卷是底层的东西，操作系统要使用底层的空间需要创建文件系统，创建文件系统（格式化操作）的时候大小就固定下来，因此逻辑卷的大小也是固定的。在拉伸逻辑卷空间时，并没有更新文件系统，所以要要执行更新文件系统的操作，要操作系统识别固定的大小；
```

## LVM缩小逻辑卷

```sh
(在实际运作当中很少使用且这种操作及其危险,容易导致数据丢失)备注:逻辑卷的缩小必须是离线操作，要卸载逻辑卷；
umount /dev/vg01/lv01   # 卸载已经挂载的逻辑卷
e2fsck -f /dev/vg01/lv01    # 强制检测文件系统信息
resize2fs /dev/vg01/lv01 10G # 缩小文件系统(一般都有提示信息)指定逻辑卷大小为10G大小；
lvreduce -L 10G /dev/vg01/lv01      # 缩小LV
lvdisplay； lvs ; lvscan    # 查看缩小后的LV
mount /dev/vg01/lv01 /mnt   # 挂载

切记：严格按照顺序执行命令。先缩小文件系统，后缩小底层空间
```

## LVM拉伸卷组

```sh
pvcreate /dev/sdd    # 创建新的物理卷
vgextend vg01 /dev/sdd  # 向vg01卷组中添加物理卷/dev/sdd
vgs, vgdisplay     # 查看卷组信息
```

## LVM缩小卷组

```sh
vgreduce vg01 /dev/sdd    # 将一个PV从指定卷组中移除
vgdisplay或vgs  # 查看缩小后的卷组大小
```