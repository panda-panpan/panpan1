import pexpect
#spawn类启动一个子程序，有丰富的方法实现对 子程序的控制
ssh_k=pexpect.spawn('ssh root@172.16.22.1 -p22')#生成子程序，去连接192.168.1.18

ssh_k.expect('[p,P]assword:')
#expect 已正则表达式的方式：匹配缓冲区执行结果包含password:的内容；
# 正则匹配成功 返回0，正则匹配不成功一直等待返回，直到子程序到达超时时间（30秒）；

ret=ssh_k.expect([pexpect.EOF,pexpect.TIMEOUT,'password'])
print(ret)
#匹配3种情况：错误输出：pexpect.EOF 超时：pexpect.TIMEOUT 正确：password
#正则匹配pexpect.EOF返回0 ，pexpect.TIMEOUT 返回1 ， password成功 返回2,