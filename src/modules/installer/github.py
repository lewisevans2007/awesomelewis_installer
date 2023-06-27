from tqdm import tqdm
class DownloadProgressBar(tqdm):
    def update_to(self, b=1, bsize=1, tsize=None):
        if tsize is not None:
            self.total = tsize
        self.update(b * bsize - self.n)

def install(name):
    import urllib
    import tag_finder
    import zipfile
    import os
    from main import logger
    try:
        username = os.getlogin()
    except:
        logger.error("Cant get the username for some reason")
    tag = tag_finder.get(name)
    if os.path.exists("tmp/"+name+"-"+tag+".zip"):
        print("A cache file was found for the current version of "+name)
        print("Version: "+tag)
        ask = input("Do you want to use this file rather than downloading again? (Y or N):")
        if ask.upper() == "Y" or ask.upper() == "YES" or ask.upper() == "YE" or ask.upper() == "OK":
            with zipfile.ZipFile("tmp/"+name+"-"+tag+".zip", 'r') as zip_ref:
                with open('app_data/system_os.txt', 'r') as f:
                    system = f.read()
                    f.close()
                if system == "Linux":
                    zip_ref.extractall("home/"+username+"/Desktop")
                if system == "Windows":
                    zip_ref.extractall("C:/users/"+username+"/Desktop")
            return "Done"
        else:
            pass
    logger.info("Downloading file :https://github.com/awesomelewis2007/"+name+"/archive/refs/tags/"+tag+".zip")
    print("Downloading "+name+" with the tag "+tag)
    with DownloadProgressBar(unit='B', unit_scale=True,miniters=1, desc=name+" "+tag) as t:
        urllib.request.urlretrieve("https://github.com/awesomelewis2007/"+name+"/archive/refs/tags/"+tag+".zip", filename="tmp/"+name+"-"+tag+".zip", reporthook=t.update_to)
    logger.info("Extracting file")
    with zipfile.ZipFile("tmp/"+name+"-"+tag+".zip", 'r') as zip_ref:
            with open('app_data/system_os.txt', 'r') as f:
                system = f.read()
                f.close()
            if system == "Linux":
                zip_ref.extractall("home/"+username+"/Desktop")
            if system == "Windows":
                zip_ref.extractall("C:/users/"+username+"/Desktop")
        