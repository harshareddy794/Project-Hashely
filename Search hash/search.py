import xlrd
def sha256(rows,cols,inp):
    for row in range(0,rows):
        if(inp==sheet.cell_value(row,1)):
            print("Found data in database.It's SHA256 hash:")
            return(sheet.cell_value(row,0))
            break
def md5(rows,cols,inp):
    for row in range(0,rows):
        if(inp==sheet.cell_value(row,2)):
            print("Found data in database.It's MD5 hash:")
            return(sheet.cell_value(row,0))
            break
if __name__ == '__main__':
    file='hash.xls'
    inp=input("Enter input:")
    wb=xlrd.open_workbook(file)
    sheet = wb.sheet_by_index(0)
    rows=sheet.nrows
    cols=sheet.ncols
    op=None
    if(len(inp)==64):
        print("Searching data in database")
        opt=sha256(rows,cols,inp)
        print(op)
        if(opt==None):
            print("Hash not found in database")
    elif(len(inp)==32):
        print("Searching data in database")
        op=md5(rows,cols,inp)
        print(op)
        if(opt==None):
            print("Hash not found in database")
    else:
        print("Invalid hash format")
