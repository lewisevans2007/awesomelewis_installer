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
    logger.info("Downloading file :https://github.com/awesomelewis2007/"+name+"/archive/refs/tags/"+tag+".zip")
    print("Downloading "+name+" with the tag "+tag)
    urllib.request.urlretrieve("https://github.com/awesomelewis2007/"+name+"/archive/refs/tags/"+tag+".zip", "tmp/"+name+"-"+tag+".zip")
    logger.info("Extracting file")
    with zipfile.ZipFile("tmp/"+name+"-"+tag+".zip", 'r') as zip_ref:
            with open('app_data/system_os.txt', 'r') as f:
                system = f.read()
                f.close()
            if system == "Linux":
                zip_ref.extractall("home/"+username+"/Desktop")
            if system == "Windows":
                zip_ref.extractall("C:/users/"+username+"/Desktop")
        