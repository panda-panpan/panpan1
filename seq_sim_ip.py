import csv
f=open('seq_sim_ip.csv','w',encoding='gb2312',newline='')
csv_writer=csv.writer(f)
#csv_writer.writerow(['地址','端口','协议','服务','状态','单位'])
with open('D:/20200729.csv','r',encoding='gb2312')as fp1:
    list1=[i for i in csv.reader(fp1)]
    #print(list1)
with open('D:/20200729 (1).csv','r',encoding='gb2312') as fp2:
    list2=[i for i in csv.reader(fp2)]
    #print(list2)
for i in list1:
    for j in list2:
        if (i[0]==j[0] and i[1]==j[1]):
            csv_writer.writerow([i[0],i[1],i[2],i[3],i[4],i[5]])