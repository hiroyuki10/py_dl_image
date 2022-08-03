import urllib.request
import os

def download_image(url, file_name):
    path =  os.path.join("./" , file_name)
    if os.path.exists(path):
        print("-----------------")
        print(path)
        print(" -> path exist...")
        return False
    print("url")
    print(url)
    print("path")
    print(path)
    headers = {
            "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:47.0) Gecko/20100101 Firefox/47.0",
            }
    request = urllib.request.Request(url=url, headers=headers)
    response = urllib.request.urlopen(request).read()
    with open(file_name, mode="wb") as f:
            f.write(response)
    return True

str = ""
download_file(str, '%03d' % (0) + ".jpg" )
