from web_monitorial.db.query import insert_metric, insert_site, get_or_create_site
import mock
import pytest


@pytest.mark.parametrize(
    'func,site_name,site_url', [
        (insert_site,"Google","https://google.com"),
        (insert_site,None,"https://google.com"),
        (get_or_create_site,"Google","https://google.com"),
        (get_or_create_site,None,"https://google.com"),
    ]
)
@mock.patch("psycopg2.connect")
def test_insert_or_get_site(mock_connect, func,site_name, site_url):
    mock_con = mock_connect.return_value  # result of psycopg2.connect(**connection_stuff)
    mock_cur = mock_con.cursor.return_value  # result of con.cursor(cursor_factory=DictCursor)
    mock_cur.fetchone.return_value = (3,)# return this when calling cur.fetchone()
    res = func(site_name=site_name, site_url=site_url)
    assert isinstance(res, int)


@pytest.mark.parametrize(
    'result', [
        (3,)
    ]
)
@mock.patch("psycopg2.connect")
def test_insert_metric(mock_connect, result, metric):
    mock_con = mock_connect.return_value  # result of psycopg2.connect(**connection_stuff)
    mock_cur = mock_con.cursor.return_value  # result of con.cursor(cursor_factory=DictCursor)
    mock_cur.fetchone.return_value = (result,)# return this when calling cur.fetchone()
    print(metric)
    res = insert_metric(metric=metric)
    assert isinstance(res, int)


