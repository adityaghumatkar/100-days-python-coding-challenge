import requests
from datetime import datetime

pixela_endpoint = "https://pixe.la/v1/users"
USERNAME = "adityaghumatkar"
TOKEN = "qwjsydghaj2k235hajh2l"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

response = requests.post(url=pixela_endpoint,json=user_params)
response.raise_for_status()
print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": "CyclingGraph",
    "unit": "km",
    "type": "float",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN.encode('utf-8')
}

graph_response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
graph_response.raise_for_status()
print(graph_response.text)

GRAPH_ID = "graph1"
pixel_creation_endpoint = f"{graph_endpoint}/{GRAPH_ID}"

today = datetime.now()

pixel_data = {
    "date": today.strftime("%Y%m%d"), # op => 20240714
    "quantity": "59.74"
}

response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
print(response.text)

update_endpoint = f"{pixel_creation_endpoint}/{today.strftime("%Y%m%d")}"

new_pixel_data = {
    "quantity": "4.5"
}

res = requests.put(url=update_endpoint, json= new_pixel_data, headers=headers)
print(res.text)

delete_endpoint = f"{pixel_creation_endpoint}/{today.strftime("%Y%m%d")}"
res = requests.delete(url=update_endpoint, headers=headers)
print(res.text)