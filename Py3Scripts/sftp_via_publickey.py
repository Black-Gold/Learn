import os
import paramiko
import subprocess
from shutil import copy2

xxxpath="xxx/xxx"
# 私钥可以被paramiko使用执行转换命令：ssh-keygen -p -m PEM -f ~/.ssh/copyid_rsa
key_path = 'xxx/.ssh/copyid_rsa'


# 定义上传函数,paramiko通过公钥免密连接
def upload(root_path, key_private_path):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname='服务器ip', port='端口',
                username='用户', key_filename=key_private_path, allow_agent=True)
    sftp = ssh.open_sftp()
    for root, dirs, files in os.walk(xxxpath):
        root_linux = root.replace('\\', '/')
        # sftp的mkdir函数不支持创建多级目录，固使用ssh连接后linux原生命令创建
        remote_path = os.path.join('xxx/path', root_linux[29:])
        stdin, stdout, stderr = ssh.exec_command(
            ''.join(['mkdir -p ' + remote_path]))
    # 利用os的walk函数获取本地目录文件列表
    for root, dirs, files in os.walk(xxxpath):
        root_linux = root.replace('\\', '/')
        remote_path = os.path.join('xxx/path/', root_linux[29:])
        for file in files:
           upload_file = os.path.join(root_linux, file).replace('\\', '/')
           print(u'Put files...' + upload_file)
           sftp.put(upload_file, os.path.join(
               remote_path, file).replace('\\', '/'))
    ssh.close()
    sftp.close()


upload(xxxpath, key_path)
