import json

from selenium.webdriver import Firefox
from time import sleep
from pprint import pprint
import mysql.connector


browser = Firefox()
browser.get("https://crane-technology.herokuapp.com/conteudos")
resultado = {}

nome = "maria"
cidade = "ocidental"

def get_link(browser, elemento):
    element = browser.find_element_by_tag_name(elemento)
    ancoras = element.find_elements_by_tag_name('h1')
    for acora in ancoras:
        resultado[acora.text] = acora.get_attribute('href')
    return resultado

sleep(2)


pprint(get_link(browser, 'main'))

# gravar arquivo
gravando_json = json.dumps(resultado, indent=1)
with open("crane.json", "w") as outfile:
    outfile.write(gravando_json)

#gravando MySql
mysql =mysql.connector.connect(
    host="192.168.1.20",
    user="leandro",
    passwd="",
    database="cursoPY"
)

mycursor = mysql.cursor()

sql = "INSERT INTO python (name, address) VALUES (%s, %s)"
val = (resultado, cidade)

mycursor.execute(sql, (val))

mysql.commit()
print(mycursor.rowcount, "record inserted.")


#finalizar apos busca
browser.quit()

