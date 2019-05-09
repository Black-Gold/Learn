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

## 实例

，然后将`/dev/hda6`到`/dev/hda9`建立成为PV格式

```sh
pvscan  # 检查有无 PV在系统上，找不到任何的 PV 存在！
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
6.执行lvm操作时，先前的meta元数据都保存在/etc/lvm/archive目录，用vgcfgrestore可进行恢复操作

## LVM拉伸逻辑卷

```sh
(可在线扩容，无需卸载逻辑卷)
vgdisplay或vgs  # 确保VG中有足够的空闲空间，通过以下指令查询即可
lvextend -L +5G /dev/vg01/lv01     # 扩充逻辑卷,增大5G的大小
resize2fs /dev/vg01/lv01      # 更新文件系统(检测磁盘的大小)ext4格式命令
xfs_growfs /dev/vg01/lv01     # 更新文件系统(检测磁盘的大小)xfs格式命令
df -hT     # 查看更新后文件系统

备注：在没有使用命令resize2fs命令之前，使用df -hT 命令看到逻辑卷的大小并没有变化，为什么？
逻辑卷是底层的东西，操作系统要使用底层的空间需要创建文件系统，创建文件系统（格式化操作）的时候大小就固定下来，因此逻辑卷的大小也是固定的。在拉伸逻辑卷空间时，并没有更新文件系统，所以要要执行更新文件系统的操作，要操作系统识别固定的大小；
```

## LVM缩小逻辑卷

```sh
(在实际运作当中很少使用且这种操作及其危险,容易导致数据丢失)备注:逻辑卷的缩小必须是离线操作，要卸载逻辑卷；xfsdump可备份xfs系统格式
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

**vgcreate命令** 用于创建LVM卷组。卷组（Volume Group）将多个物理卷组织成一个整体，屏蔽了底层物理卷细节。在卷组上创建逻辑卷时不用考虑具体的物理卷信息。

### 语法  

```
vgcreate(选项)(参数)
```

### 选项  

```
-l：卷组上允许创建的最大逻辑卷数；
-p：卷组中允许添加的最大物理卷数；
-s：卷组上的物理卷的PE大小。
```

### 参数  

*   卷组名：要创建的卷组名称；
*   物理卷列表：要加入到卷组中的物理卷列表。

### 实例  

使用vgcreate命令创建卷组 "vg1000"，并且将物理卷`/dev/sdb1`和`/dev/sdb2`添加到卷组中。在命令行中输入下面的命令：

```
[root@localhost ~]# vgcreate vg1000 /dev/sdb1 /dev/sdb2  #创建卷组"vg1000"
```

输出信息如下：

```
Volume group "vg1000" successfully created
```

**vgdisplay命令** 用于显示LVM卷组的信息。如果不指定"卷组"参数，则分别显示所有卷组的属性。

### 语法  

```
vgdisplay(选项)(参数)
```

### 选项  

```
-A：仅显示活动卷组的属性；
-s：使用短格式输出的信息。
```

### 参数  

卷组：要显示属性的卷组名称。

### 实例  

使用vgdisplay命令显示存在的卷组"vg1000"的属性。在命令行中输入下面的命令：

```
[root@localhost ~]# vgdisplay vg1000     #显示卷组"vg1000"的属性
```

输出信息如下：

```
  --- Volume group ---  
  VG Name               vg1000  
......省略部分输出内容......  
  free  PE / Size       50 / 200.00 MB  
  VG UUID  ICprwg-ZmhA-JKYF-WYuy-jNHa-AyCN-ZS5F7B
```


**vgscan命令** 查找系统中存在的LVM卷组，并显示找到的卷组列表。vgscan命令仅显示找到的卷组的名称和LVM元数据类型，要得到卷组的详细信息需要使用vgdisplay命令。

### 语法  

```
vgscan(选项)
```

### 选项  

```
-d：调试模式；
--ignorerlockingfailure：忽略锁定失败的错误。
```

### 实例  

使用vgscan命令扫描系统中所有的卷组。在命令行中输入下面的命令：

```
[root@localhost ~]# vgscan     #扫描并显示LVM卷组列表
```

输出信息如下：

```
Found volume group "vg2000" using metadata type lvm2  
Found volume group "vg1000" using metadata type lvm2 
```

说明：本例中，vgscan指令找到了两个LVM2卷组"vg1000"和"vg2000"。

**grename命令** 可以重命名卷组的名称。

### 语法  

```
vgrename [选项] [旧卷组路径|旧卷组名称|旧卷组UUID] [新卷组路径|新卷组名称]
```

### 选项  

```
-d 启用调试模式
-t 启用测试模式
```

### 例子

重命名卷组/dev/vg1为/dev/vg2。

```bash
[root@localhost ~]# vgrename /dev/vg1 /dev/vg2
  Volume group "vg1" successfullyrenamed to "vg2"
```

重命名卷组vg1为vg2。

```bash
[root@localhost ~]# vgrename vg1 vg2
  Volume group "vg1" successfully renamed to "vg2"
```
**vgchange命令** 用于修改卷组的属性，经常被用来设置卷组是处于活动状态或非活动状态。处于活动状态的卷组无法被删除，必须使用vgchange命令将卷组设置为非活动状态后才能删除。

