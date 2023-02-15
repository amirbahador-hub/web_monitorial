from web_monitorial.db import get_connection, stop_connection

class DBConnectionHandler():
    def __enter__(self):
        self.conn = get_connection()
        return self.conn

    def __exit__(self, exc_type,exc_value, exc_traceback):
        stop_connection(self.conn)
