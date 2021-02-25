import mysql.connector
from mysql.connector import errorcode
from env import set_env
import os

set_env()


class MySqlDb:
    def __init__(self, db_name):
        self.db_name = db_name
        self.conn = self.mysql_connect()
        self.table = ""

    def create_db(self, db_name):
        # CREATE DATABASE IF NOT EXISTS `pythonlogin` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci USE `pythonlogin`;
        pass

    def mysql_connect(self):
        try:
            cnx = mysql.connector.connect(user=os.getenv('MYSQL_USER'), password=os.getenv(
                'MYSQL_PASS'), host=os.getenv('MYSQL_HOST'), database=self.db_name)
            print("Connected")
            return cnx
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)
                # cnx.close()

    def create_table(self, table_name: str):
        c = self.conn.cursor()
        self.table = table_name
        SQL_QUERY = f"""CREATE TABLE IF NOT EXISTS {self.table} (
        id_cours INTEGER PRIMARY KEY AUTO_INCREMENT,
        title VARCHAR(250),
        lang VARCHAR(250),
        author VARCHAR(250),
        rate VARCHAR(250),
        enrolled VARCHAR(250),
        price VARCHAR(250),
        link VARCHAR(250)) ;"""
        c.execute(SQL_QUERY)
        self.conn.commit()
        print("Table " + table_name + " created")

    # Insert some users into our database
    def insert(self, data: list):
        c = self.conn.cursor()
        if data != "":
            query = """REPLACE INTO {} VALUES ({}, "{}", "{}", "{}", "{}", "{}", "{}" , "{}");""".format(
                self.table, data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7])
            c.execute(query)
            self.conn.commit()

    def select(self, table):
        c = self.conn.cursor(dictionary=True)
        c.execute("SELECT * FROM {}".format(table))
        # Store + print the fetched data
        result = c.fetchall()
        # Remember to save + close
        self.conn.commit()
        return result

    def exec(self, query):
        c = self.conn.cursor(dictionary=True)
        c.execute(query)
        # Store + print the fetched data
        result = c.fetchall()
        # Remember to save + close
        self.conn.commit()
        return result
