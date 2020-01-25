import xlrd
import xlwt
from xlwt import Workbook
import hashlib

if __name__ == '__main__':
    data=open('10,000.txt')
    wb=Workbook()
    sheet=wb.add_sheet('sheet1')
    j=0
    for i in data:
        s=(hashlib.new('sha256',(i.rstrip('\n')).encode('utf-8')).hexdigest())
        md=(hashlib.new('md5',(i.rstrip('\n')).encode('utf-8')).hexdigest())
        j=j+1
        sheet.write(j,0,i.rstrip('\n'))
        sheet.write(j,1,s)
        sheet.write(j,2,md)
    wb.save('10000_hash.xls')
    print("Done")
