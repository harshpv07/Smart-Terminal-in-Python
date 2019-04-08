import os 
import argparse 
from samppy import *
from weather import *
from capture import *
from mkdir import *
from touch import *
from getNics import *

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
    pyAesCrypt.encryptFile(x,(x+".aes"), l, bufferSize)
    os.remove(x)

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

def pwd(args):
    import os
    x = args.pwd[0]
    if(x == 'c'):
        cwd = os.getcwd()
        print(cwd)

def clone(args):
    from git import Repo
    git_url = str(args.clone[0])
    repo_dir = str(args.clone[1])
    Repo.clone_from(git_url, repo_dir)
    print("Repository created and downloaded")

def push(args):
    from git import Repo
    PATH_OF_GIT_REPO = str(args.push[0])
    COMMIT_MESSAGE = str(args.push[1])
    try:
        repo = Repo(PATH_OF_GIT_REPO)
        repo.git.add(update=True)
        repo.index.commit(COMMIT_MESSAGE)
        origin = repo.remote(name='origin')
        origin.push()
    except:
        print('* * * * * * * * * * * *')
    finally:
        print('Code push from script succeeded')       

def ls(args):
    import os
    dir = str(args.ls[0])
    print(os.listdir(dir))

def browse(args):
    import webbrowser
    ur = str(args.browse[0])
    st = "https://www.google.com/search?q=" + ur
    print("Opening the browser")
    webbrowser.open_new(st)

def getNicss(args):
    x = str(args.getNics[0])
    if(x == 'ip'):
        nics = getNics()
        for nic in nics :
            for k,v in nic.items() :
                print('%s : %s'%(k,v))
            print()

def netstat(args):
    x = str(args.netstat[0])
    if (x == "ip"):
        import os
        a=os.popen('netstat -a').read()
        print ('\n Connections',a )

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
      
    parser.add_argument("-rename", type = str, nargs = 2, 
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
    parser.add_argument("-pwd", type = str, nargs = 1, 
                        metavar = ('curr_dir'), 
                        help = "curr_dir")
    parser.add_argument("-clone", type = str, nargs = 2, 
                        metavar = ('clone_fromgit'), 
                        help = "clone_fromgit")
    parser.add_argument("-push", type = str, nargs = 2, 
                        metavar = ('push_togit'), 
                        help = "push_togit")
    parser.add_argument("-ls", type = str, nargs = 1, 
                        metavar = ('show_dir'), 
                        help = "show_dir")
    parser.add_argument("-browse", type = str, nargs = 1, 
                        metavar = ('search'), 
                        help = "search")
    parser.add_argument("-getNics", type = str, nargs = 1, 
                        metavar = ('ipconfig'), 
                        help = "ipconfig")
    parser.add_argument("-netstat", type = str, nargs = 1, 
                        metavar = ('netstat'), 
                        help = "netstat")




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
    elif args.pwd != None: 
        pwd(args)
    elif args.clone != None: 
        clone(args)  
    elif args.push != None: 
        push(args) 
    elif args.ls != None: 
        ls(args)
    elif args.browse != None: 
        browse(args)
    elif args.getNics != None: 
        getNicss(args)
    elif args.netstat != None: 
        netstat(args)        
  

if __name__ == "__main__":  
    main()
    print("-----------------------------------------------------------------------------------")
    print("")
    print("To perform a given task pls enter the code in the given format")
    print("")
    print("python os.py -<function name> <parameters>")
    print("")
    print("")
    print("")
    print("-encrypt (file name)")
    print("-decrypt (file name)")
    print("-weather (Location)")
    print("-video (Song name)")
    print("-mkdir(Directory)")
    print("-rename (old filename) (new filename)")
    print("Copy: -c (current file) (to copy file)")
    print("Delete: -d (current file)")
    print("Read: -r (filename)")
    print("-capture(filename)")
    print("-touch (filename)")
    print("- cd")
    print("- ls (directory)")
    print("- pwd c (current dir)")
    print("-clone (git dir) (store dir)")
    print("-push (repo folder) (commit message)")
    print("-browse (search title)")
    print("-getNics ip")
    print("-netstat ip")
    print("")
    print("")
    print("")
    print("Lets get started")
    print("-------------------------------------------------------------------")
    