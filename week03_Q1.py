targetUrl = "https://padax.github.io/taipei-day-trip-resources/taipei-attractions.json"

# target stitle
# target longitude
# target latitude
# target file

import urllib.request as request
import json

with request.urlopen(targetUrl) as response:
    #  load 資料成 json格式
    data = json.load(response)

target_list = data["result"]["results"]

with open("data.txt", "w", encoding= "utf-8") as file:
    for target in target_list:
        proto_url = target["file"]

        # 不知道為何split後的[0]沒有資料，但[1]就抓到正確資料 ← 想通了，在split http的狀況下，因為一開始就是http，所以[0]就變為空白內容
        first_url = proto_url.split("http://")[1]
        first_url_complete = "http://" + first_url

        file.writelines([target["stitle"],",", target["longitude"],",", target["latitude"],",", first_url_complete +"\n"])


