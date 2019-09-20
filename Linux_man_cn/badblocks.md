# badblocks

## 说明

**badblock命令** 用于查找磁盘中损坏的区块。 硬盘是一个损耗设备，当使用一段时间后可能会出现坏道等物理故障。电脑硬盘
出现坏道后，如果不及时更换或进行技术处理，坏道就会越来越多，并会造成频繁死机和数据丢失。最好的处理方式是更换磁盘，但
在临时的情况下，应及时屏蔽坏道部分的扇区，不要触动它们。badblocks就是一个很好的检查坏道位置的工具

## 选项

```markdown
OPTIONS
-b block-size           指定磁盘的区块大小,默认是bytes为单位大小为1024
-c number of blocks     is the number of blocks which are tested at a time.  The default is 64
-e max bad block count  在中止测试之前指定最大数量的坏块。 默认值为0，表示测试将持续到达测试范围结束
-d read delay factor    如果读取操作中没有遇到错误，则此参数（如果已传递且非零）将导致坏块在读取之间休眠; 延迟将计算
                        为执行读取操作所用时间的百分比。 换句话说，值100将导致每次读取延迟前一次读取所花费的数量，并且
                        值为200的两倍量
-f     
-i input_file
-e max bad block count  在中止测试之前指定最大数量的坏块。 默认值为0，表示测试将持续到达测试范围结束
-o output_file          将检查的结果写入指定的输出文件
-p num_passes
-s                      在检查时显示进度

# 参数
*   磁盘装置：指定要检查的磁盘装置
*   磁盘区块数：指定磁盘装置的区块总数
*   启始区块：指定要从哪个区块开始检查
```

## 实例

```bash
# badblocks以4096的一个block，每一个block检查16次，将结果输出到hda-badblocks-list文件里
badblocks -b 4096 -c 16 /dev/hda1 -o hda-badblocks-list

```
