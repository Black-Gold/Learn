# **mount**

## 说明

**mount命令** Linux mount命令是经常会使用到的命令，它用于挂载Linux系统外的文件

```markdown
 mount [-lhV]
 mount -a [选项]
 mount [选项] [--source] <源> | [--target] <目录>
 mount [选项] <源> <目录>
 mount <操作> <挂载点> [<目标>]

选项：
 -a, --all               挂载 fstab 中的所有文件系统
 -c, --no-canonicalize   不对路径规范化
 -f, --fake              空运行；跳过 mount(2) 系统调用,通常用在除错的用途
 -F, --fork              对每个设备禁用 fork(和 -a 选项一起使用)
 -T, --fstab <路径>      /etc/fstab 的替代文件
 -h, --help              显示此帮助并退出
 -i, --internal-only     不调用 mount.<类型> 助手程序
 -l, --show-labels       列出所有带有指定标签的挂载
 -n, --no-mtab           不写 /etc/mtab
 -o, --options <列表>    挂载选项列表，以英文逗号分隔
 -O, --test-opts <列表>  限制文件系统集合(和 -a 选项一起使用)
 -r, --read-only         以只读方式挂载文件系统(同 -o ro)
 -t, --types <列表>      限制文件系统类型集合
     --source <源>       指明源(路径、标签、uuid)
     --target <目标>     指明挂载点
 -v, --verbose           打印当前进行的操作
 -V, --version           显示版本信息并退出
 -w, --rw, --read-write  以读写方式挂载文件系统(默认)

源：
 -L, --label <标签>      同 LABEL=<label>
 -U, --uuid <uuid>       同 UUID=<uuid>
 LABEL=<标签>            按文件系统标签指定设备
 UUID=<uuid>             按文件系统 UUID 指定设备
 PARTLABEL=<标签>        按分区标签指定设备
 PARTUUID=<uuid>         按分区 UUID 指定设备
 <设备>                  按路径指定设备
 <目录>                  绑定挂载的挂载点(参阅 --bind/rbind)
 <文件>                  用于设置回环设备的常规文件

操作：
 -B, --bind              挂载其他位置的子树(同 -o bind)
 -M, --move              将子树移动到其他位置
 -R, --rbind             挂载其他位置的子树及其包含的所有挂载
 --make-shared           将子树标记为 共享
 --make-slave            将子树标记为 从属
 --make-private          将子树标记为 私有
 --make-unbindable       将子树标记为 不可绑定
 --make-rshared          递归地将整个子树标记为 共享
 --make-rslave           递归地将整个子树标记为 从属
 --make-rprivate         递归地将整个子树标记为 私有
 --make-runbindable      递归地将整个子树标记为 不可绑定

```

## 实例

```bash
mount /dev/hda1 /mnt    # 将/dev/hda1挂在/mnt之下
mount | column -t   # 以表格形式输出
mount -t smbfs -o fmask=666,guest //windows_box/share /mnt/share    # 挂载一个windows共享
mount -o ro /dev/hda1 /mnt 将/dev/hda1用只读模式挂在/mnt之下
mount -o loop /tmp/image.iso /mnt/cdrom    # 将/tmp/image.iso光碟的image使用loop模式挂在/mnt/cdrom下。可不烧录检视光碟
```
