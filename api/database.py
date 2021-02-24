import logging
import mysql.connector
from mysql.connector import Error

logging.basicConfig(filename='log.txt', encoding='utf-8', level=logging.DEBUG,format='%(asctime)s %(levelname)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

def reset_logfile(logfile_path):
    ### Reset du fichier log
    my_txt_file= open(logfile_path, "r+")    
    # to erase all data  
    my_txt_file.truncate() 
    # to close file
    my_txt_file.close() 

class Create_and_set_database():

    def __init__(self):
        self.conn = mysql.connector.connect(host='dbserver',
                                user='root',
                                password='123',
                                )

    def createDB(self):
        self.conn = mysql.connector.connect(host='dbserver',
                                user='root',
                                password='123',
                                )
        try:
            sql_query = self.conn.cursor()

            #Création de la table en argument
            sql_query.execute(f"CREATE DATABASE IF NOT EXISTS DB_LEARNING")    

            logging.info("[MYSQL] database  %s has been successfully created ")
        except Error as e :
            logging.warning("[MYSQL] message error:  %s", (e))

setDB = Create_and_set_database()
setDB.createDB()

