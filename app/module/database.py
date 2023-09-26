'''
Created on Fri Sep 22, 2017

@author: Aristoteles
'''
import json

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
                # print(f"SELECT * FROM customers where id = '{id}'")
                cursor.execute(
                    f"SELECT * FROM customers where id = '{id}'")
                # cursor.execute("SELECT * FROM customers order by id asc")

            return cursor.fetchall()
        except:
            print(f'Error in reading Database', flush=True)
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
            print(f'Error in inserting Data: {json.dumps(data)}', flush=True)
            con.rollback()

            return False
        finally:
            con.close()

    def update(self, id, data):
        con = Database.connect(self)
        cursor = con.cursor()

        try:
            cursor.execute("UPDATE customers set email = %s, phone = %s, birthdate = %s where id = %s",
                           (data['id'], data['email'], data['phone'], data['birthdate'], id,))
            con.commit()

            return True
        except:
            print(f'Error in updating ID: {id}, Data: {json.dumps(data)}', flush=True)
            con.rollback()

            return False
        finally:
            con.close()

    def delete(self, id):
        con = Database.connect(self)
        cursor = con.cursor()

        try:
            cursor.execute(f"DELETE FROM customers where id = {id}")
            con.commit()

            return True
        except:
            print(f'Error in deleting ID: {id}', flush=True)
            con.rollback()

            return False
        finally:
            con.close()
