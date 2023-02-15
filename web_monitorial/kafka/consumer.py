from web_monitorial.config.settings import config
from web_monitorial.db.query import insert_metric
from web_monitorial.db.models import Metric

from kafka import KafkaConsumer

import logging
import json


logger = logging.getLogger("root")

def get_consumer() -> KafkaConsumer:
  param = config(section="kafka")
  return KafkaConsumer(
            'web_monitorial',
            auto_offset_reset='earliest',
            group_id="consumer-group-a",
            **param
            )


def consume():
    consumer = get_consumer()
    logger.info("Starting consuming...")
    for index,msg in enumerate(consumer):
        msg_dict = json.loads(msg.value)
        data = Metric.parse_obj(msg_dict)
        insert_metric(metric=data)
        logger.info(f"msg {index} has been consumed successfully => {data}")


if __name__ == "__main__":
    consume()
    
