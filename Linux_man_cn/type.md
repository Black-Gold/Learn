# **type**

## 说明

**type命令** 用来显示指定命令的类型，判断给出的指令是内部指令还是外部指令

命令类型：

* alias：别名
* keyword：关键字，Shell保留字
* function：函数，Shell函数
* builtin：内建命令，Shell内建命令
* file：文件，磁盘文件，外部命令
* unfound：没有找到

## 选项

```markdown
-t：输出“file”、“alias”或者“builtin”，分别表示给定的指令为“外部指令”、“命令别名”或者“内部指令”
-p：如果给出的指令为外部指令，则显示其绝对路径
-a：在环境变量“PATH”指定的路径中，显示给定指令的信息，包括命令别名
```

## 实例

```bash
type ls
type -a cd
type -a grep
```
