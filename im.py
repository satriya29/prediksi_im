import requests
import json
import math
import datetime
import schedule
import time
from datetime import datetime, timedelta

url = "https://api.im2017.com/api/login"
payload = {'account': '6289666918924', 'password': 'ken123'}
response = requests.post(url, data=payload)

json_data = response.json()

# token = json_data['token']

jsonstring = json.dumps(json_data ,indent=3)

token = json_data['data']['token']

# set up the API endpoint URL
urlw = "https://api.im2017.com/api/game/guess_odd?page=1&limit=50&type=24"

# set up the request headers with the authorization token
headers = {
    "Authorization": f"Bearer {token}",
}

# send the GET request to the API endpoint
responsew = requests.get(urlw, headers=headers)

# get the JSON data from the response
data = responsew.json()

jsonstring = json.dumps(data ,indent=3)


numbers = [item['number'] for item in data['data'][:1]]
number2 = [item['number'] for item in data['data'][:2]]
logika = numbers+number2[-1:]
itungan = sum(logika)/95 *10
# print(itungan)
x_rounded = math.floor(itungan)
# print(x_rounded)

waktu = [item['time'] for item in data['data'][:1]]
results = [item['result'] for item in data['data'][:1]]
print('keluaran : ',numbers ,waktu,results)  # output: [31, 34]
# print("next result :",x_rounded) 

def ganjil_genap(x):
    if x % 2 == 0:
        print( "next rest  genap : " , x)
    else:
        print( "next rest ganjil : " , x)



# print(waktu_2_menit_lagi)
ganjil_genap(x_rounded)