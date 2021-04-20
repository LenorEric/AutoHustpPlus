import requests


def getID(ex_id=""):
    if ex_id == "":
        print("Exercise_ID: ", end="")
        ex_id = input()
    return ex_id


def findValue(identi, content):
    content = str(content)
    content = content[content.find(identi) + len(identi):]
    content = content[:content.find('"')]
    return content


def getPosts(mainCookies, ex_id=""):
    ex_id = getID(ex_id)
    session = requests.session()
    url = "http://dzdq.hustp.com/index.php?m=Exercises&a=exercises_detail&id=" + str(ex_id)
    formData = {}
    req_header = {
        "User-Agent""": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 "
                        "Safari/537.36",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    session.cookies = mainCookies
    response = session.post(url, headers=req_header, data=formData)
    session.close()
    if response.status_code == 200:
        content = str(response.content)
        allcount = findValue('name="allcount" id="allcount" value="', content)
        teacherID = findValue('name="teacher_id" value="', content)
        op_id = findValue('name="op_id"  value="', content)
        op_type = findValue('name="op_type"  value="', content)
        mind_id = ''
        op_str = ''
        for i in range(int(allcount)-1):
            op_str += '1,'
        op_str += '1'
        post_raw = {
            "exercises_id": ex_id,
            "allcount": allcount,
            "teacher_id": teacherID,
            "op_str": op_str,
            "op_id": op_id,
            "op_type": op_type,
            "mind_id": mind_id
        }
        return post_raw
    else:
        print("Failed, try again later or report")
        return "Get Post Error"


if __name__ == '__main__':
    print("This can be only imported")
