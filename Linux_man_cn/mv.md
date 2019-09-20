# **mv**

## 说明

**mv命令** 用来对文件或目录重新命名，或者将文件从一个目录移到另一个目录中。source表示源文件或目录，target表示目标文件或
目录。如果将一个文件移到一个已经存在的目标文件中，则目标文件的内容将被覆盖

mv命令可以用来将源文件移至一个目标文件中，或将一组文件移至一个目标目录中。源文件被移至目标文件有两种不同的结果：

1.  如果目标文件是到某一目录文件的路径，源文件会被移到此目录下，且文件名不变。
2.  如果目标文件不是目录文件，则源文件名（只能有一个）会变为此目标文件名，并覆盖己存在的同名文件。如果源文件和目标文件在
同一个目录下，mv的作用就是改文件名。当目标文件是目录文件时，源文件或目录参数可以有多个，则所有的源文件都会被移至目标文件
中。所有移到该目录下的文件都将保留以前的文件名

注意事项：mv与cp的结果不同，mv好像文件"搬家"，文件个数并未增加。而cp对文件进行复制，文件个数增加了

## 选项

```markdown
用法：mv [选项]... [-T] 源文件 目标文件
　或：mv [选项]... 源文件... 目录
　或：mv [选项]... -t 目录 源文件...
Rename SOURCE to DEST, or move SOURCE(s) to DIRECTORY.
  --backup[=CONTROL]            为每个已存在的目标文件创建备份
  -b                                类似--backup 但不接受参数,当文件存在时，覆盖前，为其创建一个备份
  -f, --force                       覆盖前不询问
  -i, --interactive                 覆盖前询问
  -n, --no-clobber                  不覆盖已存在文件,如果您指定了-i、-f、-n 中的多个，仅最后一个生效
      --strip-trailing-slashes      去掉每个源文件参数尾部的斜线
  -S, --suffix=SUFFIX               替换常用的备份文件后缀
  -t, --target-directory=DIRECTORY  移动所有源文件参数到目录
  -T, --no-target-directory         treat DEST as a normal file
  -u, --update                      当源文件比目标文件新或者目标文件不存在时，才执行移动操作
  -v, --verbose                     explain what is being done
  -Z, --context                     set SELinux security context of destination file to default type

The backup suffix is '~', unless set with --suffix or SIMPLE_BACKUP_SUFFIX.
The version control method may be selected via the --backup option or through
the VERSION_CONTROL environment variable.  Here are the values:
  none, off       不进行备份(即使使用了--backup 选项)
  numbered, t     备份文件加上数字进行排序
  existing, nil   若有数字的备份文件已经存在则使用数字，否则使用普通方式备份
  simple, never   永远使用普通方式备份
```

## 实例

```bash
mv --
```



