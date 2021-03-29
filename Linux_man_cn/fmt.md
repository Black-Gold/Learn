# fmt

## 说明

**fmt命令** 读取文件的内容，根据选项的设置对文件格式进行简单的优化处理，并将结果送到标准输出设备

```markdown
-c --crown-margin           保持前两行的缩进
-p, --prefix=字符串          只对以指定字符串开头的行重新格式化，将前缀重新附着到被重新格式化的行上
-s, --split-only            分割过长的行，但不自动补足
-t, --tagged-paragraph    indentation of first line different from second
-u, --uniform-spacing     one space between words, two after sentences
-w, --width=WIDTH         maximum line width (default of 75 columns)
-g, --goal=WIDTH          goal width (default of 93% of width)

```
