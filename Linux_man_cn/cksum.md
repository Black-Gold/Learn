# cksum

## 说明

**cksum命令** 输出每个文件的 CRC 校验值和字节统计，确保文件从一个系统传输到另一个系统的过程中不被损坏。这种方法要求校验和在源系统中被计算出来，在目的
系统中又被计算一次，两个数字进行比较，如果校验和相等，则该文件被认为是正确传输了

注意：CRC是指一种排错检查方法，即循环冗余校验法

指定文件交由cksum命令进行校验后，会返回校验结果供用户核对文件是否正确无误。若不指定任何文件名称或是所给予的文件名为"-"，则cksum命令会从
标准输入设备中读取数据

## 实例

```bash
cksum testfile1            #对指定文件进行CRC校验
```
