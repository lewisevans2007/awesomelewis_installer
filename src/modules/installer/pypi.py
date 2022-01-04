def install(name):
    import os
    if name.upper() == "PYKEYGEN":
        name = "pykeygenerator"
    os.system("pip install "+name)
