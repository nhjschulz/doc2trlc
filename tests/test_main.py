import pytest
from doc2trlc.__main__ import main


def test_main_returns_zero():
    assert main() == 0