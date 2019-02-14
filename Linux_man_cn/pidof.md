# **pidof**

## 补充说明

**pidof命令** 用于查找指定名称的进程的进程号id号。

## 选项  

```sh
-s：仅返回一个进程pid号；
-c：仅显示具有相同“root”目录的进程；
-x：显示由脚本开启的进程；
-o：指定不显示的进程ID。
```

## 实例  

```sh
pidof nginx
13312 5371

pidof crond
1509

pidof init
1
```
