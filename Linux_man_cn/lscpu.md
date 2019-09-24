# lscpu

## 说明

**lscpu命令** 是显示有关CPU架构的信息

## 选项

```markdown
-a, --all               同时打印在线和离线 CPU (-e 选项默认值)
-b, --online            只打印在线 CPU (-p 选项默认值)
-c, --offline           只打印离线 CPU
-e, --extended[=<列表>] 打印扩展的可读格式
-p, --parse[=<列表>]    打印可解析格式
-s, --sysroot <目录>    以指定目录作为系统根目录
-x, --hex               打印十六进制掩码而非 CPU 列表
-y, --physical          print physical instead of logical IDs

可用的列：
           CPU  逻辑 CPU 数量
          CORE  逻辑核心数量
        SOCKET  逻辑(CPU)座数量
          NODE  逻辑 NUMA 节点数量
          BOOK  逻辑 book 数
        DRAWER  logical drawer number
         CACHE  shows how caches are shared between CPUs
  POLARIZATION  CPU dispatching mode on virtual hardware
       ADDRESS  physical address of a CPU
    CONFIGURED  shows if the hypervisor has allocated the CPU
        ONLINE  shows if Linux currently makes use of the CPU
        MAXMHZ  shows the maximum MHz of the CPU
        MINMHZ  shows the minimum MHz of the CPU

```

## 实例

```bash
lscpu

```


