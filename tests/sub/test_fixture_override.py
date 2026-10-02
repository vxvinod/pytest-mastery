def test_sub_directory_fixture_override(sample_user):
    # tests/sub/conftest.py redefines sample_user -> this definition wins here, not the parent's
    assert sample_user["name"] == "Grace Hopper"


def test_parent_fixture_still_reachable(tracked_resource):
    # not redefined under tests/sub, so the tests/conftest.py version is still used
    assert tracked_resource["connected"] is True
