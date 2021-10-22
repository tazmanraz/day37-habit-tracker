import requests
from datetime import datetime

pixela_endpoint = "https://pixe.la/v1/users"
USERNAME = "XXX"
TOKEN = "XXX"
GRAPH_ID = "graph1"


user_params={
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService":"yes",
    "notMinor":"yes",
}

# response = requests.post(url=pixela_endpoint, json = user_params)
#
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Coding Modules",
    "unit": "Exercises",
    "type": "int",
    "color": "shibafu"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url = graph_endpoint, json = graph_config, headers=headers)
# print(response.text)

# Adding a pixel

add_endpoint = f"{graph_endpoint}/{GRAPH_ID}"

today = datetime.now().strftime("%Y%m%d")

add_config = {
    "date": "20210130",
    "quantity": "5",
}

# response = requests.post(url = add_endpoint, json = add_config, headers=headers)
# print(response.text)

# PUT response (updating values)

update_endpoint = f"{add_endpoint}/20210130"

update_config = {
    "quantity": "2",
}

response = requests.put(url=update_endpoint, json=update_config, headers=headers)
print(response.text)

# DELETE pixel

delete_endpoint = f"{update_endpoint}"

# update_config = {
#     "quantity": "2",
# }

response = requests.delete(url=delete_endpoint, headers=headers)
print(response.text)