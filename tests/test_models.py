from web_monitorial.db.models import Metric 
import pytest


@pytest.mark.parametrize(
    'url,status_code,response_time,timestamp,pattern,is_exists', [
        ("http://test.com",200,4.5685,1675900627802,"a*b",True),
        ("http://test.com","200",4.5685,1675900627802,"a*b",True), # str status code
        ("http://test.com",200,"4.5685",1675900627802,"a*b",True), # str response_time
        ("http://test.com",200,4.5685,1675900627802,"a*b",1), # int is_exists
    ]
)
def test_model_type(url, status_code, response_time, timestamp, pattern, is_exists):
    msg_dict = {
            "url": url,
            "status_code": status_code,
            "response_time": response_time,
            "timestamp": timestamp,
            "pattern":{
                "regex":pattern,
                "is_exists": is_exists,
                },
            }

    res = Metric.parse_obj(msg_dict)
    assert str(msg_dict["url"]) == res.url
    assert int(msg_dict["status_code"]) == res.status_code
    assert float(msg_dict["response_time"]) == res.response_time
    assert str(msg_dict["pattern"]["regex"]) == res.pattern.regex
    assert bool(msg_dict["pattern"]["is_exists"]) == res.pattern.is_exists

 
def test_value_execption():
    url = "example.com"
    status_code = 444
    response_time = 4.65
    pattern = "ab"
    is_exists = True

    msg_dict = {
            "url": url,
            "status_code": status_code,
            "response_time": response_time,
            "pattern":{
                "regex":pattern,
                "is_exists": is_exists,
                },
            }
    with pytest.raises(ValueError):
        Metric.parse_obj(msg_dict)