### 语法  

```
vgchange(选项)(参数)
```

### 选项  

```
-a：设置卷组的活动状态。
```

### 参数  

卷组：指定要设置属性的卷组。

### 实例  

使用vgchange命令将卷组状态改为活动的。在命令行中输入下面的命令：

```
[root@localhost ~]# vgchange -ay vg1000     #将卷组"vg1000"设置为活动状态
```

输出信息如下：

```
1 logical volume(s) in volume group "vg1000" now active
```

**vgremove命令** 用于用户删除LVM卷组。当要删除的卷组上已经创建了逻辑卷时，vgremove命令需要进行确认删除，防止误删除数据。

### 语法  

```
vgremove(选项)(参数)
```

### 选项  

```
-f：强制删除。
```

### 参数  

卷组：指定要删除的卷组名称。

### 实例  

使用vgremove命令删除LVM卷组"vg1000"。在命令行中输入下面的命令：

```
[root@localhost ~]# vgremove vg1000    #删除卷组"vg1000"
Volume group "vg1000" successfully removed
```

**vgconvert命令** 用于转换指定LVM卷组的元数据格式，通常将“LVM1”格式的卷组转换为“LVM2”格式。转换卷组元数据前必须保证卷组处于非活动状态，否则无法完成转换操作。

### 语法  

```
vgconvert(选项)(参数)
```

### 选项  

```
-M：要转换的卷组格式。
```

### 参数  

卷组：指定要转换格式的卷组。

### 实例  

转换卷组元数据格式前，使用vgchange命令将卷组设置为非活动状态。在命令行中输入下面的命令：

```
[root@localhost lvm]# vgchange -an vg1000    #设置卷组状态为非活动状态
0 logical volume(s) in volume group "vg1000" now active 

```

使用vgconvert命令将卷组"vg1000"从"LVM1"格式转换为"LVM2"格式。在命令行中输入下面的命令：

```
[root@localhost lvm]# vgconvert -M2 vg1000    #转换卷组为"LVM2"格式
Volume group vg1000 successfully converted
```

使用vgchange命令将卷组设置为活动状态。在命令行中输入下面的命令：

```
[root@localhost lvm]# vgchange -ay vg1000     #设置卷组状态为活动状态
0 logical volume(s) in volume group "vg1000" now active
```

**vgextend命令** 用于动态扩展LVM卷组，它通过向卷组中添加物理卷来增加卷组的容量。LVM卷组中的物理卷可以在使用vgcreate命令创建卷组时添加，也可以使用vgextend命令动态的添加。

### 语法  

```
vgextend(选项)(参数)
```

### 选项  

```
-d：调试模式；
-t：仅测试。
```

### 参数  

*   卷组：指定要操作的卷组名称；
*   物理卷列表：指定要添加到卷组中的物理卷列表。

### 实例  

使用vgextend命令向卷组"vg2000"中添加物理卷。在命令行中输入下面的命令：

```
[root@localhost ~]# vgextend vg2000 /dev/sdb2     #将物理卷"/dev/sdb2"加入卷组"vg2000"
```

输出信息如下：

```
Volume group "vg2000" successfully extended
```

**vgreduce命令** 通过删除LVM卷组中的物理卷来减少卷组容量。不能删除LVM卷组中剩余的最后一个物理卷。

### 语法  

```
vgreduce(选项)(参数)
```

### 选项  

```
-a：如果命令行中没有指定要删除的物理卷，则删除所有的空物理卷；
--removemissing：删除卷组中丢失的物理卷，使卷组恢复正常状态。
```

### 参数  

*   卷组：指定要操作的卷组名称；
*   物理卷列表：指定要删除的物理卷列表。

### 实例  

使用vgreduce命令从卷组"vg2000"中移除物理卷`/dev/sdb2`。在命令行中输入下面的命令：

```
[root@localhost ~]# vgreduce vg2000 /dev/sdb2    #将物理卷"/dev/sdb2"从卷组"vg2000"中删除
```

输出信息如下：

```
Removed "/dev/sdb2" from volume group "vg2000"
```
**lvcreate命令** 用于创建LVM的逻辑卷。逻辑卷是创建在卷组之上的。逻辑卷对应的设备文件保存在卷组目录下，例如：在卷组"vg1000"上创建一个逻辑卷"lvol0"，则此逻辑卷对应的设备文件为"/dev/vg1000/lvol0"。

### 语法  

```
lvcreate(选项)(参数)
```

### 选项  

```
-L：指定逻辑卷的大小，单位为“kKmMgGtT”字节；
-l：指定逻辑卷的大小（LE数）。
```

### 参数  

逻辑卷：指定要创建的逻辑卷名称。

### 实例  

使用lvcreate命令在卷组"vg1000"上创建一个200MB的逻辑卷。在命令行中输入下面的命令：

```
[root@localhost ~]# lvcreate -L 200M vg1000    #创建大小为200M的逻辑卷
```

输出信息如下：

```
Logical volume "lvol0" created
```

