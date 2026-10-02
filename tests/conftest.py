import pytest


@pytest.fixture
def sample_user():
    return {"name": "Ada Lovelace", "role": "engineer"}


@pytest.fixture
def tracked_resource():
    print("\n[setup] acquiring resource")
    resource = {"connected": True}
    yield resource
    print("[teardown] releasing resource")
    resource["connected"] = False


@pytest.fixture(scope="module")
def shared_counter():
    print("\n[setup] module-scoped shared_counter created")
    counter = {"value": 0}
    yield counter
    print(f"[teardown] module-scoped shared_counter torn down, final value={counter['value']}")
