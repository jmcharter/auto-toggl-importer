import pytest
import timelogger


def test_config():
    username = timelogger.CONFIG["OpusVL"]["username"]
    password = timelogger.CONFIG["OpusVL"]["password"]
    assert type(username) == str
    assert type(password) == str
