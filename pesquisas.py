from time import sleep

from selenium.webdriver import Firefox

url = "https://www.google.com.br/"

pesquisas = 3
rodadas = 1

while(rodadas <= pesquisas):

    navegado = Firefox()
    navegado.get(url)

    searchBox = navegado.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input')
    searchBox.send_keys('mexico é muita droga')

    searchBox = navegado.find_element_by_xpath('/html/body/div/div[3]/form/div[2]/div[1]/div[3]/center/input[1]')
    searchBox.click()

    sleep(3)

    searchBox = navegado.find_element_by_xpath('/html/body/div[6]/div[2]/div[9]/div[1]/div[2]/div/div[2]/div[2]/div/div/div[1]/div/div[1]/a/h3')
    searchBox.click()
    rodadas = rodadas + 1