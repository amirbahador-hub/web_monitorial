from web_monitorial.kafka.producer import json_serialize
from web_monitorial.db.models import Site
import pytest


def test_valid_dict(msg_dict):
    assert bytes == type(json_serialize(msg_dict))

 
def test_value_execption(foo):
    assert None == json_serialize(foo)


