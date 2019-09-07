# badblocks

## 说明

**badblock命令** 用于查找磁盘中损坏的区块。 硬盘是一个损耗设备，当使用一段时间后可能会出现坏道等物理故障。电脑硬盘
出现坏道后，如果不及时更换或进行技术处理，坏道就会越来越多，并会造成频繁死机和数据丢失。最好的处理方式是更换磁盘，但
在临时的情况下，应及时屏蔽坏道部分的扇区，不要触动它们。badblocks就是一个很好的检查坏道位置的工具

## 选项

```markdown
-b<区块大小>：指定磁盘的区块大小，单位为字节；
-o<输出文件>：将检查的结果写入指定的输出文件；
-s：在检查时显示进度；
-v：执行时显示详细的信息；
-w：在检查时，执行写入测试。

OPTIONS
       -b block-size
              Specify the size of blocks in bytes.  The default is 1024.

       -c number of blocks
              is the number of blocks which are tested at a time.  The default is 64.

       -e max bad block count
              Specify a maximum number of bad blocks before aborting the test.  The default is 0, meaning the test will  continue  until  the
              end of the test range is reached.

       -d read delay factor
              This parameter, if passed and non-zero, will cause bad blocks to sleep between reads if there were no errors encountered in the
              read operation; the delay will be calculated as a percentage of the time it took for the read operation  to  be  performed.  In
              other  words,  a  value  of  100 will cause each read to be delayed by the amount the previous read took, and a value of 200 by
              twice the amount.

       -f     Normally, badblocks will refuse to do a read/write or a non-destructive test on a device which is  mounted,  since  either  can
              cause  the  system  to  potentially crash and/or damage the filesystem even if it is mounted read-only.  This can be overridden
              using the -f flag, but should almost never be used --- if you think you're smarter than the badblocks program, you almost  cer‐
              tainly  aren't.   The  only  time  when  this option might be safe to use is if the /etc/mtab file is incorrect, and the device
              really isn't mounted.

       -i input_file
       -e max bad block count
              Specify a maximum number of bad blocks before aborting the test.  The default is 0, meaning the test will  continue  until  the
              end of the test range is reached.

       -d read delay factor
              This parameter, if passed and non-zero, will cause bad blocks to sleep between reads if there were no errors encountered in the
              read operation; the delay will be calculated as a percentage of the time it took for the read operation  to  be  performed.  In
              other  words,  a  value  of  100 will cause each read to be delayed by the amount the previous read took, and a value of 200 by
              twice the amount.

       -f     Normally, badblocks will refuse to do a read/write or a non-destructive test on a device which is  mounted,  since  either  can
              cause  the  system  to  potentially crash and/or damage the filesystem even if it is mounted read-only.  This can be overridden
              using the -f flag, but should almost never be used --- if you think you're smarter than the badblocks program, you almost  cer‐
              tainly  aren't.   The  only  time  when  this option might be safe to use is if the /etc/mtab file is incorrect, and the device
              really isn't mounted.

       -i input_file
              Read a list of already existing known bad blocks.  Badblocks will skip testing these blocks since they are known to be bad.  If
              input_file is specified as "-", the list will be read from the standard input.  Blocks listed in this list will be omitted from
              the list of new bad blocks produced on the standard output or in the output file.  The -b option of dumpe2fs(8) can be used  to
              retrieve the list of blocks currently marked bad on an existing filesystem, in a format suitable for use with this option.

       -n     Use  non-destructive  read-write mode.  By default only a non-destructive read-only test is done.  This option must not be com‐
              bined with the -w option, as they are mutually exclusive.

       -o output_file
              Write the list of bad blocks to the specified file.  Without this option, badblocks displays the list on its  standard  output.
              The format of this file is suitable for use by the -l option in e2fsck(8) or mke2fs(8).

       -p num_passes
              Repeat  scanning  the disk until there are no new blocks discovered in num_passes consecutive scans of the disk.  Default is 0,
              meaning badblocks will exit after the first pass.

       -s     Show the progress of the scan by writing out rough percentage completion of the current badblocks pass  over  the  disk.   Note
              that badblocks may do multiple test passes over the disk, in particular if the -p or -w option is requested by the user.

       -t test_pattern
              Specify  a test pattern to be read (and written) to disk blocks.   The test_pattern may either be a numeric value between 0 and
              ULONG_MAX-1 inclusive, or the word "random", which specifies that the block should be filled with a random  bit  pattern.   For
              read/write (-w) and non-destructive (-n) modes, one or more test patterns may be specified by specifying the -t option for each
              test pattern desired.  For read-only mode only a single pattern may be specified and it may not be "random".  Read-only testing
              with  a  pattern  assumes  that the specified pattern has previously been written to the disk - if not, large numbers of blocks
              will fail verification.  If multiple patterns are specified then all blocks will be tested with one pattern  before  proceeding
              to the next pattern.

       -v     Verbose mode.  Will write the number of read errors, write errors and data- corruptions to stderr.

       -w     Use  write-mode  test.  With  this  option, badblocks scans for bad blocks by writing some patterns (0xaa, 0x55, 0xff, 0x00) on
              every block of the device, reading every block and comparing the contents.  This option may not be combined with the -n option,
              as they are mutually exclusive.

       -B     Use buffered I/O and do not use Direct I/O, even if it is available.

       -X     Internal flag only to be used by e2fsck(8) and mke2fs(8).  It bypasses the exclusive mode in-use device safety check.


```

### 参数  

*   磁盘装置：指定要检查的磁盘装置；
*   磁盘区块数：指定磁盘装置的区块总数；
*   启始区块：指定要从哪个区块开始检查。

### 实例  

badblocks以4096的一个block，每一个block检查16次，将结果输出到“hda-badblocks-list”文件里。

```
badblocks -b 4096 -c 16 /dev/hda1 -o hda-badblocks-list
```

hda-badblocks-list是个文本文件，内容如下：

```
cat hda-badblocks-list
51249
51250
51251
51253
51254
……
61245
……
```

可以针对可疑的区块多做几次操作。下面，badblocks以4096字节为一个“block”,每一个“block”检查1次, 将结果输出到“hda-badblocks-list.1”文件中，由第51000 block开始，到63000 block结束。

```
badblocks -b 4096 -c 1 /dev/hda1 -o hda-badblocks-list.1 63000 51000
```

这次花费的时间比较短，硬盘在指定的情况下在很短的时间就产生“嘎嘎嘎嘎”的响声。由于检查条件的不同，其输出的结果也不完全是相同的。重复几次同样的操作，因条件多少都有些不同，所以结果也有所不同。进行多次操作后，直到产生最后的hda-badblock-list.final文件。

### 其他  

 **1、fsck使用badblocks的信息** 

badblocks只会在日志文件中标记出坏道的信息，但若希望在检测磁盘时也能跳过这些坏块不检测，可以使用fsck的-l参数：

```
fsck.ext3 -l /tmp/hda-badblock-list.final /dev/hda1
```

 **2、在创建文件系统前检测坏道** 

badblocks可以随e2fsck和mke2fs的-c删除一起运行（对ext3文件系统也一样），在创建文件系统前就先检测坏道信息：

```
mkfs.ext3 -c /dev/hda1
```

代码表示使用-c在创建文件系统前检查坏道的硬盘。

这个操作已经很清楚地告知我们可以采用`mkfs.ext3 -c`选项用`read-only`方式检查硬盘。这个命令会在格式化硬盘时检查硬盘，并标出错误的硬盘“block”。用这个方法格式化硬盘，需要有相当大的耐心，因为命令运行后，会一个个用读的方式检查硬盘。


