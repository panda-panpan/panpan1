#使用Nmap模块进行主机发现

import nmap
nm=nmap.PortScanner()
result=nm.scan('192.168.1.0/24',arguments='-sP').get('scan')
