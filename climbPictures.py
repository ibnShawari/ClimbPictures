import os
import requests

url = "https://image.ijq.tv/201608/03/16-48-56-19-26.jpg"
root = "/Users/jinxin/Desktop/"
path = root + url.split('/')[-1]

try:
    if not os.path.exists(root):
        os.mkdir(root)
    if not os.path.exists(path):
        r = requests.get(url)
        with open(path, 'wb') as f:
            f.write(r.content)
            f.close()
            print("文件保存成功！")
    else:
        print("文件已经存在！")
except:
    print("爬取失败！")