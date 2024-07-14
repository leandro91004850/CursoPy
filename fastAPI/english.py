import mysql.connector as sql

class English:
        
    def english_learning():
        mysql = sql.connect(
            host="",
            port="3306",
            user="leandro",
            passwd="",
            database="simulado"
        )

        try:
            cursor = mysql.cursor()
            cursor.execute("SELECT * FROM english_words")
            result = cursor.fetchall()
            mysql.commit()
            cursor.close()
            for row in result:
                print(row)
        except Exception as e:
            print("Error: ", e)
        
        return "English Learning"