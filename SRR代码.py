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