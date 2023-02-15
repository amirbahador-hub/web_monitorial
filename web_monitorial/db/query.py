from web_monitorial.utils.decorators import db_connection 
from web_monitorial.db.models import Metric
from psycopg2.extensions import connection, cursor

import logging


logger = logging.getLogger("notification")


@db_connection
def insert_site(*, site_name: str, site_url: str, conn:connection, cur:cursor) -> int:
    """ insert a new site into the sites table """


    sql = """INSERT INTO site(site_name, site_url)
             VALUES(%s, %s) RETURNING site_id;"""

    cur.execute(sql, (site_name, site_url))

    # get the generated id back
    site_id = cur.fetchone()[0]
    # commit the changes to the database
    conn.commit()

    return site_id


@db_connection
def get_or_create_site(*, site_url:str, site_name:str="", conn:connection, cur:cursor) -> int:

    sql = """SELECT site_id FROM site WHERE site_url = %s;"""


    if not site_name:
        site_name = site_url
    """ query data from the vendors table """
 
    cur.execute(sql, (site_url,))

    if cur.rowcount:
        return cur.fetchone()[0] 
    return insert_site(site_name=site_name, site_url=site_url)



@db_connection
def insert_metric(*, metric:Metric, conn:connection, cur:cursor) -> int:
    """ insert a new site into the sites table """
    sql = """INSERT INTO site_metric(site_id, status_code, response_time, timestamp, pattern, pattern_found)
             VALUES(%s, %s, %s, %s, %s, %s) RETURNING metric_id;"""

 

    site_id = get_or_create_site(site_url=metric.url)
    cur.execute(sql, (site_id, metric.status_code, metric.response_time,
                              metric.timestamp, metric.pattern.regex ,metric.pattern.is_exists) )
    metric_id = cur.fetchone()[0]
    # commit the changes to the database
    conn.commit()
    return metric_id 


@db_connection
def get_metrics(*, conn:connection, cur:cursor) -> int:

    sql = """SELECT * FROM site_metric;"""

    cur.execute(sql)

    if cur.rowcount:
        pps = cur.fetchall()
        for p in pps:
            print(p)


