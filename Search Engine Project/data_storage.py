import sqlite3
import pandas as pd

class DBConnec():
    def __innit__(self):
        self.con = sqlite3.connect("search_history.db")
        self.setupTables()
        
    def setupTables(self):
        cursor = self.con.cursor()
        results_table = r"""
            CREATE TABLE IF NOT EXISTS history (
                id INTEGER PRIMARY KEY,
                query TEXT,
                rank INTEGER,
                link TEXT,
                title TEXT,
                created DATETIME,
                UNIQUE(query, link)
            )
        """
        cursor.execute(results_table)
        self.con.commit()
        
    def results(self, query):
        df = pd.read_sql(f"select * from history where query='{query}'", self.con)
        return df
    
    def insert_more(self, value):
        cursor = self.con.cursor()
        try:
            cursor.execute('INSERT INTO history (query, rank, link, title, created) VALUE(?,?,?,?,?)', value)
            self.con.commit()
        except sqlite3.IntegrityError:
            pass
        cursor.close()
        