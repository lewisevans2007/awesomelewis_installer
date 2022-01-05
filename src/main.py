# awesomelewis installer
# main file
import sys
import platform
import os
import requests
import shutil

from modules import pylog
from modules.installer import pypi as pypiinstaller
from modules.installer import github as githubinstaller

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
import module_checker


global verbose
verbose = False
class logger:
    def error(msg ,file="app_data/log/system.log"):
        if verbose:
            print(bcolors.FAIL+"[ X ] ERROR:"+msg+bcolors.ENDC)
        pylog.error(file,msg)
    def info(msg,file="app_data/log/system.log"):
        if verbose:
            print("[ i ] INFO:"+msg)
        pylog.info(file,msg)
    def warning(msg ,file="app_data/log/system.log"):
        if verbose:
            print(bcolors.WARNING+"[ ! ] WARNING:"+msg+bcolors.ENDC)
        pylog.warn(file,msg)

def sys_check():
    logger.info("Start of system check",file="app_data\log\sys_check.log")
    system = platform.system()
    logger.info("Detected system: "+system,file="app_data\log\sys_check.log")
    if system == "Darwin":
        system = "Linux" 
        # Before you get angry at me!
        # I know mac os or unix is not Darwin but my software is 
        # compatible for Darwin based systems
    with open('app_data/system_os.txt', 'w') as f:
        f.write(system)
        f.close()
    try:
        request = requests.get("https://www.github.com", timeout=15)
        logger.info("Connected to github.com")
    except (requests.ConnectionError, requests.Timeout) as exception:
        logger.error("Cant talk to github.com trying google.com") 
        try:
            request = requests.get("https://www.google.com", timeout=15)
            logger.info("Connected to google.com")
        except (requests.ConnectionError, requests.Timeout) as exception:
            logger.error("Cant talk to google.com closing app")   
            print("You are not connected to the internet or that github and google is down")
            exit()
        print("I cant connect to github.com but i can talk to google.com\nIt looks like github is down\nCheck here:https://status.github.com/")
        exit()
def more_options():
    print("More options")
    print("1) Uninstall a python module using pip")
    print("2) Clear cache")
    print("3) Exit")
    continue_loop = True
    while continue_loop == True:
        menu = input("Enter option>")
        if menu == "1":
            logger.info("Opening pip uninstaller handing over to uninstall.log")
            continue_loop = False
            print("Welcome to the python package remover tool this will remove any package that is installed on your system")
            module = input("Enter a package name>")
            cmd = "pip uninstall "+module
            if verbose:
                cmd = cmd + " -v"
            os.system(cmd)
            del cmd
            exit()
        if menu == "2":
            try:
                shutil.rmtree('tmp')
                exit()
            except FileNotFoundError:
                print("There is no cache found nothing was changed")
                exit()
        if menu == "3":
            logger.info("Quiting app")
            exit()
        else:
            print("Please enter a number 1,2 or 3")
def main():
    print("welcome to awesomelewis's project installer please chose an option")
    print("1) Install an module from github or from the python package index")
    print("2) More options")
    print("3) Exit")
    continue_loop = True
    while continue_loop == True:
        menu = input("Enter option>")
        if menu == "1":
            continue_loop = False
            pypi, github = module_checker.get_avaible_modules()
            print("GitHub:")
            for i in github:
                print(bcolors.OKGREEN+"\t"+i+bcolors.ENDC)
            print("PyPi:")
            for i in pypi:
                print(bcolors.OKGREEN+"\t"+i+bcolors.ENDC)      
            print("All github packages will install to the desktop and all pypi \npackages will install to your python installation")     
            print("\nEnter witch item you want to install")
            found = False
            while found == False:
                package_name = input("Enter name of package>")
                for i in github:
                    if i.upper() == package_name.upper():
                        found = True
                        is_git_package = True
                for i in pypi:
                    if i.upper() == package_name.upper():
                        found = True
                        is_git_package = False                    
                if found == False:
                    print("The package "+package_name+" was not found or it is incompatible for your system please try again")
            if is_git_package == True:
                githubinstaller.install(package_name)
            if is_git_package == False:
                pypiinstaller.install(package_name)
            exit()
        if menu == "2":
            continue_loop = False
            more_options()
        if menu == "3":
            logger.info("Quiting app")
            exit()
        else:
            print("Please enter a number 1,2 or 3")
if __name__ == "__main__":
    pylog.message("app_data/log/system.log","---------------- START ----------------")
    for i in sys.argv:
        if i == "-v" or i == "--verbose":
            verbose = True
    try:
        os.mkdir("tmp")
        logger.info("Created tmp folder")
    except FileExistsError:
        logger.info("Attempted to create tmp folder but it was already there")  
    logger.info("Checking system info check")
    sys_check()
    logger.info("Staring main process")
    main()
