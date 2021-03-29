# **umount**

## 说明

**umount命令** 用于卸载已经加载的文件系统。利用设备名或挂载点都能umount文件系统，不过最好还是通过挂载点卸载，以免使用绑定挂载（一个设备，多个挂载点）时产生混乱

```markdown
-a                  卸除/etc/mtab中记录的所有文件系统
-h                  显示帮助
-n                  卸除时不要将信息存入/etc/mtab文件中
-r                  若无法成功卸除，则尝试以只读的方式重新挂入文件系统
-t<文件系统类型>      仅卸除选项中所指定的文件系统
-v                  执行时显示详细的信息
```

## 实例

```bash
umount -v /dev/sda1 # 通过设备名卸载
umount -v /mnt/mymount/ # 通过挂载点卸载
umount -vl /mnt/mymount/    # 延迟卸载，对付系统文件正忙的另一种方法是执行延迟卸载

eject /dev/cdrom      卸载并弹出CD
```
