import requests
import os
import getCookies
import getPosts
from sys import exit

user = ""
pwd = ""
ex_id = ""
exList = []

mainSession = requests.session()

if __name__ == '__main__':
    mainSession.cookies = getCookies.getCookies(user, pwd)
    if mainSession.cookies == 1:
        exit()
    if ex_id == '':
        print("Input exercise ID, div by space:")
        exList = input().split(' ')
        for ex_id in exList:
            postRaw = getPosts.getPosts(mainSession.cookies, ex_id)
            url = "http://dzdq.hustp.com/index.php?m=Exercises&a=show_answer"
            req_header = {
                "User-Agent""": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 "
                                "Safari/537.36",
                "Content-Type": "application/x-www-form-urlencoded"
            }
            response = mainSession.post(url, data=postRaw, headers=req_header)
            print("Success! You can check out @:", end='')
            print(getPosts.findValue('div class="error_return"><a href="', response.content))
    else:
        postRaw = getPosts.getPosts(mainSession.cookies, ex_id)
        url = "http://dzdq.hustp.com/index.php?m=Exercises&a=show_answer"
        req_header = {
            "User-Agent""": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 "
                            "Safari/537.36",
            "Content-Type": "application/x-www-form-urlencoded"
        }
        response = mainSession.post(url, data=postRaw, headers=req_header)
        print("Success! You can check out @:", end='')
        print(getPosts.findValue('div class="error_return"><a href="', response.content))
        mainSession.close()
    os.system('pause')
