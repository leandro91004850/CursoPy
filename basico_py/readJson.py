

import json

# Opening JSON file
f = open('crane.json', )

#carrega arquivo
data = json.load(f)

#percorre arquivo e apresenta resultado
for i in data:
    print(i)

f.close()
