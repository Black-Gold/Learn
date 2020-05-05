import os
import paramiko
import subprocess
from shutil import copy2

xxxpath="xxx/xxx"
# RSA格式私钥可以被paramiko使用执行转换命令：ssh-keygen -p -m PEM -t RSA -f ~/.ssh/copyid_rsa
key_path = 'xxx/.ssh/copyid_rsa'


# 定义上传函数,paramiko通过公钥免密连接
def upload(root_path, privateKey):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname='服务器ip', port='端口',
                username='用户', key_filename=privateKey, allow_agent=True)
    sftp = client.open_sftp()
    # 利用os的walk函数获取本地目录文件列表
    for dirspath, dirsname, files in os.walk(xxxpath):
        root_linux = dirspath.replace('\\', '/')
        # sftp的mkdir函数不支持创建多级目录，固使用ssh连接后linux原生命令创建
        remote_path = os.path.join('xxx/path', root_linux[29:])
        stdin, stdout, stderr = client.exec_command(
            ''.join(['mkdir -p ' + remote_path]))
        for file in files:
           upload_file = os.path.join(root_linux, file).replace('\\', '/')
           print(u'Put files...' + upload_file)
           sftp.put(upload_file, os.path.join(
               remote_path, file).replace('\\', '/'))
    client.close()
    sftp.close()


upload(xxxpath, key_path)
