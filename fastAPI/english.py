import mysql.connector as sql
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

class English:

    @staticmethod
    def banco_dados():
        return sql.connect(
            host="",
            port="3306",
            user="leandro",
            passwd="",
            database="simulado"
        )    
    
    @staticmethod
    def english_learning():

        try:
            # Usando o bloco with para garantir que a conexão seja fechada automaticamente
            with English.banco_dados() as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM english_words WHERE acertos <= 4 OR acertos IS NULL ORDER BY RAND() LIMIT 1")
                result = cursor.fetchall()
                
                cursor.execute("SELECT * FROM english_words ORDER BY RAND() LIMIT 4")
                result2 = cursor.fetchall()

                # Não é necessário chamar commit em operações de leitura
                # conn.commit()
                all_rows = []
                for row in result:
                    portugues_alternativas = []
                    for row2 in result2:
                        if row2[2] not in portugues_alternativas:
                            portugues_alternativas.append(row2[2])

                    # Garantir que a tradução correta esteja sempre nas alternativas
                    if row[2] not in portugues_alternativas:
                        portugues_alternativas.append(row[2])

                    row_dict = dict(zip(cursor.column_names, row))
                    all_rows.append(row_dict)

                    for row_dict in all_rows:
                        row_dict['portugues_alternativas'] = portugues_alternativas

                return JSONResponse(content=jsonable_encoder(all_rows))
        
        except Exception as e:
            print("Error: ", e)
        
        return "English Learning"
    
    @staticmethod
    def update_item(item_id: str, traducao: str): # dist é um dicionário
        try:
            with English.banco_dados() as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM english_words WHERE id = %s", (item_id,))
                result = cursor.fetchall()
                status = "Error"
                for row in result:
                    if row[2].lower() == traducao.lower():
                         cursor.execute("UPDATE english_words SET acertos = acertos + 1 WHERE id = %s", (item_id,))
                         conn.commit()
                         status = "Success"
                    else:
                        cursor.execute("UPDATE english_words SET acertos = acertos - 1 WHERE id = %s", (item_id,))
                        conn.commit()

                return JSONResponse(content=jsonable_encoder({"status": status}))
        
        except Exception as e:
            print("Error: ", e)
        
        return "Update Item"

