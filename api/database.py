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
        self.createDB()
        self.conn = mysql.connector.connect(host='dbserver',
                                user='root',
                                database='DB_LEARNING',
                                password='123',
                                )

    def createDB(self):
        self.conn = mysql.connector.connect(host='dbserver',
                                user='root',
                                password='123',
                                )
        try:
            sql_query = self.conn.cursor()

            #Création de la en argument
            sql_query.execute(f"CREATE DATABASE IF NOT EXISTS DB_LEARNING")    

            logging.info("[MYSQL] database DB_LEARNING has been successfully created ")
        except Error as e :
            logging.warning("[MYSQL] message error:  %s", (e))
    
    def createTableCours(self):
        self.conn = mysql.connector.connect(host='dbserver',
                        user='root',
                        database='DB_LEARNING',
                        password='123',
                        )
        try:
            sql_query = self.conn.cursor()

            #Création de la table en argument
            sql_query.execute(f"DROP TABLE IF EXISTS COURS")    
            sql_query.execute(f"CREATE TABLE IF NOT EXISTS COURS (id_cours INT PRIMARY KEY NOT NULL AUTO_INCREMENT,name_cours VARCHAR(100) NOT NULL, code VARCHAR(100) NOT NULL)")
            logging.info("[MYSQL] table 'cours' has been successfully created ")
        except Error as e :
            logging.warning("[MYSQL] message error:  %s", (e))

    def createTableSpecialName(self,support_name) :
        self.conn = mysql.connector.connect(host='dbserver',
                        user='root',
                        database='DB_LEARNING',
                        password='123',
                        )
        try:
            sql_query = self.conn.cursor()

            #Création de la table en argument
            sql_query.execute(f"DROP TABLE IF EXISTS {support_name}")    
            sql_query.execute(f"""CREATE TABLE IF NOT EXISTS {support_name} (id_value INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
             link VARCHAR(100) NOT NULL,
             niveau VARCHAR(100) NOT NULL,
             titre VARCHAR(100) NOT NULL,
             description TEXT,
             tags VARCHAR(100) NOT NULL,
             rate INT NOT NULL)""")
            logging.info("[MYSQL] table  %s has been successfully created ", (support_name) )
        except Error as e :
            logging.warning("[MYSQL] message error:  %s", (e))   

reset_logfile("log.txt")
setDB = Create_and_set_database()
setDB.createTableCours()
setDB.createTableSpecialName("Python")
setDB.createTableSpecialName("Azure")


