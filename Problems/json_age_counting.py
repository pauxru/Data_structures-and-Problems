import requests
r = requests.get('https://coderbyte.com/api/challenges/json/age-counting')
raw_data = r.json()['data']
# print(raw_data)
key_age = []
for data in raw_data.split(", "):
    if "age=" in data:
        age = data.replace("age=", "")
        key_age.append(int(age))

count = len([x for x in key_age if x > 50])
print(count)
