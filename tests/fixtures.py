from web_monitorial.db.models import Metric, Pattern
import pytest


@pytest.fixture
def metric() -> Metric:
    pattern = Pattern(regex="div", is_exists=True)
    return Metric(
            url="https://google.com",
            status_code=200,
            response_time=3.675578,
            timestamp=int(106531.165651),
            pattern=pattern
            )


@pytest.fixture
def msg_dict() -> dict:
    return  {
            "url": "URL",
            "status_code": 200,
            "response_time": 4.5665650,
            "pattern":{
                "regex":"^a.*r",
                "is_exists": False,
                },
            }


@pytest.fixture
def foo():
    class Foo():
        ...
    return Foo()


