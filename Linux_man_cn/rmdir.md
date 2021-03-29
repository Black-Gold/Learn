# **rmdir**

## 说明

**rmdir命令** 删除指定的`空目录`。rmdir命令可以从一个目录中删除一个或多个空的子目录。删除目录时，必须具有对其父目录的写权限

注意：子目录被删除之前应该是空目录。就是说，该目录中的所有文件必须用rm命令全部，另外，当前工作目录必须在被删除目录之上，不能是被删除目录
本身，也不能是被删除目录的子目录

```markdown
    --ignore-fail-on-non-empty  忽略仅由目录非空产生的所有错误
-p, --parents   删除目录，若该目录删除后上层目录变为空目录一并删除; 例如：'rmdir -p a/b/c' 和 'rmdir a/b/c a/b a'相同
-v, --verbose   output a diagnostic for every directory processed

```

## 实例

```bash
rmdir -p bin/os_1   # 删除子目录os_1,若bin目录为空，则删除，否则保留

```
