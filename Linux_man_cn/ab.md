# **ab**

## 说明

**ab命令** 是Apache的Web服务器的性能测试工具，它可以测试安装Web服务器每秒种处理的HTTP请求

### 选项

```markdown
-n requests     指定测试会话的请求数量
-c concurrency  一次进行多少个并发请求
-t timelimit    Seconds to max. to spend on benchmarking,This implies -n 50000
-s timeout      Seconds to max. wait for each response,Default is 30 seconds
-b windowsize   Size of TCP send/receive buffer, in bytes
-B address      Address to bind to when making outgoing connections
-p postfile     File containing data to POST. Remember also to set -T
-u putfile      File containing data to PUT. Remember also to set -T
-T content-type 用于POST/PUT数据的Content-type header,例如：'application/x-www-form-urlencoded',默认是：'text/plain'
-v verbosity    How much troubleshooting info to print
-w              以HTML表格方式打印结果
-i              Use HEAD instead of GET
-x attributes   String to insert as table attributes
-y attributes   String to insert as tr attributes
-z attributes   String to insert as td or th attributes
-C attribute    Add cookie,例如：'Apache=1234'. (repeatable)
-H attribute    为请求添加一个额外的header,例如：'Accept-Encoding: gzip'
                Inserted after all normal header lines. (repeatable)
-A attribute    添加基本的WWW身份验证，attribute是用冒号分隔的用户名和密码
-P attribute    添加基本代理身份验证，attribute是用冒号分隔的用户名和密码
-X proxy:port   Proxyserver and port number to use
-V              Print version number and exit
-k              使用HTTP KeepAlive特性
-d              Do not show percentiles served table
-S              Do not show confidence estimators and warnings
-q              超过150个请求时不显示进度
-g filename     将收集的结果输出为gnuplot格式文件
-e filename     Output CSV file with percentages served
-r              Don't exit on socket receive errors
-Z ciphersuite  Specify SSL/TLS cipher suite (See openssl ciphers)
-f protocol     指定SSL/TLS协议(SSL3, TLS1, TLS1.1, TLS1.2 or ALL)

```

