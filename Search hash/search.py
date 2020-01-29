import xlrd
def sha256(rows,cols,inp):
    for row in range(0,rows):
        if(inp==sheet.cell_value(row,1)):
            print("Found data in database.It's SHA256 hash:")
            print(sheet.cell_value(row,0))
            break
    print("Hash not found in database")
def md5(rows,cols,inp):
    for row in range(0,rows):
        if(inp==sheet.cell_value(row,2)):
            print("Found data in database.It's MD5 hash:")
            print(sheet.cell_value(row,0))
            break
    print("Hash not found in database")
if __name__ == '__main__':
    file='hash.xls'
    inp=input("Enter input:")
    wb=xlrd.open_workbook(file)
    sheet = wb.sheet_by_index(0)
    rows=sheet.nrows
    cols=sheet.ncols
    if(len(inp)==64):
        print("Searching data in database")
        sha256(rows,cols,inp)
    elif(len(inp)==32):
        print("Searching data in database")
        md5(rows,cols,inp)
    else:
        print("Invalid hash format")
