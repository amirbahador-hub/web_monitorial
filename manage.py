from web_monitorial.kafka.consumer import consume as consume_func
from web_monitorial.kafka.producer import get_producer,single_produce, produce as produce_func
from web_monitorial.db.migrations.site_and_metric_tables import create_tables, drop_tables 
from web_monitorial.db.query import insert_site, get_metrics 
from web_monitorial.checker import check_site
from web_monitorial.db import get_connection, stop_connection

import typer
import logging
from web_monitorial.utils.regex import check_exists


logger = logging.getLogger("root")
conn = get_connection()
#logger_notifier = logging.getLogger("notification")

app = typer.Typer()


@app.command()
def migrate() -> None:
    """
    This command will Create Tables in your postgresql instance \n
    -> Create Site table \n
    -> Create Metric table
    """
    create_tables()

@app.command()
def revert_migration() -> None:
    """
    This command will Drop Tables in your postgresql instance \n
    -> Drop Site table \n
    -> Drop Metric table 
    """
    inp = input("Are you sure you want to delete your site and metric table(y/n)?")
    if inp:
        drop_tables()

@app.command()
def consume() -> None:
    """
    This command will start consuming from your kafka instance \n
    -> Pull masages from kafka instance \n
    -> Insert masages to postgresql instance
    """
    consume_func()

@app.command()
def produce() -> None:
    """
    This command will start your kafka producer for all sites \n
    - > Generate Metrics \n
    - > Send Metrics to Kafka 
    """
    produce_func()

@app.command()
def single_site(url: str) -> None:
    """
    This command will start your kafka producer for only one site (with no schaduling) \n
    - > Generate Metrics \n
    - > Send Metrics to Kafka 
    """
    
    single_produce(url, producer=get_producer())

@app.command()
def get_metric(url: str) -> None:
    """
    This command will give you metrics without any kafka usage (Just For Testing usage) \n
    - > Single Site \n
    - > Display Metrics
    """
    logger.info(check_site(url)) 

@app.command()
def add_site(name: str, url: str) -> None:
    """
    This command will create a site in database (Just For Testing usage) \n
    - > Single Site \n
    - > Display Metrics
    """
    id_ = insert_site(site_name=name, site_url=url)
    logger.info(f"{name} with id={id_} hass been created")

    
@app.command()
def fetch_metrics() -> None:
    """
    This command will print the metrics data from the table site_metric
    """
    get_metrics()
 
def get_con():
    return conn

if __name__ == "__main__":
    import logging.config
    logging.config.fileConfig('web_monitorial/config/logging.conf')
    app()
    stop_connection(conn)
