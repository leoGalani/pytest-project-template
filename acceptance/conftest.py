# pylint: disable=redefined-outer-name

"""
BASE FIXTURE!
"""
import pytest


@pytest.fixture(scope="session")
def new_something():
    return "something"
