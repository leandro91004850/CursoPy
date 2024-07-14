import mysql.connector as sql
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

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
            
            cursor.execute("SELECT * FROM english_words WHERE acertos <= 4 OR acertos IS NULL ORDER BY RAND() LIMIT 1")
            result = cursor.fetchall()
            
            cursor.execute("SELECT * FROM english_words ORDER BY RAND() LIMIT 4")
            result2 = cursor.fetchall()

            mysql.commit()
            cursor.close()
            all_rows = []
            for row in result:
                portugues_alternativas = []
                for row2 in result2:
                    portugues_alternativas.append(row2[2])                   
                    
                row_dict = dict(zip(cursor.column_names, row))
                all_rows.append(row_dict)
                
                for row_dict in all_rows:
                    row_dict['portugues_alternativas'] = portugues_alternativas
            return JSONResponse(content=jsonable_encoder(all_rows))
        
        except Exception as e:
            print("Error: ", e)
        
        return "English Learning"