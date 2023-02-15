from web_monitorial.utils.decorators import db_connection 
from psycopg2.extensions import connection, cursor

import logging

logger = logging.getLogger("root")


@db_connection
def drop_tables(*, cur:cursor, conn:connection) -> None:
    """ drop tables in the PostgreSQL database"""
    commands = (
        """
        DROP TABLE site CASCADE
        """,
        """
        DROP TABLE site_metric
        """,
        """
        DROP EXTENSION pg_trgm;
        DROP EXTENSION btree_gin;
        """,

        )

    # drop tables one by one
    for command in commands:
        cur.execute(command)

    # commit the changes
    conn.commit()

    logger.info("Tables site and site_metric has been droped")
    logger.info("Revert migration Compelete")
 

@db_connection
def create_tables(*, cur:cursor, conn:connection) -> None:
    """ create tables in the PostgreSQL database"""
    commands = (
            """
            CREATE EXTENSION pg_trgm;
            CREATE EXTENSION btree_gin;
            """,
        """
        CREATE TABLE site(
            site_id SERIAL PRIMARY KEY,
            site_url VARCHAR(255) NOT NULL,
            site_name VARCHAR(255) NOT NULL
        )
        """,
        """
        CREATE TABLE site_metric(
                metric_id SERIAL PRIMARY KEY,
                site_id SERIAL,
                pattern VARCHAR(50),
                pattern_found BOOLEAN,
                status_code INTEGER NOT NULL CHECK(status_code<600 and status_code>199),
                response_time FLOAT8 NOT NULL,
                timestamp BIGINT NOT NULL,
                FOREIGN KEY (site_id)
                    REFERENCES site (site_id)
                    ON UPDATE CASCADE ON DELETE CASCADE
        )
        """,
        """
        CREATE INDEX idx_metric_site_id ON site_metric USING btree (site_id, status_code);
        """,
        """
        CREATE INDEX idx_metric_timestamp ON site_metric USING brin (timestamp);
        """,
        """
        CREATE INDEX idx_site_name ON site USING gin (site_name);
        """,
        )

    # create tables one by one
    for command in commands:
        cur.execute(command)

    # commit the changes
    conn.commit()

    logger.info("Tables site and site_metric has been created")
    logger.info("Migration Compelete")
 
