from sched import scheduler
from typing import Callable

import logging
import time

logger = logging.getLogger("root")


def get_interval(num: int) -> float:
    return time.time() + num


def schedule_adder(*args, scheduler_obj: scheduler, func:Callable, interval:int):
    """
        this is a scheduler loop
        run the function and schedule the next one
    """

    func(*args)
    scheduler_obj.enterabs(time=get_interval(interval), priority=0, action=schedule_adder, 
                           argument=args, 
                           kwargs={"func":func,"interval":interval, "scheduler_obj":scheduler_obj})


