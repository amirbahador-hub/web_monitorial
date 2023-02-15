from web_monitorial.config.settings import config

from functools import wraps

import logging
import signal
import errno    # defines a number of symbolic error codes
import os
import psycopg2


logger = logging.getLogger("root")


def db_connection(function):
    def wrapper(*args, **kwargs):
            cur = None
            try:
                    from manage import get_con 

                    conn = get_con()
                    cur = conn.cursor()
                    result = function(cur=cur, conn=conn, *args, **kwargs)
                    return result
            except (Exception, psycopg2.DatabaseError) as error:
                    logger.warning(error)
            finally:
                    if cur is not None:
                        cur.close()

    return wrapper


def exception_logger(logger, level="error"):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                if level == "error":
                    logger.error(e, exc_info=True)
                    raise
                elif level == "warning":
                    logger.warning(e)
        return wrapper
    return decorator


def timeout(seconds=10, error_message=os.strerror(errno.ETIME)):
    # ETIME -> 103 timeout
    def decorator(func):
        def _handle_timeout(signum, frame):
            raise TimeoutError(error_message)

        @wraps(func)
        def wrapper(*args, **kwargs):
            signal.signal(signal.SIGALRM, _handle_timeout)
            signal.alarm(seconds)
            try:
                result = func(*args, **kwargs)
            finally:
                signal.alarm(0)
            return result

        return wrapper

    return decorator
