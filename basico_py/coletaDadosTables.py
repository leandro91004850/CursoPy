from selenium import webdriver
from time import sleep

#acesso o site
#http://jonathansoma.com/lede/foundations-2018/classes/selenium/scraping-supplement/
url = "http://192.168.1.50:8081/table.html"
driver = webdriver.Chrome()
driver.get(url)



sleep(5)
coletaAtivo = driver.find_element_by_tag_name('table')
coletaTR = coletaAtivo.find_elements_by_tag_name('tr')


for value in coletaTR:
        coletaTD = value.find_elements_by_tag_name('td')
        print(coletaTD[0].text)
        print(coletaTD[1].text)
        print(coletaTD[2].text)
        

