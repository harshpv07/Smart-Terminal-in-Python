def touch(x):
    file = open(x, "w")
    print("Enter 1 to write to the file")
    print("Enter 2 to exit the file")
    d = int(input("Enter the command"))
    if d == 1:
        l = str(input("Enter the text")) 
        file.write(l)
        file.close()
        print("The file has been saved successfully")
    if d == 2:
        file.close()
        print("File successfully saved and exited") 
