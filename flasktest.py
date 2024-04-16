import requests
import base64


api_url = "http://127.0.0.1:5000/image"


with open("images/baseball.jpg", 'rb')as img:
    string = base64.b64encode(img.read()).decode('utf-8')


res = requests.post(api_url, json = {'user_photo':string})
print(res.text)