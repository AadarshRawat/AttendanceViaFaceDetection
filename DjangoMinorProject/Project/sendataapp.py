import json
import requests

def call():
    URL="http://127.0.0.1:8000/create"

    datatest=[{'rollnumber': '1929001', 'name': 'Aadarsh', 'lname': 'Rawat'}, {'rollnumber': '1929088', 'name': 'HARSH', 'lname': 'CHANDRA'}]
    #for post
    # for i in datatest:
    #     json_data=json.dumps(i)
    #     print('This is json data',json_data)
    #     r=requests.post(url=URL,data=json_data)
    #     data=r.json()
    #     print(data)
    #for put
    for i in datatest:
        json_data=json.dumps(i)
        print('This is json data',json_data)
        r=requests.put(url=URL,data=json_data)
        data=r.json()
        print(data)




# data={
#     'rollnumber':1929001,
#     'name':'Aadarsh',
#     'lname':'Rawat'
# }

# json_data=json.dumps(data)
# print('json_data=',json_data)
# r=requests.post(url=URL,data=json_data)

# data=r.json()

# print(data)