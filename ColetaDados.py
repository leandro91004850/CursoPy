import json

from selenium.webdriver import Firefox
from time import sleep

url = "https://crane-technology.herokuapp.com/conteudos"

navegado = Firefox()
navegado.get(url)

#esperar 3 segundos antes de procurar outro elemento
sleep(3)

a = navegado.find_element_by_id('h3-texto')

print(f' valor da acao: {a.text}')
gravando = a.text

# gravar arquivo
gravando_json = json.dumps(gravando, indent=1)
with open("crane.json", "w") as outfile:
    outfile.write(gravando_json)

#finalizar apos busca
navegado.quit()

