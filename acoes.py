import json
from time import sleep
from selenium.webdriver import Firefox

#faz a busca
url = "https://br.investing.com/equities/via-varejo-sa-historical-data"
endereco = Firefox()
endereco.get(url)

# clica no elemento
searchBox = endereco.find_element_by_xpath('//*[@id="column-content"]/div[3]')
searchBox.click()

# apaga e inserir a data requisitada
emitirRelatorio = endereco.find_element_by_xpath('//*[@id="startDate"]').clear()
insindoData = endereco.find_element_by_xpath('//*[@id="startDate"]')
insindoData.send_keys('20/01/2000')

# emitir o relatorio
clicando = endereco.find_element_by_xpath('//*[@id="applyBtn"]')
clicando.click()

# imprimi o resultado
a = endereco.find_element_by_xpath('//*[@id="last_last"]')
print(f'resultado: {a.text}')

# grava o resultado
gravador = a.text
json_gravar = json.dumps(gravador, indent=1)
with open("testes.json", "w") as outfile:
    outfile.write(json_gravar)


# espera o time e encerra o processo
sleep(3)
endereco.quit()
