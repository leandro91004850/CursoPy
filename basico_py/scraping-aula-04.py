from selenium.webdriver import Firefox
from urllib.parse import  urlparse
from time import sleep
from pprint import pprint

browser = Firefox()
browser.get("https://selenium.dunossauro.live/aula_04.html")

def get_link(browser, elemento):
    resultado = {}
    element = browser.find_element_by_tag_name(elemento)
    ancoras = element.find_elements_by_tag_name('a')
    for acora in ancoras:
        resultado[acora.text] = acora.get_attribute('href')
    return resultado

sleep(2)


pprint(get_link(browser, 'aside'))


#main = browser.find_element_by_tag_name('main')
