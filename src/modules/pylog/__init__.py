"""Pylog

The new python logger

This project is licenced under the GNU GENERAL PUBLIC LICENSE

For more info visit: https://github.com/awesomelewis2007/pylog
"""
import datetime
def log(location,msg,log_time=True,file=False):
    """# Pylog - log

    generates a log message
    
    example:
        script:
            import pylog

            pylog.log("system.log","this is a log")
        output:
            [LOG] [0000-00-00 00:00:00.000000] this is a log
    Args:
        location ([str]): [Defines the location of the log file]
        msg ([str]): [Message to log]
        log_time (bool, optional): [Defines wether the time of the log is added onto the log]. Defaults to True.
        file (bool, optional): [Defines wether a file name should be logged you need to define the file ]. Defaults to False.
    """
    try:
        log_file = open(location,"a")
    except FileNotFoundError:
        log_file = open(location,"w")
    log_message = "[LOG]"+" "
    if log_time == True:
        log_message = log_message + "["+str(datetime.datetime.now())+"]"+" "
    if file != False:
        log_message = log_message + "["+file+"]"+" "
    log_message = log_message + msg +"\n"
    log_file.write(log_message)
    log_file.close()
    del log_file 

def info(location,msg,log_time=True,file=False):
    """# Pylog - info

    generates a info log
    
    example:
        script:
            import pylog

            pylog.info("system.log","this is a log")
        output:
            [INFO] [0000-00-00 00:00:00.000000] this is a log
    Args:
        location ([str]): [Defines the location of the log file]
        msg ([str]): [Message to log]
        log_time (bool, optional): [Defines wether the time of the log is added onto the log]. Defaults to True.
        file (bool, optional): [Defines wether a file name should be logged you need to define the file ]. Defaults to False.
    """
    try:
        log_file = open(location,"a")
    except FileNotFoundError:
        log_file = open(location,"w")
    log_message = "[INFO]"+" "
    if log_time == True:
        log_message = log_message + "["+str(datetime.datetime.now())+"]"+" "
    if file != False:
        log_message = log_message + "["+file+"]"+" "
    log_message = log_message + msg +"\n"
    log_file.write(log_message)
    log_file.close()
    del log_file
def debug(location,msg,log_time=True,file=False):
    """# Pylog - debug

    generates a debug log
    
    example:
        script:
            import pylog

            pylog.debug("system.log","this is a log")
        output:
            [DEBUG] [0000-00-00 00:00:00.000000] this is a log
    Args:
        location ([str]): [Defines the location of the log file]
        msg ([str]): [Message to log]
        log_time (bool, optional): [Defines wether the time of the log is added onto the log]. Defaults to True.
        file (bool, optional): [Defines wether a file name should be logged you need to define the file ]. Defaults to False.
    """
    try:
        log_file = open(location,"a")
    except FileNotFoundError:
        log_file = open(location,"w")
    log_message = "[DEBUG]"+" "
    if log_time == True:
        log_message = log_message + "["+str(datetime.datetime.now())+"]"+" "
    if file != False:
        log_message = log_message + "["+file+"]"+" "
    log_message = log_message + msg +"\n"
    log_file.write(log_message)
    log_file.close()
    del log_file
def warn(location,msg,log_time=True,file=False):
    """# Pylog - warn

    generates a warn log
    
    example:
        script:
            import pylog

            pylog.warn("system.log","this is a log")
        output:
            [WARNING] [0000-00-00 00:00:00.000000] this is a log
    Args:
        location ([str]): [Defines the location of the log file]
        msg ([str]): [Message to log]
        log_time (bool, optional): [Defines wether the time of the log is added onto the log]. Defaults to True.
        file (bool, optional): [Defines wether a file name should be logged you need to define the file ]. Defaults to False.
    """
    try:
        log_file = open(location,"a")
    except FileNotFoundError:
        log_file = open(location,"w")
    log_message = "[WARNING]"+" "
    if log_time == True:
        log_message = log_message + "["+str(datetime.datetime.now())+"]"+" "
    if file != False:
        log_message = log_message + "["+file+"]"+" "
    log_message = log_message + msg +"\n"
    log_file.write(log_message)
    log_file.close()
    del log_file

