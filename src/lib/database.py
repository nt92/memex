import sqlite3


class Database:
    def __init__(self, dbname="./db/records.db"):
        self.dbname = dbname
        self.conn = sqlite3.connect(dbname)

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
            print("Exception occurred while executing Query: {}".format(query))
            print(e)
            return False

    def setup(self):
        """Creates the tables required for the database"""
        setup_query = """
        CREATE VIRTUAL TABLE IF NOT EXISTS records USING fts5(
            source,
            title,
            content,
            timestamp,
            link,
        );
        """
        self.execute_query(setup_query, commit=True)

    def reset(self):
        """Resets the database by dropping the tables"""
        reset_query = """
        DROP TABLE IF EXISTS records;
        """
        self.execute_query(reset_query, commit=True)

    def save_record(self, source, title, content, timestamp, link):
        """Saves the record to the database"""
        save_query = """
        INSERT INTO records VALUES (?, ?, ?, ?, ?);
        """
        self.execute_query(save_query, (source, title, content, timestamp, link), commit=True)

    def search(self, term):
        """Searches the database for the term"""
        search_query = """
        SELECT * FROM records WHERE content MATCH ? ORDER BY rank;
        """
        return self.execute_query(search_query, term)
