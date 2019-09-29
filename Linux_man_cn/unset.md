# **unset**

## 说明

**unset命令** 用于删除已定义的shell变量（包括环境变量）和shell函数。unset命令不能够删除具有只读属性的shell变量和环境变量

## 选项

```markdown
-f：仅删除函数
-v：仅删除变量
```

## 实例

```bash
unset -v mylove # 使用unset命令将前面所创建的环境变量mylove及其对应的值进行删除
```

