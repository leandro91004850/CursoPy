from selenium.webdriver import Firefox
from time import sleep

url = "https://crane-technology.herokuapp.com/conteudos"

navegado = Firefox()
navegado.get(url)

#esperar 3 segundos antes de procurar outro elemento
sleep(3)


for tabela in range(1, 550):
    # procurar elemento
    a = navegado.find_elements_by_id('h3-texto')
    print(f' valor da acao: {a[tabela].text}')


#finalizar apos busca
navegado.quit()

