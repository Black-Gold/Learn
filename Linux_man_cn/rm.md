# **rm**

## 说明

**rm**  可以删除一个目录中的一个或多个文件或目录，也可以将某个目录及其下属的所有文件及其子目录均删除掉。对于链接文件，只
是删除整个链接文件，而原有文件保持不变

注意：使用rm命令要格外小心。因为一旦删除了一个文件，就无法再恢复它。所以，在删除文件之前，最好再看一下文件的内容，确定是
否真要删除。rm命令可以用-i选项，这个选项在使用文件扩展名字符删除多个文件时特别有用。使用这个选项，系统会要求你逐一确定是
否要删除。这时，必须输入y并按Enter键，才能删除文件。如果仅按Enter键或其他字符，文件不会被删除

## 选项

```markdown

  -f, --force           忽略不存在的文件和参数，不提示直接强制删除
  -i                    删除已有文件或目录之前先询问用户
  -I                    prompt once before removing more than three files, or
                          when removing recursively; less intrusive than -i,
                          while still giving protection against most mistakes
      --interactive[=WHEN]  prompt according to WHEN: never, once (-I), or
                          always (-i); without WHEN, prompt always
      --one-file-system         递归删除一个层级时，跳过所有不符合命令行参
                                数的文件系统上的文件
      --no-preserve-root  do not treat '/' specially
      --preserve-root   do not remove '/' (default)
  -r, -R, --recursive   remove directories and their contents recursively
  -d, --dir             移除空目录
  -v, --verbose         显示指令的详细执行过程
      --help            显示此帮助信息并退出
      --version         显示版本信息并退出

默认时，rm 不会删除目录。使用--recursive(-r 或-R)选项可删除每个给定
的目录，以及其下所有的内容。

To remove a file whose name starts with a '-', for example '-foo',
use one of these commands:
  rm -- -foo

  rm ./-foo

请注意，如果使用rm 来删除文件，通常仍可以将该文件恢复原状。如果想保证
该文件的内容无法还原，请考虑使用shred。
```

## 实例

```bash
rm -i test example  # 交互式删除当前目录下的文件test和example
```
