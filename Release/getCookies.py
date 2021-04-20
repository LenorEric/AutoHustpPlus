import requests


def getID(user="", pwd=""):
    if user == "":
        print("Username(Cellphone Number): ", end="")
        user = input()
    if pwd == "":
        print("Password: ", end="")
        pwd = input()
    return [user, pwd]


def getCookies(user="", pwd=""):
    user, pwd = getID(user, pwd)
    session = requests.session()
    url = "http://dzdq.hustp.com/index.php?m=Login&a=checkloginuser"
    formData = {
        "backurl": "",
        "phone": str(user),
        "password": pwd,
        "remember": '1'
    }
    req_header = {
        "User-Agent""": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 "
                        "Safari/537.36",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    response = session.post(url, headers=req_header, data=formData)
    session.close()
    if response.status_code == 200:
        if "password" in response.cookies.keys():
            print("Login Successfully")
            return response.cookies
        else:
            print("Login Failed, Check Number and Password")
            return 1
    else:
        return 1


if __name__ == '__main__':
    print("This can be only imported")
