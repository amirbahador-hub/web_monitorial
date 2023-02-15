from web_monitorial.config.settings import REQUEST_TIMEOUT
from web_monitorial.utils.regex import check_exists
from web_monitorial.utils.decorators import exception_logger

import logging
import requests 
import time

logger = logging.getLogger("root")


@exception_logger(logger=logger)
def check_site(url, pattern="") -> dict:
    response = requests.get(url, timeout=REQUEST_TIMEOUT)

    is_exists = False
    if pattern:
        is_exists = check_exists(pattern, response.text)

    return {
            "url": url,
            "status_code": response.status_code,
            "response_time": response.elapsed.total_seconds(),
            "timestamp": int(time.time()), # millisec epoch time
            "pattern":{
                "regex":pattern,
                "is_exists": is_exists,
                },
            }
       

if __name__ == "__main__":
    logger.info(check_site("https://google.com"))