说明：创建成功后，新的逻辑卷"lvol0"，将通过设备文件`/dev/vg1000/lvol0`进行访问。

**lvscan命令** 用于扫描当前系统中存在的所有的LVM逻辑卷。使用lvscan指令可以发现系统中的所有逻辑卷，及其对应的设备文件。

### 语法  

```
lvscan(选项)
```

### 选项  

```
-b：显示逻辑卷的主设备和次设备号。
```

### 实例  

使用lvscan命令扫描系统中的所有逻辑卷。在命令行中输入下面的命令：

```
[root@localhost ~]# lvscan     #扫描所有的逻辑卷
```

输出信息如下：

```
ACTIVE          '/dev/vg1000/lvol0' [200.00 MB] inherit
```
**lvdisplay命令** 用于显示LVM逻辑卷空间大小、读写状态和快照信息等属性。如果省略"逻辑卷"参数，则lvdisplay命令显示所有的逻辑卷属性。否则，仅显示指定的逻辑卷属性。

### 语法  

```
lvdisplay(参数)
```

### 参数  

逻辑卷：指定要显示属性的逻辑卷对应的设备文件。

### 实例  

使用lvdisplay命令显示指定逻辑卷的属性。在命令行中输入下面的命令：

```
[root@localhost ~]# lvdisplay /dev/vg1000/lvol0     #显示逻辑卷属性
```

输出信息如下：

```
  --- Logical volume ---  
  LV Name                /dev/vg1000/lvol0  
......省略部分输出内容......  
  Block device           253:0
```

**lvextend命令** 用于在线扩展逻辑卷的空间大小，而不中断应用程序对逻辑卷的访问。使用lvextend命令动态在线扩展磁盘空间，整个空间扩展过程对于应用程序来说是完全透明的。

### 语法  

```
lvextend(选项)(参数)
```

### 选项  

```
-L：指定逻辑卷的大小，单位为“kKmMgGtT”字节；
-l：指定逻辑卷的大小（LE数）。
```

### 参数  

逻辑卷：指定要扩展空间的逻辑卷。

### 实例  

使用lvextend命令为逻辑卷`/dev/vg1000/lvol0`增加100M空间。在命令行中输入下面的命令：

```
[root@localhost ~]# lvextend -L +100M /dev/vg1000/lvol0    #为了解决增加100M空间
```

输出信息如下：

```
Extending logical volume lvol0 to 300.00 MB  
Logical volume lvol0 successfully resized
```
**lvresize命令** 用于调整LVM逻辑卷的空间大小，可以增大空间和缩小空间。使用lvresize命令调整逻辑卷空间大小和缩小空间时需要谨慎，因为它有可能导致数据丢失。

### 语法  

```
lvresize(选项)(参数)
```

### 选项  

```
-L：指定逻辑卷的大小，单位为“kKmMgGtT”字节；
-l：指定逻辑卷的大小（LE数）。
```

### 参数  

逻辑卷：指定要删除的逻辑卷。

### 实例  

使用lvresize命令调整最大的逻辑卷大小。在命令行中输入下面的命令：

```
[root@localhost ~]# lvresize -L +200M /dev/vg1000/lvol0     #将逻辑卷空间增加200M
```

输出信息如下：

```
Extending logical volume lvol0 to 280.00 MB
Logical volume lvol0 successfully resized
```
**lvreduce命令** 用于减少LVM逻辑卷占用的空间大小。使用lvreduce命令收缩逻辑卷的空间大小有可能会删除逻辑卷上已有的数据，所以在操作前必须进行确认。

### 语法  

```
lvreduce(选项)(参数)
```

### 选项  

```
-L：指定逻辑卷的大小，单位为“kKmMgGtT”字节；
-l：指定逻辑卷的大小（LE数）。
```

### 参数  

逻辑卷：指定要操作的逻辑卷对应的设备文件。

### 实例  

使用lvreduce命令减少指定的逻辑卷的空间大小。在命令行中输入下面的命令：

```
[root@localhost ~]# lvreduce -L -50M /dev/vg1000/lvol0     #将逻辑卷的空间大小减少50M
```

输出信息如下：

```
......省略部分输出内容......  
Do you really want to reduce lvol0? [y/n]: y  #确认操作  
  Reducing logical volume lvol0 to 252.00 MB  
  Logical volume lvol0 successfully resized
```
**lvremove命令** 用于删除指定LVM逻辑卷。如果逻辑卷已经使用mount命令加载，则不能使用lvremove命令删除。必须使用umount命令卸载后，逻辑卷方可被删除。

### 语法  

```
lvremove(选项)(参数)
```

### 选项  

```
-f：强制删除。
```

### 参数  

逻辑卷：指定要删除的逻辑卷。

### 实例  

使用lvremove命令删除指定的逻辑卷。在命令行中输入下面的命令：

```
[root@localhost ~]# lvremove /dev/vg1000/lvol0    #删除逻辑卷"lvol0"
```

输出信息如下：

```
Do you really want to remove active logical 
volume "lvol0"? [y/n]: y    #确认删除
  Logical volume "lvol0" successfully removed
```
