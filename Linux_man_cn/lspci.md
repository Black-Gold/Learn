# lspci

## 说明

**lspci命令** 用于显示当前主机的所有PCI总线信息，以及所有已连接的PCI设备信息。

## 选项

```markdown
-n：以数字方式显示PCI厂商和设备代码；
-t：以树状结构显示PCI设备的层次关系，包括所有的总线、桥、设备以及它们之间的联接；
-b：以总线为中心的视图；
-d：仅显示给定厂商和设备的信息；
-s：仅显示指定总线、插槽上的设备和设备上的功能块信息；
-i：指定PCI编号列表文件，而不使用默认的文件；
-m：以机器可读方式显示PCI设备信息。

Usage: lspci [<switches>]

Basic display modes:
-mm		Produce machine-readable output (single -m for an obsolete format)
-t		Show bus tree

Display options:
-v		Be verbose (-vv for very verbose)
-k		Show kernel drivers handling each device
-x		Show hex-dump of the standard part of the config space
-xxx		Show hex-dump of the whole config space (dangerous; root only)
-xxxx		Show hex-dump of the 4096-byte extended config space (root only)
-b		Bus-centric view (addresses and IRQ's as seen by the bus)
-D		Always show domain numbers

Resolving of device ID's to names:
-n		Show numeric ID's
-nn		Show both textual and numeric ID's (names & numbers)
-q		Query the PCI ID database for unknown ID's via DNS
-qq		As above, but re-query locally cached entries
-Q		Query the PCI ID database for all ID's via DNS

Selection of devices:
-s [[[[<domain>]:]<bus>]:][<slot>][.[<func>]]	Show only devices in selected slots
-d [<vendor>]:[<device>][:<class>]		Show only devices with specified ID's

Other options:
-i <file>	Use specified ID database instead of /usr/share/hwdata/pci.ids
-p <file>	Look up kernel modules in a given file instead of default modules.pcimap
-M		Enable `bus mapping' mode (dangerous; root only)

PCI access options:
-A <method>	Use the specified PCI access method (see `-A help' for a list)
-O <par>=<val>	Set PCI access parameter (see `-O help' for a list)
-G		Enable PCI access debugging
-H <mode>	Use direct hardware access (<mode> = 1 or 2)
-F <file>	Read PCI configuration dump from a given file


```

## 实例

```bash
lspci -tv   # 显示PCI信息

```


