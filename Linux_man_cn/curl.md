# **curl**

## 说明

**curl命令** 是一个利用URL规则在命令行下工作的文件传输工具。它支持文件的上传和下载，所以是综合传输工具，但按传统，习惯称
curl为下载工具。作为一款强力工具，curl支持包括HTTP、HTTPS、ftp等众多协议，还支持POST、cookies、认证、从指定偏移处下载部分
文件、用户代理字符串、限速、文件大小、进度条等特征。做网页处理流程和数据检索自动化，curl可以祝一臂之力

[curl官网](https://curl.haxx.se/)

## 选项

```markdown
(H) means HTTP/HTTPS only, (F) means FTP only

    --anyauth       Pick "any" authentication method (H)
-a, --append        上传时附加到目标文件(F/SFTP)
    --basic         Use HTTP Basic Authentication (H)
    --cacert FILE   CA certificate to verify peer against (SSL)
    --capath DIR    CA directory to verify peer against (SSL)
-E, --cert CERT[:PASSWD] Client certificate file and password (SSL)
    --cert-type TYPE Certificate file type (DER/PEM/ENG) (SSL)
    --ciphers LIST  SSL ciphers to use (SSL)
    --compressed    Request compressed response (using deflate or gzip)
-K, --config FILE   指定从FILE文件读取配置
    --connect-timeout SECONDS  Maximum time allowed for connection
-C, --continue-at OFFSET  断点续传
-b, --cookie STRING/FILE  String or file to read cookies from (H)
-c, --cookie-jar FILE  操作完成后将cookie写入到这个文件中(H)
    --create-dirs   Create necessary local directory hierarchy
    --crlf          Convert LF to CRLF in upload
    --crlfile FILE  Get a CRL list in PEM format from the given file
-d, --data DATA     HTTP POST方式传输数据(H)
    --data-ascii DATA  HTTP POST ASCII编码方式传输数据 (H)
    --data-binary DATA  HTTP POST binary编码方式传输数据 (H)
    --data-urlencode DATA  HTTP POST data url encoded (H)
    --delegation STRING GSS-API delegation permission
    --digest        使用HTTP数字身份认证(H)
    --disable-eprt  禁止使用EPRT or LPRT (F)
    --disable-epsv  禁止使用EPSV (F)
-D, --dump-header FILE 把header信息写入到FILE文件 
    --egd-file FILE  为随机数据设置EGD socket路径 (SSL)
    --engine ENGINGE  Crypto engine (SSL). "--engine list" for list
-f, --fail          HTTP连接失败时不显示错误 (H)
-F, --form CONTENT  Specify HTTP multipart POST data (H)
    --form-string STRING  Specify HTTP multipart POST data (H)
    --ftp-account DATA  Account data string (F)
    --ftp-alternative-to-user COMMAND  String to replace "USER [name]" (F)
    --ftp-create-dirs  Create the remote dirs if not present (F)
    --ftp-method [MULTICWD/NOCWD/SINGLECWD] Control CWD usage (F)
    --ftp-pasv      Use PASV/EPSV instead of PORT (F)
-P, --ftp-port ADR  使用端口地址而不是使用PASV (F)
    --ftp-skip-pasv-ip Skip the IP address for PASV (F)
    --ftp-pret      Send PRET before PASV (for drftpd) (F)
    --ftp-ssl-ccc   Send CCC after authenticating (F)
    --ftp-ssl-ccc-mode ACTIVE/PASSIVE  Set CCC mode (F)
    --ftp-ssl-control Require SSL/TLS for ftp login, clear for transfer (F)
-G, --get           Send the -d data with a HTTP GET (H)
-g, --globoff       禁用网址序列和范围使用 {} and []
-H, --header LINE   自定义头消息传递给服务器 (H)
-I, --head          Show document info only
    --hostpubmd5 MD5  Hex encoded MD5 string of the host public key. (SSH)
-0, --http1.0       Use HTTP 1.0 (H)
    --ignore-content-length  Ignore the HTTP Content-Length header
-i, --include       Include protocol headers in the output (H/F)
-k, --insecure      允许连接不使用证书连接到SSL站点 (H)
    --interface INTERFACE  Specify network interface/address to use
-4, --ipv4          Resolve name to IPv4 address
-6, --ipv6          Resolve name to IPv6 address
-j, --junk-session-cookies 忽略从文件中读取的session cookie (H)
    --keepalive-time SECONDS  Interval between keepalive probes
    --key KEY       Private key file name (SSL/SSH)
    --key-type TYPE Private key file type (DER/PEM/ENG) (SSL)
    --krb LEVEL     Enable Kerberos with specified security level (F)
    --libcurl FILE  Dump libcurl equivalent code of this command line
    --limit-rate RATE  Limit transfer speed to this rate
-l, --list-only     仅列出ftp目录的名称(F)
    --local-port RANGE  强制使用RANGE内的本地端口号
-L, --location      Follow redirects (H)
    --location-trusted like --location and send auth to other hosts (H)
-M, --manual        Display the full manual
    --mail-from FROM  Mail from this address
    --mail-rcpt TO  Mail to this receiver(s)
    --mail-auth AUTH  Originator address of the original email
    --max-filesize BYTES  Maximum file size to download (H/F)
    --max-redirs NUM  Maximum number of redirects allowed (H)
-m, --max-time SECONDS  设置最大传输时间
    --metalink      Process given URLs as metalink XML file
    --negotiate     Use HTTP Negotiate Authentication (H)
-n, --netrc         必须从.netrc文件读取用户和密码
    --netrc-optional Use either .netrc or URL; overrides -n
    --netrc-file FILE  Set up the netrc filename to use
-N, --no-buffer     禁用buffer缓存输出
    --no-keepalive  Disable keepalive use on the connection
    --no-sessionid  Disable SSL session-ID reusing (SSL)
    --noproxy       List of hosts which do not use proxy
    --ntlm          Use HTTP NTLM authentication (H)
-o, --output FILE   将输出吸入到FILE取代默认输出stdout
    --pass PASS     Pass phrase for the private key (SSL/SSH)
    --post301       Do not switch to GET after following a 301 redirect (H)
    --post302       Do not switch to GET after following a 302 redirect (H)
    --post303       Do not switch to GET after following a 303 redirect (H)
-#, --progress-bar  Display transfer progress as a progress bar
    --proto PROTOCOLS  Enable/disable specified protocols
    --proto-redir PROTOCOLS  Enable/disable specified protocols on redirect
-x, --proxy [PROTOCOL://]HOST[:PORT] Use proxy on given port
    --proxy-anyauth Pick "any" proxy authentication method (H)
    --proxy-basic   Use Basic authentication on the proxy (H)
    --proxy-digest  Use Digest authentication on the proxy (H)
    --proxy-negotiate Use Negotiate authentication on the proxy (H)
    --proxy-ntlm    Use NTLM authentication on the proxy (H)
-U, --proxy-user USER[:PASSWORD]  Proxy user and password
    --proxy1.0 HOST[:PORT]  Use HTTP/1.0 proxy on given port
-p, --proxytunnel   使用HTTP代理隧道 (using CONNECT)
    --pubkey KEY    Public key file name (SSH)
-Q, --quote CMD     传输之前发送命令到服务器 (F/SFTP)
    --random-file FILE  File for reading random data from (SSL)
-r, --range RANGE   仅检索RANGE范围内的字节
    --raw           Do HTTP "raw", without any transfer decoding (H)
-e, --referer       Referer URL (H)
-J, --remote-header-name Use the header-provided filename (H)
-O, --remote-name   将输出写入到文件并以远程文件名称作为输出文件的名称
    --remote-name-all Use the remote file name for all URLs
-R, --remote-time   输出到本地文件时保留远程文件的时间
-X, --request COMMAND  Specify request command to use
    --resolve HOST:PORT:ADDRESS  Force resolve of HOST:PORT to ADDRESS
    --retry NUM   Retry request NUM times if transient problems occur
    --retry-delay SECONDS When retrying, wait this many seconds between each
    --retry-max-time SECONDS  Retry only within this period
-S, --show-error    Show error. With -s, make curl show errors when they occur
-s, --silent        Silent mode. Don't output anything
    --socks4 HOST[:PORT]  SOCKS4 proxy on given host + port
    --socks4a HOST[:PORT]  SOCKS4a proxy on given host + port
    --socks5 HOST[:PORT]  SOCKS5 proxy on given host + port
    --socks5-basic  Enable username/password auth for SOCKS5 proxies
    --socks5-gssapi Enable GSS-API auth for SOCKS5 proxies
    --socks5-hostname HOST[:PORT] SOCKS5 proxy, pass host name to proxy
    --socks5-gssapi-service NAME  SOCKS5 proxy service name for gssapi
    --socks5-gssapi-nec  Compatibility with NEC SOCKS5 server
-Y, --speed-limit RATE  Stop transfers below speed-limit for 'speed-time' secs
-y, --speed-time SECONDS  Time for trig speed-limit abort. Defaults to 30
    --ssl           Try SSL/TLS (FTP, IMAP, POP3, SMTP)
    --ssl-reqd      Require SSL/TLS (FTP, IMAP, POP3, SMTP)
-2, --sslv2         Use SSLv2 (SSL)
-3, --sslv3         Use SSLv3 (SSL)
    --ssl-allow-beast Allow security flaw to improve interop (SSL)
    --stderr FILE   Where to redirect stderr. - means stdout
    --tcp-nodelay   Use the TCP_NODELAY option
-t, --telnet-option OPT=VAL  设置telnet选项
    --tftp-blksize VALUE  Set TFTP BLKSIZE option (must be >512)
-z, --time-cond TIME  Transfer based on a time condition
-1, --tlsv1         Use => TLSv1 (SSL)
    --tlsv1.0       Use TLSv1.0 (SSL)
    --tlsv1.1       Use TLSv1.1 (SSL)
    --tlsv1.2       Use TLSv1.2 (SSL)
    --trace FILE    Write a debug trace to the given file
    --trace-ascii FILE  Like --trace but without the hex output
    --trace-time    Add time stamps to trace/verbose output
    --tr-encoding   Request compressed transfer encoding (H)
-T, --upload-file FILE  上传文件FILE
    --url URL       URL to work with
-B, --use-ascii     使用ASCII/text传输
-u, --user USER[:PASSWORD]  设置服务器的用户和密码
    --tlsuser USER  TLS username
    --tlspassword STRING TLS password
    --tlsauthtype STRING  TLS authentication type (default SRP)
    --unix-socket FILE    Connect through this UNIX domain socket
-A, --user-agent STRING  设置User-Agent发送给服务器(H)
-v, --verbose       Make the operation more talkative
-V, --version       Show version number and quit
-w, --write-out FORMAT  What to output after completion
    --xattr        Store metadata in extended file attributes
-q                 使用时必须作为第一个参数用来关闭.curlrc

```

## 实例

```bash
curl -I http://man.linuxde.net  # 通过-I或者--head可以只打印出HTTP头部信息
curl -H "Host:man.linuxde.net" -H "accept-language:zh-cn" URL # 使用-H "头部信息" 传递多个头部信息
curl URL --silent   # curl默认输出到stdout，将进度信息输出到stderr，不显示进度信息使用--silent选项
curl http://man.linuxde.net/text.iso --silent -O    # 所有下载的数据都被写入到stdout,将下载的数据写入到文件，必须使用绝对路径
curl http://man.linuxde.net/test.iso -o filename.iso --progress # 选项-o将下载数据写入到指定文件中，--progress显示进度
curl URL/File -C 偏移量    # curl能从特定的文件偏移处继续下载，它可以通过指定一个偏移量来下载部分文件,偏移量是以字节为单位的整数
curl http://man.linuxde.net --cookie "user=root;pass=123456"    # 指定cookie，多个cookie使用分号分隔
curl URL --cookie-jar cookie_file # 将cookie另存为一个文件，使用--cookie-jar选项
curl URL --user-agent "Mozilla/5.0" # 使用user-agent访问或下载
curl URL --limit-rate 50k # --limit-rate限制curl的下载速度：k,m,g或K,M,G
curl URL --max-filesize bytes # 使用--max-filesize指定可下载的最大文件大小
curl -u user:pwd http://man.linuxde.net # 使用curl选项-u可以完成HTTP或者FTP的认证，也可以不指定密码在后续操作中输入密码

: << comment
参照页是位于HTTP头部中的一个字符串，用来表示用户是从哪个页面到达当前页面的，如果用户点击网页A中的某个连接，那么用户就会跳转到B网页
网页B头部的参照页字符串就包含网页A的URL,使用--referer选项指定参照页字符串：
comment
curl --referer http://www.google.com http://man.linuxde.net

```
