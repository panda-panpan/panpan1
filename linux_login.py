import pexpect
import sys
password='abcdefghijklmn'
ssh=pexpect.spawn('ssh root@10.212.1.1 -p 22')
status=ssh.expect(['password:','continue connecting (yes/no)?',pexpect.TIMEOUT,pexpect.EOF],timeout=50)
if status==0:
    ssh.sendline(password)  #输入密码
elif status ==1:
    ssh.send('yes')
    ssh.expect('password: ')
    ssh.sendline(password)
elif status==2:
    sys.exit()
elif status==3:
    sys.exit()
index=ssh.expect(['#',pexpect.EOF,pexpect.TIMEOUT])
if index==0:
    print('You were logged in as root.')
    #ssh.interact() #远连，交互
    #可以通过ssh.senline做账户切换，根据status=ssh.expect状态码判断是否切换成功