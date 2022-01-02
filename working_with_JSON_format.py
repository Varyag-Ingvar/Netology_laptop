import json
from pprint import pprint
from random import randint
from datetime import datetime

str_json = """{
    "response": {
        "count": 5939864,
        "items": [
            {
                "id": 399704992,
                "first_name": "Данил",
                "last_name": "Данилов",
                "can_access_closed": true,
                "is_closed": false
            },
            {
                "id": 138314261,
                "first_name": "Игорь",
                "last_name": "Брагинец",
                "can_access_closed": true,
                "is_closed": false
                
            }
        ]
    }
}"""

print(type(str_json))

data = json.loads(str_json)
print(type(data))
# pprint(data['response']['items'])

# for item in data['response']['items']:
#     print(item['first_name'], item['last_name'])

for item in data['response']['items']:
    del item['id']
    item['likes'] = randint(100, 200)
    item['date'] = datetime.now().strftime('%d.%m.%y')
pprint(data['response']['items'])
print('------------------------')

new_json = json.dumps(data, indent=2, ensure_ascii=False)
print(new_json)
print('------------------------------')

with open('my_json', 'w') as file:
    json.dump(data, file, indent=3)

with open('my_json', 'r') as file:
    data_1 = json.load(file)
pprint(data_1)