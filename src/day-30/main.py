# Error handling

try:
    file = open("no_file.txt")
    a_dictionary = {"key": "value"}
    print(a_dictionary["key"])
except FileNotFoundError:
    file = open("no_file.txt", "w")
except KeyError as error_message:
    print("the key does not exist")
else:
    content = file.read()
finally:
    file.close()

#JSON

import json
# write in json
new_data = dict(website=dict(email="aditya.ghumatkar@google.com", password="1234"), cost="$200")
with open("data.json", "w") as json_file:
    json.dump(new_data, json_file, indent=4)

# read json file
with open("data.json", "r") as json_file:
    data = json.load(json_file)
    print(data)

    # update json
    # update_data = dict(website=dict(email="ajinkya.ghumatkar@google.com", password="5678"), cost="$400")
    update_data = {
        "website": {
            "email": "ajinkya.ghumatkar@google.com",
            "password": "5678"
        },
        "cost": "$400"
    }
    data.update(update_data)

    print(data)

with open('data.json', "w") as file:
    json.dump(data,file, indent=4)