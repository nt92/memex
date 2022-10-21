import sqlite3


class Database:
    def __init__(self, dbname="./db/records.db"):
        self.dbname = dbname
        self.conn = sqlite3.connect(dbname)
        self.setup()

    def execute_query(self, query, query_args=None, commit=False):
        """Executes the SQL query 'query'. Commits the connection
           if the commit flag is set"""
        try:
            cursor = self.conn.cursor()
            if query_args:
                if type(query_args) != tuple:
                    query_args = (query_args,)
                cursor.execute(query, query_args)
            else:
                cursor.execute(query)
            if commit:
                self.conn.commit()
            return cursor.fetchall()
        except Exception as e:
            print("Exception occured while executing Query: {}".format(query))
            print(e)
            return False

    def setup(self):
        """Creates the tables required for the database"""
        setup_query = """
        CREATE VIRTUAL TABLE IF NOT EXISTS records USING fts5(
            content,
        );
        """
        self.execute_query(setup_query, commit=True)
