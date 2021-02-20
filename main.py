import json
import requests


response = requests.get("http://api.open-notify.org/astros.json")
print(response)
print(response.json())
print(response.json()["people"])
data = response.json()
print(data.__class__)
for value in data:
    print (value)
    # print(data[value].__class__)
    if isinstance(data[value], (list, tuple, dict)):
        for item in data[value]:
            print (item)
    if isinstance(data[value], (dict)):
        for value_key,value_value in value.iteritems():
            print (value_key,str(value_value))
# for item in response.json():
#     for data_item in item["people"]:
#         print (data_item['craft'], data_item['name'])