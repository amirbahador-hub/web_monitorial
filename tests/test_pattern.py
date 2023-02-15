import pytest
from web_monitorial.utils.regex import check_exists


@pytest.mark.parametrize(
    'text,result', [
        ('Amir Bahador' , False),
        ('amir bahador' , True),
        #('A' * 100000, None),  # TimeOut execption handle by logger and return nothing
    ]
)
def test_regex(text, result):
    pattern = '.*b'
    assert result ==  check_exists(pattern, text)
