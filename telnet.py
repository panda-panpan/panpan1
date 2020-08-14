
#过滤主机列表中服务器IP是否为Linux服务器，在ssh服务开启22端口前提下
import telnetlib
#判定是否为linux系统（约定开启22端口）
tn=telnetlib.Telnet(host='10.17.10.112',port='22',timeout=4)
result=tn.read_until(b'\n')
#读取截止到/n的返回结果
print(result)
