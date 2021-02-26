import logging
import json
import mysql.connector
from mysql.connector import Error

logging.basicConfig(filename='log.txt', encoding='utf-8', level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')


def reset_logfile(logfile_path):
    # Reset du fichier log
    my_txt_file = open(logfile_path, "r+")
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

            # Création de la en argument
            sql_query.execute(f"CREATE DATABASE IF NOT EXISTS DB_LEARNING")

            logging.info(
                "[MYSQL] database DB_LEARNING has been successfully created ")
        except Error as e:
            logging.warning("[MYSQL] message error:  %s", (e))

    def createTableCours(self):
        self.conn = mysql.connector.connect(host='dbserver',
                                            user='root',
                                            database='DB_LEARNING',
                                            password='123',
                                            )
        try:
            sql_query = self.conn.cursor()

            # Création de la table en argument
            sql_query.execute(f"DROP TABLE IF EXISTS COURS")
            sql_query.execute(
                f"CREATE TABLE IF NOT EXISTS COURS (id_cours INT PRIMARY KEY NOT NULL AUTO_INCREMENT,name_cours VARCHAR(100) NOT NULL, code VARCHAR(100) NOT NULL)")
            logging.info(
                "[MYSQL] table 'cours' has been successfully created ")
        except Error as e:
            logging.warning("[MYSQL] message error:  %s", (e))

    def createTableSpecialName(self, course_name):
        self.conn = mysql.connector.connect(host='dbserver',
                                            user='root',
                                            database='DB_LEARNING',
                                            password='123',
                                            )
        try:
            sql_query = self.conn.cursor()

            # Création de la table en argument
            sql_query.execute(f"DROP TABLE IF EXISTS {course_name}")
            sql_query.execute(f"""CREATE TABLE IF NOT EXISTS {course_name} (id_value INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
             link VARCHAR(100) NOT NULL,
             niveau VARCHAR(100) NOT NULL,
             titre VARCHAR(100) NOT NULL,
             description TEXT,
             tags VARCHAR(100) NOT NULL,
             rate INT NOT NULL)""")
            logging.info(
                "[MYSQL] table  %s has been successfully created ", (course_name))
        except Error as e:
            logging.warning("[MYSQL] message error:  %s", (e))

    def fetchDATAfile(self, course_name):
        liste_link = []
        liste_level = []
        liste_title = []
        liste_desc = []
        liste_tags = []
        liste_rate = []
        with open('data_course.txt') as json_file:
            data = json.load(json_file)
            for i in range(0, len(data[course_name])):
                # pour add le link
                liste_link.append(data[course_name][i][1])
                # pour add le niveau
                liste_level.append(data[course_name][i][2])
                # pour add le title
                liste_title.append(data[course_name][i][3])
                # pour add la description
                liste_desc.append(data[course_name][i][4])
                # pour add les tags
                liste_tags.append(data[course_name][i][5])
                # pour add le rating
                liste_rate.append(data[course_name][i][6])
        self.full_course_info = list(
            zip(liste_link, liste_level, liste_title, liste_desc, liste_tags, liste_rate))
        return self.full_course_info

    def setIntoTableCourse(self, course_name, course_info):
        self.conn = mysql.connector.connect(host='dbserver',
                                            user='root',
                                            database='DB_LEARNING',
                                            password='123',
                                            )
        sql_query = self.conn.cursor()
        insert = f"INSERT INTO {course_name} (link, niveau, titre, description, tags, rate) VALUES (%s, %s, %s, %s, %s, %s);"
        value = course_info

        sql_query.executemany(insert, value)
        self.conn.commit()

    def select(self, table):
        c = self.conn.cursor(dictionary=True)
        c.execute("SELECT * FROM {}".format(table))
        # Store + print the fetched data
        result = c.fetchall()
        # Remember to save + close
        self.conn.commit()
        return result

    # Cette methode va inserer un nouveau video dans la table de cours qui corresponde
    def add_new_video(self, course_name, course_info):
        c = self.conn.cursor()
        query = f"""INSERT INTO {course_name} (link, niveau, titre, description, tags, rate) VALUES (%s, %s, %s, %s, %s, %s);""" % (
            course_info)
        c.execute(query)
        self.conn.commit()

    def select_from_tag(self,custom_tag):
        c = self.conn.cursor(dictionary=True)
        #select * from PYTHON where tags like '%super%';
        c.execute(f"SELECT link FROM PYTHON WHERE tags like '%{custom_tag}%';")
        # Store + print the fetched data
        result = c.fetchall()

        c.execute(f"SELECT link FROM AZURE WHERE tags like '%{custom_tag}%';")
        # Store + print the fetched data
        result2 = c.fetchall()

        c.execute(f"SELECT link FROM SRE WHERE tags like '%{custom_tag}%';")
        # Store + print the fetched data
        result3 = c.fetchall()
        # Remember to save + close
        self.conn.commit()
        final_result = result + result2 + result3
        return final_result


def main():
    reset_logfile("log.txt")
    setDB = Create_and_set_database()
    setDB.createTableCours()
    setDB.createTableSpecialName("PYTHON")
    setDB.createTableSpecialName("AZURE")
    setDB.createTableSpecialName("SRE")
    setDB.setIntoTableCourse("PYTHON", setDB.fetchDATAfile("python"))
    setDB.setIntoTableCourse("AZURE", setDB.fetchDATAfile("azure"))
    setDB.setIntoTableCourse("SRE", setDB.fetchDATAfile("sre"))


main()
