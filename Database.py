import sqlite3


class DBManager:
    """
    A class to manage SQLite database operations.

    Manages SQLite database operations for user authentication and data storage.
    Handles connection, query execution, user table management, and authentication.
    Uses SQLite3 for database interactions.

    Author: Elmira Pour
    Timestamp: 1717701765.2003505

    Attributes:
        dbname (str): Name of the SQLite database file.
        password (str, optional): Password for the database, if applicable.
        conn (sqlite3.Connection): SQLite database connection object.
        cursor (sqlite3.Cursor): Cursor object for executing SQL queries.

    Methods:
        connect(): Establishes a connection to the SQLite database.
        disconnect(): Closes the connection to the SQLite database.
        execute_query(query, params=()): Executes a query that does not return data.
        execute_select_query(query, params=()): Executes a SELECT query that returns data.
        create_user_table(): Creates 'users' table if it does not exist.
        db_save_user(username, password, name, email, mobile, birthday): Saves user data into the 'users' table.
        db_authenticate_user(username, password): Authenticates user against the 'users' table.

    Example:
        # Usage example
        with DBManager('my_database.db') as db:
            db.create_user_table()
            db.db_save_user('john_doe', 'password123', 'John Doe', 'john.doe@email.com', '1234567890', '1990-01-01')
            authenticated = db.db_authenticate_user('john_doe', 'password123')
            print("Authentication successful!" if authenticated else "Authentication failed.")
    """

    def __init__(self, db_name, db_password=None):
        """
        Initialize the DBManager instance.

        :param db_name: Name of the SQLite database file.
        :param db_password: Optional password for the database.
        """
        self.dbname = db_name
        self.password = db_password
        self.conn = None
        self.cursor = None

    @property
    def version(self):
        """
        Get the version of the DBManager class.

        :return: A string representing the version.
        """
        return f"v1.0"  # The current version of the DBManager class

    def connect(self):
        """
        Establish a connection to the SQLite database.
        """
        try:
            self.conn = sqlite3.connect(self.dbname)
            self.cursor = self.conn.cursor()
            if self.password:
                self.cursor.execute(f"PRAGMA key='{self.password}'")
        except sqlite3.Error as e:
            print(f"Error connecting to database: {e}")

    def disconnect(self):
        """
        Close the connection to the SQLite database.
        """
        try:
            if self.conn:
                self.conn.close()
        except sqlite3.Error as e:
            print(f"Error disconnecting from database: {e}")
        finally:
            self.conn = None
            self.cursor = None

    def execute_query(self, query, params=()):
        """
        Execute a query that does not return data (e.g., INSERT, UPDATE, DELETE).

        :param query: SQL query to execute.
        :param params: Optional parameters for the query.
        """
        try:
            self.cursor.execute(query, params)
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Error executing query: {e}")

    def execute_select_query(self, query, params=()):
        """
        Execute a SELECT query that returns data.

        :param query: SQL SELECT query to execute.
        :param params: Optional parameters for the query.
        :return: Result set of the query.
        """
        try:
            self.cursor.execute(query, params)
            return self.cursor.fetchall()
        except sqlite3.Error as e:
            print(f"Error executing SELECT query: {e}")
            return None

    def create_user_table(self):
        """
        Create 'users' table if it does not exist.
        """
        create_table_query = ('\n'
                              '            CREATE TABLE IF NOT EXISTS users (\n'
                              '                id INTEGER PRIMARY KEY AUTOINCREMENT,\n'
                              '                username TEXT NOT NULL,\n'
                              '                password TEXT NOT NULL,\n'
                              '                name TEXT,\n'
                              '                email TEXT,\n'
                              '                mobile TEXT,\n'
                              '                birthday TEXT\n'
                              '            )\n'
                              '        ')
        self.execute_query(create_table_query)

    def db_save_user(self, username, password, name, email, mobile, birthday):
        """
        Save user data into the 'users' table.

        :param username: Username of the user.
        :param password: Password of the user.
        :param name: Name of the user.
        :param email: Email address of the user.
        :param mobile: Mobile number of the user.
        :param birthday: Birthday of the user.
        """
        insert_query = ('\n'
                        '            INSERT INTO users (username, password, name, email, mobile, birthday)\n'
                        '            VALUES (?, ?, ?, ?, ?, ?)\n'
                        '        ')
        self.execute_query(insert_query, (username, password, name, email, mobile, birthday))
        print(f"User '{username}' successfully saved.")

    def db_authenticate_user(self, username, password):
        """
        Authenticate user against the 'users' table.

        :param username: Username provided by the user.
        :param password: Password provided by the user.
        :return: True if authentication succeeds, False otherwise.
        """
        select_query = ('\n'
                        '            SELECT username, password FROM users\n'
                        '            WHERE username = ? AND password = ?\n'
                        '        ')
        result = self.execute_select_query(select_query, (username, password))
        if result:
            return True
        else:
            return False

    def __enter__(self):
        """
        Context manager entry point. Establishes connection.
        """
        self.connect()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Context manager exit point. Closes connection.
        """
        self.disconnect()