def error(location,msg,log_time=True,file=False):
    """# Pylog - error

    generates a error log
    
    example:
        script:
            import pylog

            pylog.error("system.log","this is a log")
        output:
            [ERROR] [0000-00-00 00:00:00.000000] this is a log
    Args:
        location ([str]): [Defines the location of the log file]
        msg ([str]): [Message to log]
        log_time (bool, optional): [Defines wether the time of the log is added onto the log]. Defaults to True.
        file (bool, optional): [Defines wether a file name should be logged you need to define the file ]. Defaults to False.
    """
    try:
        log_file = open(location,"a")
    except FileNotFoundError:
        log_file = open(location,"w")
    log_message = "[ERROR]"+" "
    if log_time == True:
        log_message = log_message + "["+str(datetime.datetime.now())+"]"+" "
    if file != False:
        log_message = log_message + "["+file+"]"+" "
    log_message = log_message + msg +"\n"
    log_file.write(log_message)
    log_file.close()
    del log_file
def cerror(location,msg,log_time=True,file=False):
    """# Pylog - critical error

    generates a critical error log
    
    example:
        script:
            import pylog

            pylog.cerror("system.log","this is a log")
        output:
            [CRITICAL_ERROR] [0000-00-00 00:00:00.000000] this is a log
    Args:
        location ([str]): [Defines the location of the log file]
        msg ([str]): [Message to log]
        log_time (bool, optional): [Defines wether the time of the log is added onto the log]. Defaults to True.
        file (bool, optional): [Defines wether a file name should be logged you need to define the file ]. Defaults to False.
    """
    try:
        log_file = open(location,"a")
    except FileNotFoundError:
        log_file = open(location,"w")
    log_message = "[CRITICAL_ERROR]"+" "
    if log_time == True:
        log_message = log_message + "["+str(datetime.datetime.now())+"]"+" "
    if file != False:
        log_message = log_message + "["+file+"]"+" "
    log_message = log_message + msg +"\n"
    log_file.write(log_message)
    log_file.close()
    del log_file
def ferror(location,msg,log_time=True,file=False):
    """# Pylog - fatal error

    generates a critical error log
    
    example:
        script:
            import pylog

            pylog.ferror("system.log","this is a log")
        output:
            [FATAL_ERROR] [0000-00-00 00:00:00.000000] this is a log
    Args:
        location ([str]): [Defines the location of the log file]
        msg ([str]): [Message to log]
        log_time (bool, optional): [Defines wether the time of the log is added onto the log]. Defaults to True.
        file (bool, optional): [Defines wether a file name should be logged you need to define the file ]. Defaults to False.
    """
    try:
        log_file = open(location,"a")
    except FileNotFoundError:
        log_file = open(location,"w")
    log_message = "[FATAL_ERROR]"+" "
    if log_time == True:
        log_message = log_message + "["+str(datetime.datetime.now())+"]"+" "
    if file != False:
        log_message = log_message + "["+file+"]"+" "
    log_message = log_message + msg +"\n"
    log_file.write(log_message)
    log_file.close()
    del log_file

def message(location,msg):
    """# Pylog - messsage

    writes a message in a log file
    
    example:
        script:
            import pylog

            pylog.message("system.log","this is a log")
        output:
            this is a message
    Args:
        location ([str]): [Defines the location of the log file]
        msg ([str]): [Message to log]
    """
    try:
        log_file = open(location,"a")
    except FileNotFoundError:
        log_file = open(location,"w")
    log_message = msg +"\n"
    log_file.write(log_message)
    log_file.close()
    del log_file