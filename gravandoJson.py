import json

# Data to be written
gravacao = {

    "name": "leandro foda",
    "rollno": 56,
    "cgpa": 8.6,
    "phonenumber": "9976770500"

}

# Serializing json
json_object = json.dumps(gravacao, indent=4)

# Writing to sample.json
with open("arquivo.json", "w") as outfile:
    outfile.write(json_object)