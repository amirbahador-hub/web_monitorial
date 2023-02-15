import psycopg2
import logging
from web_monitorial.config.settings import config

logger = logging.getLogger("root")

def get_connection():
    try:
        params = config()
        return psycopg2.connect(**params)
    except (Exception, psycopg2.DatabaseError) as error:
        logger.error(error)

def stop_connection(conn):
    conn.close()


