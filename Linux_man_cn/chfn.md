# chfn

## 说明

**chfn命令** 用来改变finger命令显示的信息。这些信息都存放在/etc目录里的passwd文件里。若不指定任何选项，则chfn命令会进入问答式界面

## 选项

```markdown
-f, --full-name <全名>        设置真实姓名
-o, --office <办公>           设置办公号码
-p, --office-phone <电话>     设置办公电话
-h, --home-phone <电话>       设置住宅电话

```

## 实例

```bash
chfn    # 改变finger信息;按照提示输入即可
chfn -f jack    # 改变账号真实姓名
Changing finger information for root.

```


