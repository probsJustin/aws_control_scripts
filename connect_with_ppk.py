import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('<hostname>', username='<username>', password='<password>', key_filename='<path/to/openssh-private-key-file>')
stdin, stdout, stderr = ssh.exec_command('ls')
print(stdout.readlines())
ssh.close()