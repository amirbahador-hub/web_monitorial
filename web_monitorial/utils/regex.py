import re
import logging

from web_monitorial.config.settings import REGEX_TIMEOUT
from web_monitorial.utils.decorators import timeout, exception_logger

logger = logging.getLogger("root")

@exception_logger(logger, level="warning")
@timeout(REGEX_TIMEOUT)
def check_exists(pattern, body) -> bool:
    if re.search(pattern, body):
        return True
    return False

