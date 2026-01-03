import os
import pyodbc

class Database() :
    # Koneksi ke database
    def get_connection(self):
        connection_string = (
            f"Driver={{ODBC Driver 18 for SQL Server}};"
            f"Server={os.environ.get('DB_SERVER')};"
            f"Database={os.environ.get('DB_DATABASE')};"
            f"UID={os.environ.get('DB_USERNAME')};"
            f"PWD={os.environ.get('DB_PASSWORD')};"
            "Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;"
        )

        return pyodbc.connect(connection_string)

    # Test datavase
    def db_test(self):
        try :
            connection = self.get_connection()
            cursor = connection.cursor()
            cursor.execute("SELECT @@VERSION")
            row = cursor.fetchone()
            connection.close()
            return f"Berhasil Connect ke Database Versi Database: {row[0]}"
        
        except Exception as error:
            return f"Gagal Connect ke Database </h1> </h2> Pesan Error : {str(error)}"
