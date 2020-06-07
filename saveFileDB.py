import mysql.connector

from selenium.webdriver import Firefox

# faz a busca
url = "https://br.investing.com/equities/via-varejo-sa-historical-data"
endereco = Firefox()
endereco.get(url)


# imprimi o resultado
acao = endereco.find_element_by_xpath('//*[@id="last_last"]')
print(f'resultado: {acao.text}')


mysql =mysql.connector.connect(
    host="192.168.1.20",
    user="leandro",
    passwd="",
    database="cursoPY"
)

mycursor = mysql.cursor()

sql = "INSERT INTO scraping (raspagem) VALUES (%s)"
val = (acao)

mycursor.execute(sql, (val))

mysql.commit()

print(mycursor.rowcount, "record inserted.")
