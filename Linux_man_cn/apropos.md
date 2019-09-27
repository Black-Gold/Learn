# apropos

## 说明

**apropos命令** 在一些特定的包含系统命令的简短描述的数据库文件里查找关键字，然后把结果送到标准输出。 

如果你不知道完成某个特定任务所需要命令的名称，可以使用一个关键字通过Linux apropos实用程序来搜索它。该实用程序可以搜索关键字并且显示所有包含匹配项的man页面的简短描述。另外，使用man实用程序和-k（关键字）选项，可以得到和用Linux apropos实用程序相同的结果（实际上是相同的命令）



```info
-d, --debug                           输出调试信息
-v, --verbose                         输出详细的警告信息
-e, --exact                           对每个关键词都进行严格匹配的搜索
-r, --regex                           把每个关键词都当作正则表达式解读,默认开启 --regex 选项
-w, --wildcard                        关键词里包含通配符
-a, --and                             要求所有的关键词都同时匹配
-l, --long                            不要把输出按终端宽度截断
-C, --config-file=文件                使用该用户设置文件
-L, --locale=区域                     定义本次搜索所使用的区域设置
-m, --systems=系统                    use manual pages from other systems
-M, --manpath=路径                    设置搜索手册页的路径为“路径”,默认使用$MANPATH环境变量
-s, --sections=列表, --section=列表   只查找指定的手册section

返回值:返回0表示成功，1表示用法、语法或配置文件错误，2表示操作错误，16表示没有找到匹配的内容
```

## 实例

```sh
apropos -a emacs vi     # 查找手册页名字和描述中包含emacs和vi的手册页
apropos whatis          # 显示和whatis相关的命令
```