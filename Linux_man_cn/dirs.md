# dirs

## 说明

**dirs命令** 显示当前目录栈中的所有记录（不带参数的dirs命令显示当前目录栈中的记录）。dirs始终显示当然目录, 再是堆栈中的内容；
即使目录堆栈为空, dirs命令仍然只显示当然目录，使用pushd命令将目录添加到列表中；该 popd命令从列表中删除目录，当前目录始终是堆栈中的第一个目录

```markdown
-c  删除目录栈中的所有记录
-l  以完整格式显示；默认列表格式使用波浪号表示主目录
-p  一个目录一行的方式显示
-v  每行一个目录来显示目录栈的内容，每个目录前加上索引
+N  显示从左到右的第n个目录，数字从0开始
-N  显示从右到左的第n个日录，数字从0开始

```

## 实例

```bash
dirs
```
