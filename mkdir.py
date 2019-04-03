import os, sys
def mkdir(x):
    print("Press 1 for Desktop")
    print("Press 2 for Documents")
    print("Press 3 for Downloads")
    print("Press 4 for custom location")
    y = int(input("Press no"))
    if(y == 1):
        path = "C:\\Users\\PREMRAJ\\Desktop\\" + x
        os.mkdir(path)
        print("Created Sucessfully")
    if(y == 2):
        path = "C:\\Users\\PREMRAJ\\Documents\\" + x
        os.mkdir(path)
        print("Created Sucessfully")
    if(y == 3):
        path = "C:\\Users\\PREMRAJ\\Downloads\\" + x
        os.mkdir(path)
        print("Created Sucessfully")
    if(y == 4):
        z = str(input("Enter the path"))
        path = z + x
        os.mkdir(path)
        print("Created Sucessfully")
