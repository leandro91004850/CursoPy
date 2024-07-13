import mysql.connector

nomes = input("digite o nome: ")
cidade = input("digite a cidade: ")

mysql =mysql.connector.connect(
    host="192.168.1.20",
    user="leandro",
    passwd="",
    database="cursoPY"
)

mycursor = mysql.cursor()

sql = "INSERT INTO python (name, address) VALUES (%s, %s)"
val = (nomes, cidade)

mycursor.execute(sql, val)

mysql.commit()

print(mycursor.rowcount, "record inserted.")


