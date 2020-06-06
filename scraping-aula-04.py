from selenium.webdriver import Firefox
from urllib.parse import  urlparse
from time import sleep

browser = Firefox()
browser.get("https://selenium.dunossauro.live/aula_04.html")

#url_parceada = urlparse(browser.current_url)

sleep(2)
aside = browser.find_element_by_tag_name('aside')
aside_acoras = aside.find_elements_by_tag_name('a')

for acora in aside_acoras:
    print(acora.text)
    print(acora.text, acora.get_attribute('href'))
    print('--------------------------------------------\n')