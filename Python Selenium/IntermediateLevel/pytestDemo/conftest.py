# Sceanrio - we have to place in conftest only when we think that particular fixtures is shared by multiple files.
import pytest


@pytest.fixture(scope='class')
def setup():
    print("I will be executing first")
    yield
    print("I will be executed last")

