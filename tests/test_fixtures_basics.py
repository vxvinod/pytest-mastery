def test_sample_user_fixture(sample_user):
    assert sample_user["name"] == "Ada Lovelace"
    assert sample_user["role"] == "engineer"


def test_tracked_resource_is_connected(tracked_resource):
    assert tracked_resource["connected"] is True


def test_tracked_resource_gets_fresh_instance_each_test(tracked_resource):
    # default fixture scope is "function" -> a brand-new resource per test
    assert tracked_resource["connected"] is True
