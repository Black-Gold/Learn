# sum

## 说明

**sum命令** 用于计算并显示指定文件的校验和与文件所占用的磁盘块数

```markdown
-r：使用BSD的校验和算法，块大小为1k
-s：使用system V的校验和算法，块大小为512字节
```

## 实例

```bash
sum insert.sql  # 计算文件校验码
```
