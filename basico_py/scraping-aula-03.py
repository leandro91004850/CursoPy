from selenium.webdriver import Firefox
from time import sleep

def find_by_text(browser, tag, text):

    elementos = browser.find_elements_by_tag_name(tag)

    for elemento in elementos:
        if elemento.text == text:
            return elemento

browser = Firefox()
browser.get("https://selenium.dunossauro.live/aula_04_b.html")

nome_das_caixas = ['um', 'dois', 'tres', 'quatro']


for texto in nome_das_caixas:
    find_by_text(browser, 'div', texto).click()


for nome in nome_das_caixas:
    sleep(0.2)
    browser.back()

for nome in nome_das_caixas:
    sleep(0.2)
    browser.forward()