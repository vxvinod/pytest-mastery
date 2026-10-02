import pytest


@pytest.fixture
def sample_user():
    return {"name": "Grace Hopper", "role": "engineer"}
