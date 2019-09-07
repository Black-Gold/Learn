# **uname**

## 说明

**uname命令** 用于打印当前系统相关信息（内核版本号、硬件架构、主机名称和操作系统类型等）

## 选项

```markdown
用法：uname [选项]
输出一组系统信息。如果不跟随选项，则视为只附加-s 选项
-a, --all			        以如下次序输出所有信息。其中若-p 和-i 的探测结果不可知则被省略
-s, --kernel-name		    输出内核名称
-n, --nodename		        输出网络节点上的主机名
-r, --kernel-release        输出内核发行号
-v, --kernel-version	    输出内核版本
-m, --machine		        输出主机的硬件架构名称
-p, --processor		        输出处理器类型或"unknown"
-i, --hardware-platform	    输出硬件平台或"unknown"
-o, --operating-system	    输出操作系统名称

```

## 实例

```bash
uname -a    # 查询内核/操作系统/CPU信息
```
