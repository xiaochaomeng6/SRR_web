# SRR_web
#八位数的SRR号下载网址为http://ftp.sra.ebi.ac.uk/vol1/srr/SRRxxx/0yz/SRR号
#七位数的SRR号下载网址为http://ftp.sra.ebi.ac.uk/vol1/srr/SRRxxx/00z/SRR号
#六位数的SRR号下载网址为http://ftp.sra.ebi.ac.uk/vol1/srr/SRRxxx/SRR号

#XXX为SRR号前三位
#y为SRR号倒数第二位
#z为SRR号倒数第一位



import re
my_list1 = []
#输入文件
with open('D:\\腾讯\\2250619732\\FileRecv\\GSE163558.txt','r') as f:
#输出文件
with open('D:\\腾讯\\2250619732\\FileRecv\\GSE163558zhaodao.txt','w',encoding='utf-8') as h:
    my_list = f.readlines()
    for i in my_list:
        if len(i) == 10:
            a = i.strip()
            six = 'http://ftp.sra.ebi.ac.uk/vol1/srr/'  + a[:6]  +'/' + i
            h.write(six)
        elif len(i) == 11:
            a = i.strip()
            seven = 'http://ftp.sra.ebi.ac.uk/vol1/srr/'  + a[:6] + '/00' + a[9:] +'/' + i
            h.write(seven)
        elif len(i) == 12:
            a = i.strip()
            eight = 'http://ftp.sra.ebi.ac.uk/vol1/srr/' + a[:6] + '/0' + a[9:] + '/' + i
            h.write(eight)
        else:
            h.write(i)
