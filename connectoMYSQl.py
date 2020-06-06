import mysql.connector

mysql =mysql.connector.connect(
    host="192.168.1.20",
    user="leandro",
    passwd="sua-senha",
    database="cursoPY"
)

mycursor = mysql.cursor()

sql = "INSERT INTO python (name, address) VALUES (%s, %s)"
val = ("John", "Highway 26")

mycursor.execute(sql, val)

mysql.commit()

print(mycursor.rowcount, "record inserted.")
