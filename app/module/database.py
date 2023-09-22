'''
Created on Fri Sep 22, 2017

@author: Aristoteles
'''

import pymysql


class Database:
    def connect(self):
        return pymysql.connect(host="db", user="root", password="root", database="ebreakfast_db")

    def read(self, id):
        con = Database.connect(self)
        cursor = con.cursor()

        try:
            if id == None:
                cursor.execute("SELECT * FROM customers order by id asc")
            else:
                cursor.execute(
                    "SELECT * FROM customers where id = '%s' order by name asc", (id,))

            return cursor.fetchall()
        except:
            return ()
        finally:
            con.close()

    def insert(self, data):
        con = Database.connect(self)
        cursor = con.cursor()

        try:
            cursor.execute("INSERT INTO customers(id, email, phone, birthdate, address_fk) VALUES(%s, %s, %s, %s, 1)",
                           (data['id'], data['email'], data['phone'], data['birthdate'],))
            con.commit()

            return True
        except:
            con.rollback()

            return False
        finally:
            con.close()

    def update(self, id, data):
        con = Database.connect(self)
        cursor = con.cursor()

        try:
            cursor.execute("UPDATE phone_book set name = %s, phone = %s, address = %s where id = %s",
                           (data['name'], data['phone'], data['address'], id,))
            con.commit()

            return True
        except:
            con.rollback()

            return False
        finally:
            con.close()

    def delete(self, id):
        con = Database.connect(self)
        cursor = con.cursor()

        try:
            cursor.execute("DELETE FROM phone_book where id = %s", (id,))
            con.commit()

            return True
        except:
            con.rollback()

            return False
        finally:
            con.close()
