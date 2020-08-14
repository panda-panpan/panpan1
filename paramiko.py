import paramiko
 
hostname='10.21.1.1'
username='sadmin'
password='gsadmin'

ssh= paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname=hostname,username=username,password=password)
stdin,stdout,stderr=ssh.exec_command('cmd')
print(stdout.read().decode('utf-8'))#ascii,gb2312,gbk
#stdout.readlines()
for line in stdout:
    data=json.loads(line)
    print(date['available'])
#ssh.close()
ssh.close()