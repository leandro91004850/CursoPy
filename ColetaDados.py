import json

from selenium.webdriver import Firefox
from time import sleep
from pprint import pprint

browser = Firefox()
browser.get("https://crane-technology.herokuapp.com/conteudos")
resultado = {}

def get_link(browser, elemento):
    element = browser.find_element_by_tag_name(elemento)
    ancoras = element.find_elements_by_tag_name('h1')
    for acora in ancoras:
        resultado[acora.text] = acora.get_attribute('href')
    return resultado

sleep(2)


pprint(get_link(browser, 'main'))

# gravar arquivo
gravando_json = json.dumps(resultado, indent=1)
with open("crane.json", "w") as outfile:
    outfile.write(gravando_json)

#finalizar apos busca
browser.quit()

