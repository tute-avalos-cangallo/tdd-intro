from typing import List
import mysql.connector as db
#import constantes
from constantes import DB_HOSTNAME,DB_DATABASE,DB_PASSWORD,DB_USERNAME


def abrir_conexion() -> db.pooling.PooledMySQLConnection | db.MySQLConnection:
    return db.connect(host=DB_HOSTNAME,
                      user=DB_USERNAME,
                      password=DB_PASSWORD,
                      database=DB_DATABASE)

def consulta_generica(conn : db.MySQLConnection, consulta : str) -> List[db.connection.RowType]:
    cursor = conn.cursor(buffered=True)
    cursor.execute(consulta)
    return cursor.fetchall()

if __name__ == "__main__":
    conn = abrir_conexion()

    resultado = consulta_generica(conn, "SHOW TABLES")
    for row in resultado:
        print(row[0]) # <- se muestra la primera columna de las filas resultantes

    conn.close()
