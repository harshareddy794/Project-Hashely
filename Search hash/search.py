import xlrd
def sha256(row,col,inp):
    for i in range(0,row):
        if(inp==sheet.cell_value(i,1)):
            print("Found data in database.It's SHA256 hash:")
            print(sheet.cell_value(i,0))
            break
    print("Hash not found in database")
def md5(row,col,inp):
    for i in range(0,row):
        if(inp==sheet.cell_value(i,2)):
            print("Found data in database.It's MD5 hash:")
            print(sheet.cell_value(i,0))
            break
    print("Hash not found in database")
if __name__ == '__main__':
    file='hash.xls'
    inp=input("Enter input:")
    wb=xlrd.open_workbook(file)
    sheet = wb.sheet_by_index(0)
    row=sheet.nrows
    col=sheet.ncols
    if(len(inp)==64):
        print("Searching data in database")
        sha256(row,col,inp)
    elif(len(inp)==32):
        print("Searching data in database")
        md5(row,col,inp)
    else:
        print("Invalid hash format")
