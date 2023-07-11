import sqlite3

class Database():
    def __init__(self, db_path):
        self.db_path = db_path
        self.con = sqlite3.connect(self.db_path)
        self.cur = self.con.cursor()

    def get_cursor(self):
        return self.cur

    def insert_data(self, plate_number, entry_time ,username , stiker):
        self.cur.execute('INSERT INTO VALUE(?, ?, ?, ?)', (plate_number,entry_time, username, stiker))

    def get_enter_time(self, plate_number):
        self.cur.execute('SELECT ENTER_TIME FROM PARKING WHERE PLATE_NUMBER == "?"',(plate_number))
        return self.cur.fetchone()
    
    def get_sticker(self, plate_number):
        self.cur.execute('SELECT STICKER FROM PARKING WHERE PLATE_NUMBER == "?"', (plate_number))
        return self.cur.fetchone()
    
    def check_user_database(self, plate_number):
        self.cur.execute('SELECT NAME FROM USER WHERE PLATE_NUMBEr == "?"', (plate_number))
        return self.cur.fetchone()
        

        

    




