import mysql.connector

from selenium.webdriver import Firefox

# faz a busca
url = "https://br.investing.com/equities/via-varejo-sa-historical-data"
endereco = Firefox()
endereco.get(url)


# imprimi o resultado
acao = endereco.find_element_by_xpath('/html/body/div[5]/section/div[1]/h1')
acaoConvert = acao.text
print(f'resultado: {acaoConvert}')

nomes = "leandro"



mysql =mysql.connector.connect(
    host="192.168.1.20",
    user="leandro",
    passwd="",
    database="cursoPY"
)
mycursor = mysql.cursor()

sql = "INSERT INTO python (name, address) VALUES (%s, %s)"
val = (acaoConvert, nomes)

mycursor.execute(sql, val)

mysql.commit()
print(mycursor.rowcount, "record inserted.")

