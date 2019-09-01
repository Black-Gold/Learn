# **uniq**

## 说明

**uniq命令** 用于报告或忽略文件中的重复行，一般与sort命令结合使用

## 选项

```markdown
用法：uniq [选项]... [文件]
Filter adjacent matching lines from INPUT (or standard input),
writing to OUTPUT (or standard output).

With no options, matching lines are merged to the first occurrence.

Mandatory arguments to long options are mandatory for short options too.
-c, --count                     在每列旁边显示该行重复出现的次数
-d, --repeated                  仅显示重复出现的行列
-D, --all-repeated[=METHOD]     显示所有的重复行print all duplicate lines groups can be delimited with an empty line
                        METHOD={none(default),prepend,separate}
-f, --skip-fields=N             avoid comparing the first N fields
    --group[=METHOD]    show all items, separating groups with an empty line
                        METHOD={separate(default),prepend,append,both}
-i, --ignore-case               ignore differences in case when comparing
-s, --skip-chars=N              忽略比较指定的字符
-u, --unique                    仅显示出一次的行列
-z, --zero-terminated           end lines with 0 byte, not newline
-w, --check-chars=N	            对每行第N 个字符以后的内容不作对照;即指定要比较的字符

若域中为先空字符(通常包括空格以及制表符)，然后非空字符，域中字符前的空字符将被跳过

```

## 实例

```bash
# 删除重复行
uniq file.txt
sort file.txt | uniq
sort -u file.txt

sort file.txt | uniq -c     # 统计各行在文件中出现的次数
sort file.txt | uniq -d     # 在文件中找出重复的行

```
