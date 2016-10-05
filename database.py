import time
from mock import MagicMock

class Database:
    def __init__(self, passwd):
        self.passwd = passwd

    def query(self):
        time.sleep(3)
        return [4] * 12

def test_db_mocked_query():
    db = Database('sekrit')
    db.query = MagicMock(return_value = [1, 2, 3])
    assert sum(db.query()) == 6


def test_db_slow_query():
    db = Database('sekrit')
    assert sum(db.query()) == 4 * 12

