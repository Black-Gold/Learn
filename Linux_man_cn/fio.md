# **fio**

linux和Windows都推荐使用FIO工具进行测试块存储性能，测试前确保已经4k对齐，测试裸盘可以获取真实块存储盘性能。但是会破坏文件系统结构

```bash
fio [options] [job options] <job file(s)>
  --debug=options	Enable debug logging. May be one/more of:
			process,file,io,mem,blktrace,verify,random,parse,
			diskutil,job,mutex,profile,time,net,rate,compress,
			steadystate,helperthread
  --parse-only		Parse options only, don't start any IO
  --output		Write output to file
  --bandwidth-log	Generate aggregate bandwidth logs
  --minimal		Minimal (terse) output
  --output-format=type	Output format (terse,json,json+,normal)
  --terse-version=type	Set terse version output format (default 3, or 2 or 4)
  --cpuclock-test	Perform test/validation of CPU clock
  --crctest=[type]	Test speed of checksum functions
  --cmdhelp=cmd		Print command help, "all" for all of them
  --enghelp=engine	Print ioengine help, or list available ioengines
  --enghelp=engine,cmd	Print help for an ioengine cmd
  --showcmd		Turn a job file into command line options
  --eta=when		When ETA estimate should be printed
            		May be "always", "never" or "auto"
  --eta-newline=time	Force a new line for every 'time' period passed
  --status-interval=t	Force full status dump every 't' period passed
  --readonly		Turn on safety read-only checks, preventing writes
  --section=name	Only run specified section in job file, multiple sections can be specified
  --alloc-size=kb	Set smalloc pool to this size in kb (def 16384)
  --warnings-fatal	Fio parser warnings are fatal
  --max-jobs=nr		Maximum number of threads/processes to support
  --server=args		Start a backend fio server
  --daemonize=pidfile	Background fio server, write pid to file
  --client=hostname	Talk to remote backend(s) fio server at hostname
  --remote-config=file	Tell fio server to load this local job file
  --idle-prof=option	Report cpu idleness on a system or percpu basis
			(option=system,percpu) or run unit work
			calibration only (option=calibrate)
  --inflate-log=log	Inflate and output compressed log
  --trigger-file=file	Execute trigger cmd when file exists
  --trigger-timeout=t	Execute trigger at this time
  --trigger=cmd		Set this command as local trigger
  --trigger-remote=cmd	Set this command as remote trigger
  --aux-path=path	Use this path for fio state generated files
```

命令参数含义

| 参数 | 说明 |
| :------: | :------: |
| -direct=1 | 表示测试时忽略I/O缓存，数据直写。 |
| -iodepth=128 | 表示使用AIO时，同时发出I/O数的上限为128。 |
| -rw=randwrite | 表示测试时的读写策略为随机写（random writes）。作其它测试时可以设置为：randread（随机读random reads）、read（顺序读sequential reads）、write（顺序写sequential writes）、randrw（混合随机读写mixed random reads and writes） |
| -ioengine=libaio | 表示测试方式为libaio（Linux AIO，异步I/O）。应用程序使用I/O通常有两种方式：一：同步-->>同步的I/O一次只能发出一个I/O请求，等待内核完成才返回。这样对于单个线程iodepth总是小于1，但是可以透过多个线程并发执行来解决。通常会用16−32根线程同时工作将iodepth塞满。二：异步-->>异步的I/O通常使用libaio这样的方式一次提交一批I/O请求，然后等待一批的完成，减少交互的次数，会更有效率 |
| -bs=4k | 表示单次I/O的块文件大小为4 KB。未指定该参数时的默认大小也是4 KB。测试IOPS时，建议将bs设置为一个比较小的值，如本示例中的4k。测试吞吐量时，建议将bs设置为一个较大的值，如本示例中的1024k |
| -size=1G | 表示测试文件大小为1 GiB |
| -numjobs=1 | 表示测试线程数为1 |
| -runtime=1000 | 表示测试时间为1000秒。如果未配置，则持续将前述-size指定大小的文件，以每次-bs值为分块大小写完 |
| -group_reporting | 表示测试结果里汇总每个进程的统计信息，而非以不同job汇总展示信息 |
| -filename=iotest | 指定测试文件的名称，比如iotest。测试裸盘可以获得真实的硬盘性能，但直接测试裸盘会破坏文件系统结构，请在测试前提前做好数据备份 |
| -name=Rand_Write_Testing | 表示测试任务名称为Rand_Write_Testing，可以随意设定 |

```bash
fio -direct=1 -iodepth=128 -rw=randwrite -ioengine=libaio -bs=4k -size=1G -numjobs=1 -runtime=1000 -group_reporting -filename=iotest -name=Rand_Write_Testing   # 测试随机写IOPS
fio -direct=1 -iodepth=128 -rw=randread -ioengine=libaio -bs=4k -size=1G -numjobs=1 -runtime=1000 -group_reporting -filename=iotest -name=Rand_Read_Testing     # 测试随机读IOPS
fio -direct=1 -iodepth=64 -rw=write -ioengine=libaio -bs=1024k -size=1G -numjobs=1 -runtime=1000 -group_reporting -filename=iotest -name=Write_PPS_Testing      # 测试顺序写吞吐量
fio -direct=1 -iodepth=64 -rw=read -ioengine=libaio -bs=1024k -size=1G -numjobs=1 -runtime=1000 -group_reporting -filename=iotest -name=Read_PPS_Testing        # 测试顺序读吞吐量
fio -direct=1 -iodepth=1 -rw=randwrite -ioengine=libaio -bs=4k -size=1G -numjobs=1 -group_reporting -filename=iotest -name=Rand_Write_Latency_Testing           # 测试随机写延时
fio -direct=1 -iodepth=1 -rwfio -direct=1 -iodepth=1 -rw=randread -ioengine=libaio -bs=4k -size=1G -numjobs=1 -group_reporting -filename=iotest -name=Rand_Read_Latency_Testingrandwrite -ioengine=libaio -bs=4k -size=1G -numjobs=1 -group_reporting -filename=iotest -name=Rand_Write_Latency_Testing         # 测试随机读延时

```
