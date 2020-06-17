# pylint: disable=redefined-outer-name

"""
BASE FIXTURE FOR CORA ACCEPTANCE TESTS
"""
import pytest


@pytest.fixture(scope="session")
def new_something():
    return "something"
