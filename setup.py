import os
from os.path import exists
import urllib.request
# debug printing added

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def datafolder():
    return os.path.expanduser("~")

def installPackage(pkname, dir, username):
    urllib.request.urlretrieve("https://raw.githubusercontent.com/Kiffolisk/pykern-setup/main/" + pkname + ".py", dir + "/user/" + username + "/pkg/" + pkname + ".py")

def mkdir(newpath):
    if not os.path.exists(newpath):
        print("A new path doesn't exist, creating a new one")
        os.makedirs(newpath)
        

def setupInit():
    import main
    cls()
    print("PyKern Setup")
    print("The Terminal OS made on python for fun!")
    print("Choose install directory:")
    installdir = input()
    print("[-] Creating config file...")
    configfile = open(datafolder() + "/config.pykern", "w")
    configfile.write(installdir)
    configfile.close()
    print("[-] Creating the directory for installation...")

    mkdir(installdir)

    cls()
    print("Choose a username you want to use: ")
    username = input()
    print("[-] Creating the directory for user...")

    mkdir(installdir + "/user/" + username)

    print(installdir + "/user/" + username + "/pkg")

    mkdir(installdir + "/user/" + username + "/pkg")

    usrfile = open(installdir + "/user/.curuser", "w")
    usrfile.write(username)
    usrfile.close()

    print("[-] Setup has ended successfully!")
    print("Attempting to boot...")
    installPackage("sip", installdir, username)
    installPackage("sip-uninstall", installdir, username)
    installPackage("sip-update", installdir, username)
    main.boot()
