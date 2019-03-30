import os, sys
x = str(input("Enter  a file name"))
y = str(input("Enter the location in which you want to save"))
path = "C:\\Users\\PREMRAJ\\"+y+"\\" + x
os.mkdir(path)

print("Path is created")