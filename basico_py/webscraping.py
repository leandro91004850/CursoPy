from selenium.webdriver import Firefox

browser = Firefox()

browser.get("https://selenium.dunossauro.live/aula_04_a.html")

#conta quantos li tem no meu html
contaLI = len(browser.find_elements_by_tag_name('li'))
print(contaLI)

lista_n_ordenada = browser.find_element_by_tag_name('ul')
contaUL = len(browser.find_elements_by_tag_name('ul'))
print('Quantidades de Ul:', contaUL)

#coletando o elemento A dentro de LI
lis = lista_n_ordenada.find_elements_by_tag_name('li')
lis[0].find_element_by_tag_name('a')
print(lis[0].find_element_by_tag_name('a').text)