from database.DB_connect import DBConnect



class DAO:
    def __init__(self):
        pass

    @staticmethod
    def getAllNazioni():
        cnx=DBConnect.get_connection()
        cursor=cnx.cursor(dictionary=False)

        query=""""""
        cursor.execute(query)

        risultato=[]
        for a in cursor:
            risultato.append(a[0])

        cursor.close()
        cnx.close()
        return risultato
