from requests import HTTPError
from web_monitorial.checker import check_site
from web_monitorial.utils import status

from requests.exceptions import  MissingSchema

import requests_mock
import requests
import pytest



URL = "https://example.com"
PATTERN = "^r.s"

@pytest.mark.parametrize(
    'pattern,result', [
        ("^r.s", True),
        ('$r' , False),
    ]
)
def test_pattern_checker(pattern, result):
    with requests_mock.Mocker() as m:
        m.get(URL, text='resp', status_code=200)
        response = check_site(URL, pattern)

        assert URL == response.get("url")
        assert 200 == response.get("status_code")
        assert 'resp' == requests.get(URL).text
        assert result == response["pattern"].get("is_exists")
        assert pattern == response["pattern"].get("regex")
        assert float == type(response["response_time"])


@pytest.mark.parametrize(
    'status,url', [
        (202, "http://test.com"),
        (401,"https://example.com"),
        (500,"http://mock.gov")
    ]
)
def test_status_checker(status, url):
    with requests_mock.Mocker() as m:
        m.get(url, text='resp', status_code=status)
        response = check_site(url, PATTERN)

        assert url == response.get("url")
        assert status == response.get("status_code")


def test_response_execption():
    url = "example.com"
    with requests_mock.Mocker() as m:
        m.get(url, text='resp', status_code=500)

        with pytest.raises(MissingSchema):
            response = check_site(url, PATTERN)

