def get(repo):
    import requests
    data = requests.get("https://api.github.com/repos/awesomelewis2007/"+repo+"/releases").json()
    data = data[0]
    return data["tag_name"]
