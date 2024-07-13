from time import sleep

from selenium.webdriver import Firefox

url = "https://crane-technology.herokuapp.com/conteudos"

navegado = Firefox()
navegado.get(url)

searchBox = navegado.find_element_by_xpath('//*[@id="butao"]/img')
searchBox.click()

prenchimento1 = navegado.find_element_by_xpath('//*[@id="recipient-name"]')
preencher = input("digite: ")
prenchimento1.send_keys(preencher)

