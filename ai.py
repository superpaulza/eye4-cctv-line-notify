import requests
from PIL import Image
from datetime import datetime

url = 'https://notify-api.line.me/api/notify'
token = 'PnZWJcOXC7fJXfxGanEpYRuFnNC7vmROw7GJVaMUL0a'
headers = {'content-type':'application/x-www-form-urlencoded','Authorization':'Bearer '+token}

image_data = open("crop.png","rb").read()
image = Image.open("crop.png").convert("RGB")
str = "There is "
ck = False
response = requests.post("http://localhost:80/v1/vision/detection",files={"image":image_data}).json()
#r = requests.post(url, headers=headers, data = {'message':"CCTV detected but just a stupid car!"})

for object in response["predictions"]:
    if object["label"] == "person" or object["label"] == "cat" or object["label"] == "dog":
        ck = True
        str+= object["label"] + ", "

if ck:
    str += " in front of a door right now!\n\n For more information please open Eye4 App!"
    r = requests.post(url, headers=headers, data={'message':"[Detected Alert] "+ str,'imageThumbnail':"http://pankrub.ddns.net/pic/001.jpg",'imageFullsize':"http://pankrub.ddns.net/pic/001.jpg"})