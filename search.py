import xlrd
def sha256(rows,cols,inp):
    for col in range(1,cols,4):
        for row in range(0,rows):
            if(inp==sheet.cell_value(row,col)):
                print("Found data in database.It's SHA256 hash:")
                return(sheet.cell_value(row,col-1))
                break
def md5(rows,cols,inp):
    for col in range(2,cols,4):
        for row in range(0,rows):
            if(inp==sheet.cell_value(row,col)):
                print("Found data in database.It's MD5 hash:")
                return(sheet.cell_value(row,col-2))
                break
if __name__ == '__main__':
    file='hash.xls'
    inp=input("Enter input:")
    wb=xlrd.open_workbook(file)
    sheet = wb.sheet_by_index(0)
    rows=sheet.nrows
    cols=sheet.ncols
    opt=None
    if(len(inp)==64):
        print("Searching data in database")
        opt=sha256(rows,cols,inp)
        print(opt)
        if(opt==None):
            print("Hash not found in database")
    elif(len(inp)==32):
        print("Searching data in database")
        opt=md5(rows,cols,inp)
        print(opt)
        if(opt==None):
            print("Hash not found in database")
    else:
        print("Invalid hash format")
