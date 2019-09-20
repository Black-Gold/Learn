# **wget**

## 说明

**wget命令** 用来从指定的URL下载文件。wget非常稳定，它在带宽很窄的情况下和不稳定网络中有很强的适应性，如果是由于网络的原
因下载失败，wget会不断的尝试，直到整个文件下载完毕。如果是服务器打断下载过程，它会再次联到服务器上从停止的地方继续下载。
这对从那些限定了链接时间的服务器上下载大文件非常有用

[wget官网](http://www.gnu.org/software/wget/)

wget支持HTTP，HTTPS和FTP协议，可以使用HTTP代理。所谓的自动下载是指，wget可以在用户退出系统的之后在后台执行。这意味这你可
以登录系统，启动一个wget下载任务，然后退出系统，wget将在后台执行直到任务完成，相对于其它大部分浏览器在下载大量数据时需要
用户一直的参与，这省去了极大的麻烦

用于从网络上下载资源，没有指定目录，下载资源回默认为当前目录。wget虽然功能强大，但是使用起来还是比较简单：

1. **支持断点下传功能**
2. **同时支持FTP和HTTP下载方式**
3. **支持代理服务器**
4. **设置方便简单**
5. **程序小，完全免费**

## 选项

wget [选项]... [URL]...

```markdown
长选项所必须的参数在使用短选项时也是必须的

启动：
-b,--background 启动后转入后台执行
-e,--execute=COMMAND 执行”.wgetrc“格式的命令，wgetrc格式参见/etc/wgetrc或~/.wgetrc

日志和输入文件：
-o,--output-file=FILE 把记录写到FILE文件中
-a,--append-output=FILE 把记录追加到FILE文件中
-d,--debug 打印调试输出
-q,--quiet 安静模式(没有输出)
-v,--verbose 详尽模式(这是缺省设置)
-nv,--non-verbose 关掉冗长模式，但不进入安静模式
    --report-speed=类型 以类型报告带宽，类型可以是bits
-i,--input-file=FILE 下载本地或外部文件中的 URL
-F,--force-html 把输入文件当作HTML格式文件对待
-B,--base=URL 将URL作为在-F -i参数指定的文件中出现的相对链接的前缀
   --config=文件 指定要使用的配置文件
   --no-cookies 不读取任何配置文件
   --rejected-log=文件 将拒绝URL的原因写入文件

下载：
--bind-address=ADDRESS 指定本地使用地址(主机名或IP，当本地有多个IP或名字时使用)
-t,--tries=NUMBER 设定最大尝试链接次数(0 表示无限制)
  --retry-connrefused 即使拒绝连接也是重试
-O，--output-document=FILE 把文档写到FILE文件中
-nc,--no-clobber 不要覆盖存在的文件或使用.#前缀
    --no-netrc 不要尝试从.netrc获取凭据
-c,--continue 断点续传文件
   --start-pos=偏移量 从由零计数的偏移量开始下载
   --progress=类型 选择进度条类型
   --show-progress 在任意状态下都显示进度条
-N,--timestamping 只下载比本地文件新的文件
   --no-if-modified-since 不要在时间戳(timestamping)模式下使用if-modified-since get 条件请求
   --no-use-server-timestamps 不用服务器上的时间戳来设置本地文件
-S,--server-response 打印服务器的响应
   --spider 不下载任何东西
-T,--timeout=SECONDS           将所有超时设为 SECONDS
   --dns-timeout=SECS          设置 DNS 查寻超时为 SE
   --connect-timeout=SECS      设置连接超时为 SECS 秒
   --read-timeout=SECS         设置读取超时为 SECS 秒
-w,--wait=SECONDS              等待间隔为 SECONDS 秒
   --waitretry=SECONDS         在获取文件的重试期间等待 1..SECO
   --random-wait               获取多个文件时，每次随机等待间隔
(0.5~1.5)*WAIT 秒
   --no-proxy                  禁止使用代理
-Q,--quota=数字                设置获取配额为 <数字> 字节
   --bind-address=ADDRESS      绑定至本地主机上的 ADDRESS (主机
IP)
   --limit-rate=RATE           限制下载速率为 RATE
   --no-dns-cache              关闭 DNS 查询缓存
   --restrict-file-names=系统  限定文件名中的字符为 <系统> 允许
   --ignore-case               匹配文件/目录时忽略大小写
-4,--inet4-only                仅连接至 IPv4 地址
-6,--inet6-only                仅连接至 IPv6 地址
   --prefer-family=地址族      首先连接至指定家族（IPv6，IPv4
的地址
   --user=用户                 将 ftp 和 http 的用户名均设置为
   --password=密码             将 ftp 和 http 的密码均设置为 <
   --ask-password              提示输入密码
   --use-askpass=命令          指定用于请求用户名和密码的凭据管
                                 如果没有提供指定命令，程序将使
WGET_ASKPASS 或
                                 SSH_ASKPASS 环境变量。
   --no-iri                    关闭 IRI 支持
   --local-encoding=ENC        使用 ENC 作为 IRI (国际化资源标
本地编码
   --remote-encoding=ENC       使用 ENC 作为默认远程编码
   --unlink                    覆盖前移除文件
   --no-xattr                  不要在文件的拓展属性中储存元数据

目录：
-nd,--no-directories            不创建目录
-x, --force-directories         强制创建目录
-nH,--no-host-directories       不要创建主 (host) 目录
    --protocol-directories      在目录中使用协议名称
-P, --directory-prefix=前缀     保存文件到 <前缀>/..
    --cut-dirs=数字             忽略远程目录中 <数字> 个目录层

HTTP 选项：
       --http-user=用户            设置 http 用户名为 <用户>
       --http-password=密码        设置 http 密码为 <密码>
       --no-cache                  不使用服务器缓存的数据。
       --default-page=NAME         改变默认页 (通常是“index.html”)。
  -E,  --adjust-extension          以合适的扩展名保存 HTML/CSS 文档
       --ignore-length             忽略头部的‘Content-Length’区域
       --header=字符串             在头部插入 <字符串>
       --max-redirect              每页所允许的最大重定向
       --proxy-user=用户           使用 <用户> 作为代理用户名
       --proxy-password=密码       使用 <密码> 作为代理密码
       --referer=URL               在 HTTP 请求头包含‘Referer: URL’
       --save-headers              将 HTTP 头保存至文件。
  -U,  --user-agent=代理           标识自己为 <代理> 而不是 Wget/VERSION。
       --no-http-keep-alive        禁用 HTTP keep-alive (持久连接)。
       --no-cookies                不使用 cookies。
       --load-cookies=文件         会话开始前从 <文件> 中载入 cookies。
       --save-cookies=文件         会话结束后保存 cookies 至 FILE。
       --keep-session-cookies      载入并保存会话 (非永久) cookies。
       --post-data=字符串          使用 POST 方式；把 <字串>作为数据发送。
       --post-file=文件            使用 POST 方式；发送 <文件> 内容。
       --method=HTTP方法           在请求中使用指定的 <HTTP 方法>。
       --post-data=字符串          把 <字串> 作为数据发送，必须设置 --method
       --post-file=文件            发送 <文件> 内容，必须设置 --method
       --content-disposition       当选择本地文件名时允许 Content-Disposition
                                   头部 (实验中)。
       --content-on-error          在服务器错误时输出接收到的内容
       --auth-no-challenge         不先等待服务器询问就发送基本 HTTP 验证信息。

HTTPS (SSL/TLS) 选项：
       --secure-protocol=PR        choose secure protocol, one of auto, SSLv2,
                                     SSLv3, TLSv1, TLSv1_1, TLSv1_2 and PFS
       --https-only                 只跟随安全的 HTTPS 链接
       --no-check-certificate       不要验证服务器的证书。
       --certificate=文件           客户端证书文件。
       --certificate-type=类型      客户端证书类型，PEM 或 DER。
       --private-key=文件           私钥文件。
       --private-key-type=类型      私钥文件类型，PEM 或 DER。
       --ca-certificate=文件        带有一组 CA 证书的文件。
       --ca-directory=DIR           保存 CA 证书的哈希列表的目录。
       --ca-certificate=文件        带有一组 CA 证书的文件。
       --pinnedpubkey=文件/散列值  用于验证节点的公钥（PEM/DER）文件或
                                   任何数量的 sha256 散列值，以 base64 编码、
                                   “sha256//” 开头、用“;”间隔
       --random-file=文件           用于初始化 SSL 伪随机数生成器（PRNG）的文件，
                                      应含有随机数据

HSTS 选项：
       --no-hsts                   禁用 HSTS
       --hsts-file                 HSTS 数据库路径（将覆盖默认值）

FTP 选项：
 --ftp-user=用户             设置 ftp 用户名为 <用户>。
 --ftp-password=密码         设置 ftp 密码为 <密码>
 --no-remove-listing         不要删除‘.listing’文件
 --no-glob                   不在 FTP 文件名中使用通配符展开
 --no-passive-ftp            禁用“passive”传输模式
 --preserve-permissions      保留远程文件的权限
 --retr-symlinks             递归目录时，获取链接的文件 (而非目录)

FTPS 选项：
       --ftps-implicit                 使用隐式 FTPS（默认端口 990）
       --ftps-resume-ssl               打开数据连接时继续控制连接中的 SSL/TLS 会话
       --ftps-clear-data-connection    只加密控制信道；数据传输使用明文
       --ftps-fallback-to-ftp          回落到 FTP，如果目标服务器不支持 FTPS
WARC 选项：
       --warc-file=文件名          在一个 .warc.gz 文件里保持请求/响应数据
       --warc-header=字符串        在头部插入 <字符串>
       --warc-max-size=数字        将 WARC 的最大尺寸设置为 <数字>
       --warc-cdx                  写入 CDX 索引文件
       --warc-dedup=文件名         不要记录列在此 CDX 文件内的记录
       --no-warc-digests           不要计算 SHA1 摘要
       --no-warc-keep-log          不要在 WARC 记录中存储日志文件
       --warc-tempdir=目录         WARC 写入器的临时文件目录

递归下载：
  -r,  --recursive                 指定递归下载
  -l,  --level=数字                最大递归深度 (inf 或 0 代表无限制，即全部下载)。
       --delete-after              下载完成后删除本地文件
  -k,  --convert-links             让下载得到的 HTML 或 CSS 中的链接指向本地文件
       --convert-file-only         只转换 URL 的文件部分（一般叫做“基础名”/basename）
       --backups=N                 写入文件 X 前，轮换移动最多 N 个备份文件
  -K,  --backup-converted          在转换文件 X 前先将它备份为 X.orig。
  -m,  --mirror                    -N -r -l inf --no-remove-listing 的缩写形式。
  -p,  --page-requisites           下载所有用于显示 HTML 页面的图片之类的元素。
       --strict-comments           用严格方式 (SGML) 处理 HTML 注释。

递归接受/拒绝：
  -A,  --accept=列表               逗号分隔的可接受的扩展名列表
  -R,  --reject=列表               逗号分隔的要拒绝的扩展名列表
       --accept-regex=REGEX        匹配接受的 URL 的正则表达式
       --reject-regex=REGEX        匹配拒绝的 URL 的正则表达式
       --regex-type=类型           正则类型 (posix|pcre)
  -D,  --domains=列表              逗号分隔的可接受的域名列表
       --exclude-domains=列表      逗号分隔的要拒绝的域名列表
       --follow-ftp                跟踪 HTML 文档中的 FTP 链接
       --follow-tags=列表          逗号分隔的跟踪的 HTML 标识列表
       --ignore-tags=列表          逗号分隔的忽略的 HTML 标识列表
  -H,  --span-hosts                递归时转向外部主机
  -L,  --relative                  仅跟踪相对链接
  -I,  --include-directories=列表  允许目录的列表
       --trust-server-names        使用重定向 URL 的最后一段作为本地文件名
  -X,  --exclude-directories=列表  排除目录的列表
  -np, --no-parent                 不追溯至父目录
```

## 实例

```bash
wget--limit-rate=300k http://www.jsdig.com/testfile.zip # wget限速下载
wget -bc http://www.jsdig.com/testfile.zip # -b进行后台下载，-c实现断点续传

wget -m -p --convert-links -P ./LOCAL URL    # 下载整个网站到本地
cd path && wget -nd -pHEKk http://www.pixelbeat.org/cmdline.html  # cd到目录中下载指定网页及其相关的文件使其可完全浏览
wget --user-agent="Mozilla/5.0" http://www.jsdig.com/testfile.zip  # 伪装代理名称下载
wget --mirror http://www.example.com/     # 更新网站的本地拷贝可以方便地用于cron
wget -r -nd -np -l1 -A '*.jpg' http://www.example.com/   # 批量下载文件到当前目录中
wget --tries=40 URL  # 增加重试次数
wget -i filelist.txt    # 下载多个文件
wget --reject=gif url   # 过滤指定格式下载
wget -o download.log URL    # 把下载信息存入日志文件,不希望下载信息直接显示在终端而是在一个日志文件
wget -Q5m -i filelist.txt   # 限制总下载文件大小,注意：这个参数对单个文件下载不起作用，只能递归下载时才有效
wget -r -A.pdf url  # 下载一个网站的所有PDF文件
wget ftp-url    # wget匿名ftp下载
wget --ftp-user=USERNAME--ftp-password=PASSWORD url     # 使用wget用户名和密码认证的ftp下载
wget ftp://remote/file[1-9].iso/                         # 下载FTP站上的整个目录
wget -q -O- http://www.pixelbeat.org/timeline.html | grep 'a href' | head  # 匹配后直接处理输出
echo 'wget url' | at 01:00  # 在下午一点钟下载指定文件到当前目录

wget --spider URL   # 测试下载链接是否有效，--spider`参数进行检查。正确会返回200状态码
wget -nv --spider --force-html -i bookmarks.html  # 检查文件中的链接是否存在
: << comment
可以在以下几种情况下使用`--spider`参数：
定时下载之前进行检查
间隔检测网站是否可用
检查网站页面的死链接
comment

# wget默认会以最后一个符合`/`的后面的字符来命令，对于动态链接的下载通常文件名会不正确
wget http://www.jsdig.com/download.aspx?id=1080 # 错误：此例会下载一个文件并以名称`download.aspx?id=1080`保存
wget -O wordpress.zip http://www.jsdig.com/download.aspx?id=1080    # 正确：为解决此问题，使用参数`-O`来指定一个文件名

```
