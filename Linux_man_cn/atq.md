atq
===

列出当前用户的at任务列表

## 说明

**atq命令** 显示系统中待执行的任务列表，也就是列出当前用户的at任务列表

## 选项

```
atq(选项)
```

  

```
-V：显示版本号
-q：查询指定队列的任务
```

## 实例

```
at now + 10 minutes
at> echo 1111
at> <eot>
job 3 at Fri Apr 26 12:56:00 2013

atq
3       Fri Apr 26 12:56:00 2013 a root
```


