import os 
import argparse 
from samppy import *
from weather import *
from capture import *
from mkdir import *
from touch import *

INVALID_FILETYPE_MSG = "Error: Invalid file format. %s must be a .txt file."
INVALID_PATH_MSG = "Error: Invalid file path/name. Path %s does not exist."
  
  
def validate_file(file_name):  
    if not valid_path(file_name): 
        print(INVALID_PATH_MSG%(file_name)) 
        quit() 
    elif not valid_filetype(file_name): 
        print(INVALID_FILETYPE_MSG%(file_name)) 
        quit() 
    return
      
def valid_filetype(file_name): 
    return file_name.endswith('.txt') 
  
def valid_path(path): 
    return os.path.exists(path) 
          
def read(args):  
    file_name = args.read[0] 
    validate_file(file_name) 
    with open(file_name, 'r') as f: 
        print(f.read()) 
  
  
def show(args): 
    dir_path = args.show[0] 
    if not valid_path(dir_path): 
        print("Error: No such directory found.") 
        exit() 
    files = [f for f in os.listdir(dir_path) if valid_filetype(f)] 
    print("{} text files found.".format(len(files))) 
    print('\n'.join(f for f in files)) 
      
  
def delete(args): 
    file_name = args.delete[0] 
    validate_file(file_name) 
    os.remove(file_name) 
    print("Successfully deleted {}.".format(file_name)) 
      
  
def copy(args): 
    file1 = args.copy[0] 
    file2 = args.copy[1] 
    validate_file(file1) 
    if not valid_filetype(file2): 
        print(INVALID_FILETYPE_MSG%(file2)) 
        exit() 
    with open(file1, 'r') as f1: 
        with open(file2, 'w') as f2: 
            f2.write(f1.read()) 
    print("Successfully copied {} to {}.".format(file1, file2)) 
  
  
def rename(args): 
    old_filename = args.rename[0] 
    new_filename = args.rename[1] 
    validate_file(old_filename) 
    if not valid_filetype(new_filename): 
        print(INVALID_FILETYPE_MSG%(new_filename)) 
        exit()  
    os.rename(old_filename, new_filename) 
    print("Successfully renamed {} to {}.".format(old_filename, new_filename)) 

def video(args):
    x = args.video[0]
    getvideo(x)
    print("Playing video")

def weather(args):
    x = args.weather[0]
    getweather(x)

def encrypt(args):
    import pyAesCrypt
    import os
    bufferSize = 64 * 1024
    x = args.encrypt[0]
    l = input("Set password")
    # encrypt
    pyAesCrypt.encryptFile(x,(x+".aes"), l, bufferSize)
    os.remove(x)
    # decrypt
    #pyAesCrypt.decryptFile("data.txt.aes", "dataout.txt", password, bufferSize)

def decrypt(args):
    import pyAesCrypt
    import os
    bufferSize = 64 * 1024
    x = args.decrypt[0]
    l = input("Set password")
    pyAesCrypt.decryptFile(x, "dataout.txt", l, bufferSize)
    os.remove(x)

def capture(args):
    x = args.getcapture[0]
    getcapture(x)
    print("Say Cheese")

def mkdirr(args):
    x = args.mkdir[0]
    mkdir(x)

def touchh(args):
    x = args.touch[0]
    touch(x)




def main():  
    parser = argparse.ArgumentParser(description = "A Custom command Line") 
    parser.add_argument("-r", "--read", type = str, nargs = 1, 
                        metavar = "file_name", default = None, 
                        help = "Opens and reads the specified text file.") 
      
    parser.add_argument("-s", "--show", type = str, nargs = 1, 
                        metavar = "path", default = None, 
                        help = "Shows all the text files on specified directory path.\ Type '.' for current directory.") 
      
    parser.add_argument("-d", "--delete", type = str, nargs = 1, 
                        metavar = "file_name", default = None, 
                        help = "Deletes the specified text file.") 
      
    parser.add_argument("-c", "--copy", type = str, nargs = 2, 
                        metavar = ('file1','file2'), help = "Copy file1 contents to \ file2 Warning: file2 will get overwritten.") 
      
    parser.add_argument("--rename", type = str, nargs = 2, 
                        metavar = ('old_name','new_name'), 
                        help = "Renames the specified file to a new name.")
    parser.add_argument("-video", type = str, nargs = 1, 
                        metavar = ('video'), 
                        help = "Plays video from youtube")

    parser.add_argument("-weather", type = str, nargs = 1, 
                        metavar = ('weather'), 
                        help = "Shows Weather")

    parser.add_argument("-encrypt", type = str, nargs = 1, 
                        metavar = ('encrypt'), 
                        help = "Encrypts file")
    parser.add_argument("-decrypt", type = str, nargs = 1, 
                        metavar = ('decrypt'), 
                        help = "decrypts file")
    parser.add_argument("-capture", type = str, nargs = 1, 
                        metavar = ('capture'), 
                        help = "capture photo")
    parser.add_argument("-mkdir", type = str, nargs = 1, 
                        metavar = ('show_dir'), 
                        help = "show_dir")
    parser.add_argument("-touch", type = str, nargs = 1, 
                        metavar = ('create_file'), 
                        help = "create_file")



    args = parser.parse_args() 
    if args.read != None: 
        read(args) 
    elif args.show != None: 
        show(args) 
    elif args.delete !=None: 
        delete(args) 
    elif args.copy != None: 
        copy(args) 
    elif args.rename != None: 
        rename(args)
    elif args.video != None: 
        video(args)
    elif args.weather != None: 
        weather(args)
    elif args.encrypt != None: 
        encrypt(args)  
    elif args.decrypt != None: 
        decrypt(args)
    elif args.capture != None: 
        getcapture(args)
    elif args.mkdir != None: 
        mkdirr(args) 
    elif args.touch != None: 
        touchh(args)  
  

if __name__ == "__main__":  
    main() 