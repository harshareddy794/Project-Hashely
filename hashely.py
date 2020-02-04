import xlrd
#import xlwt
import hashlib
def hash():
    print("Hash in which format?")
    print("[1].sha256\n"+"[2].MD5")
    inp_opt=int(input())
    print("Enter string to hash it")
    inp_str=input()
    inp_str=inp_str.encode('utf-8')
    if(inp_opt==1):
        opt=hashlib.new('sha256',inp_str).hexdigest()
    if(inp_opt==2):
        opt=hashlib.new('md5',inp_str).hexdigest()
    print(opt)

def dehash(rows,cols):
    inp=input("Enter hash to decrypt it :")
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
    try:
        file='hash.xls'
        wb=xlrd.open_workbook(file)
        sheet = wb.sheet_by_index(0)
        print("Welcome to Project hashely\n"+"What do you want to do now")
        print("[1].Hash\n"+"[2].Dehash")
        inp=int(input())
        if(inp==1):
            hash()
        if(inp==2):
            rows=sheet.nrows
            cols=sheet.ncols
            dehash(rows,cols)
        else:
            print("Enter correct option")
    except:
        print("Enter option correctly")
