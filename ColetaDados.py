from selenium.webdriver import Firefox
from time import sleep

url = "https://br.investing.com/equities/via-varejo-sa"

navegado = Firefox()
navegado.get(url)

#esperar 3 segundos antes de procurar outro elemento
sleep(3)

#procurar elemento
a = navegado.find_element_by_id('last_last')

print(f' valor da acao: {a.text}')

#finalizar apos busca
navegado.quit()