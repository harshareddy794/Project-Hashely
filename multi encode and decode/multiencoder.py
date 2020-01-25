import base64

def intro():
        print("MULTI ENCODER AND DECODER\n"+"Good day")


def converter():
    try:
        print("\nWhat is your input type?")
        print("[1] Binary\n"+"[2] Hex\n"+"[3] Interger\n"+"[4] Octal\n"+"[5] base64\n"+"[6] Ascii code"+"[7] Text")
        inp=int(input("Enter option:"))
        print("\nWhat output do you need?")
        print("[1] Binary\n"+"[2] Hex\n"+"[3] Interger\n"+"[4] Octal\n"+"[5] base64\n"+"[6] Ascii code"+"[7] Text")
        out=int(input("Enter option:"))
    except:
        print("Enter correct inputs!")
        exit()

    if(inp==1):
        binary(out)


def binary(out):
    try:
        if(out==1):
            data=input()
            print(data)
        if(out==2):
            data=input()
            print(hex(int(data,2)))
        if(out==3):
            data=input()
            print(int(data,2))
        if(out==4):
            data=input()
            print(oct(int(data,2)))
        if(out==5):
            data=input()
            print(data.encode('base64'))
        if(out==6):
            data=input()
            print(int(data,2))
        if(out==7):
            data=input()
            print(str(int(data,2)))

    except:
        print("Enter correct inputs")



if __name__ == '__main__':
    intro()
    converter()
