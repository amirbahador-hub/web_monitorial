from web_monitorial.config.settings import config, URLS
from web_monitorial.checker import check_site
from web_monitorial.web_scheduler import schedule_adder, get_interval
from web_monitorial.utils.decorators import exception_logger
from web_monitorial.config.settings import KAFKA_TOPIC

from kafka import KafkaProducer

from sched import scheduler
import time
import logging
import json


from typing import ByteString

logger = logging.getLogger("root")


@exception_logger(logger=logger, level="warning")
def json_serialize(obj: dict) -> ByteString:
    return json.dumps(obj).encode('ascii')


def get_producer() -> KafkaProducer:
   param = config(section="kafka")
   return KafkaProducer(value_serializer=json_serialize, **param)


def single_produce(url:str ="https://google.com", name:str="", pattern:str="", producer="", topic:str=KAFKA_TOPIC) -> None:
    if not name:
        name = url
    if not producer:
        producer = get_producer()

    result = check_site(url, pattern)
    logger.info(result)
    result["name"] = name

    if result.get("error", None):
        logger.warning(result)
    else:
        producer.send(topic, result)
        #producer.flush()
        #exit()

def produce() -> None:
    producer = get_producer()
    scheduler_obj = scheduler(time.time)

    logger.info("producer started ...")

    for site in URLS:

        url = site["url"]
        interval = site.get("interval",1)
        name = site.get("name", url)
        pattern = site.get("pattern", "")

        kwargs = {
                "func":single_produce,
                "interval":interval,
                "scheduler_obj":scheduler_obj
                }

        scheduler_obj.enterabs(get_interval(interval), priority=0, action=schedule_adder, 
                           argument=(url, name, pattern, producer, KAFKA_TOPIC), 
                           kwargs=kwargs)
        logger.info(f"{site} added to scheduler")

    scheduler_obj.run()

