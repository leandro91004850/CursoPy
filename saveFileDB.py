import mysql.connector
from time import sleep
from selenium.webdriver import Firefox

# faz a busca
url = "https://br.investing.com/indices/us-30-futures"
endereco = Firefox()
endereco.get(url)

endereco.refresh()

lopps = 10
rodadas = 1

mysql = mysql.connector.connect(
    host="192.168.1.20",
    user="leandro",
    passwd="",
    database="cursoPY"
)

mycursor = mysql.cursor()

while(rodadas <= lopps):
    sleep(3)
    endereco.refresh()
    # imprimi o resultado
    acao = endereco.find_element_by_xpath('//*[@id="last_last"]')
    acaoConvert = acao.text
    print(f'resultado: {acaoConvert}')

    nome = "Dow Jones"

    sql = "INSERT INTO acoes (nome, papel) VALUES (%s, %s)"
    val = (acaoConvert, nome)

    mycursor.execute(sql, val)

    mysql.commit()
    print(mycursor.rowcount, "record inserted.")
    lopps = lopps + 1

endereco.quit()
