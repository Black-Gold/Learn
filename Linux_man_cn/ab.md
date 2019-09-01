# **ab**

## 说明

**ab命令** 是Apache的Web服务器的性能测试工具，它可以测试安装Web服务器每秒种处理的HTTP请求

### 选项

```markdown
-A：指定连接服务器的基本的认证凭据
-c：指定一次向服务器发出请求数
-C：添加cookie
-g：将测试结果输出为“gnuolot”文件
-H：为请求追加一个额外的头
-i：使用“head”请求方式
-k：激活HTTP中的“keepAlive”特性
-n：指定测试会话使用的请求数
-p：指定包含数据的文件
-q：不显示进度百分比
-T：使用POST数据时，设置内容类型头
-v：设置详细模式等级
-w：以HTML表格方式打印结果
-x：以表格方式输出时，设置表格的属性
-X：使用指定的代理服务器发送请求
-y：以表格方式输出时，设置表格属性
```

用法: ab [选项] [http[s]://]hostname[:port]/path
选项:
    -n requests     执行请求的数量
    -c concurrency  一次进行多少个并发请求
    -t timelimit    Seconds to max. to spend on benchmarking
                    This implies -n 50000
    -s timeout      Seconds to max. wait for each response
                    Default is 30 seconds
    -b windowsize   Size of TCP send/receive buffer, in bytes
    -B address      Address to bind to when making outgoing connections
    -p postfile     File containing data to POST. Remember also to set -T
    -u putfile      File containing data to PUT. Remember also to set -T
    -T content-type Content-type header to use for POST/PUT data, eg.
                    'application/x-www-form-urlencoded'
                    Default is 'text/plain'
    -v verbosity    How much troubleshooting info to print
    -w              Print out results in HTML tables
    -i              Use HEAD instead of GET
    -x attributes   String to insert as table attributes
    -y attributes   String to insert as tr attributes
    -z attributes   String to insert as td or th attributes
    -C attribute    Add cookie, eg. 'Apache=1234'. (repeatable)
    -H attribute    Add Arbitrary header line, eg. 'Accept-Encoding: gzip'
                    Inserted after all normal header lines. (repeatable)
    -A attribute    Add Basic WWW Authentication, the attributes
                    are a colon separated username and password.
    -P attribute    Add Basic Proxy Authentication, the attributes
                    are a colon separated username and password.
    -X proxy:port   Proxyserver and port number to use
    -V              Print version number and exit
    -k              Use HTTP KeepAlive feature
    -d              Do not show percentiles served table.
    -S              Do not show confidence estimators and warnings.
    -q              Do not show progress when doing more than 150 requests
    -g filename     Output collected data to gnuplot format file.
    -e filename     Output CSV file with percentages served
    -r              Don't exit on socket receive errors.
    -h              Display usage information (this message)
    -Z ciphersuite  Specify SSL/TLS cipher suite (See openssl ciphers)
    -f protocol     Specify SSL/TLS protocol
                    (SSL3, TLS1, TLS1.1, TLS1.2 or ALL)


