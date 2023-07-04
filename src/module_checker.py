def get_avaible_modules():
    import json
    with open('app_data/system_os.txt', 'r') as f:
        system = f.read()
        f.close()
    if system == "Linux":
        f = open('app_data\modules_linux.json')
    if system == "Windows":
        f = open('app_data\modules_win.json')
    data = json.load(f)

    return data["pypi"],data["github"] # pypi,github = get_avaible_modules()