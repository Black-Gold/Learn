# **ssh-keygen**

## 说明

**ssh-keygen命令** 用于为“ssh”生成、管理和转换认证密钥，它支持RSA和DSA两种认证密钥

## 选项

```markdown
用法: ssh-keygen [-q] [-b bits] [-t dsa | ecdsa | ed25519 | rsa | rsa1]
                  [-N new_passphrase] [-C comment] [-f output_keyfile]
ssh-keygen -p [-P old_passphrase] [-N new_passphrase] [-f keyfile]
ssh-keygen -i [-m key_format] [-f input_keyfile]
ssh-keygen -e [-m key_format] [-f input_keyfile]
ssh-keygen -y [-f input_keyfile]
ssh-keygen -c [-P passphrase] [-C comment] [-f keyfile]
ssh-keygen -l [-v] [-E fingerprint_hash] [-f input_keyfile]
ssh-keygen -B [-f input_keyfile]
ssh-keygen -D pkcs11
ssh-keygen -F hostname [-f known_hosts_file] [-l]
ssh-keygen -H [-f known_hosts_file]
ssh-keygen -R hostname [-f known_hosts_file]
ssh-keygen -r hostname [-f input_keyfile] [-g]
ssh-keygen -G output_file [-v] [-b bits] [-M memory] [-S start_point]
ssh-keygen -T output_file -f input_file [-v] [-a rounds] [-J num_lines]
           [-j start_line] [-K checkpt] [-W generator]
ssh-keygen -s ca_key -I certificate_identity [-h] [-n principals]
           [-O option] [-V validity_interval] [-z serial_number] file ...
ssh-keygen -L [-f input_keyfile]
ssh-keygen -A
ssh-keygen -k -f krl_file [-u] [-s ca_public] [-z version_number]
           file ...
ssh-keygen -Q -f krl_file file ...


