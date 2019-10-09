# mktemp

## 说明

**mktemp命令** 被用来创建临时文件供shell脚本使用

## 选项

```markdown
-d, --directory     创建一个目录而非文件
-u, --dry-run       不创建任何东西，仅打印出名字。(仅供测试)
-q, --quiet         不显示任何有关文件或目录创建错误信息
    --suffix=SUFF   将STUFF附加到TEMPLATE; SUFF不能包含斜线。如果TEMPLATE不以X结尾，则使用此选项
  -p DIR, --tmpdir[=DIR]  interpret TEMPLATE relative to DIR; if DIR is not specified, use $TMPDIR if set, else /tmp.
                          With this option, TEMPLATE must not be an absolute name;unlike with -t, TEMPLATE may contain
                          slashes, but mktemp creates only the final component

```


