from constantes import DB_HOSTNAME,DB_DATABASE,DB_PASSWORD,DB_USERNAME
#import constantes
import mysql.connector as db

def abrir_conexion():
    return db.connect(host=DB_HOSTNAME,
                      user=DB_USERNAME,
                      password=DB_PASSWORD,
                      database=DB_DATABASE)

if __name__ == "__main__":
    pass
