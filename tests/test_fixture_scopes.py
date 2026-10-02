def test_increment_once(shared_counter):
    shared_counter["value"] += 1
    assert shared_counter["value"] == 1


def test_increment_again_same_instance(shared_counter):
    # proves this is the SAME object as the previous test - module scope caches it
    shared_counter["value"] += 1
    assert shared_counter["value"] == 2


def test_function_scoped_resource_is_fresh(tracked_resource):
    # tracked_resource (Lesson 2) is function-scoped -> always connected=True, never carries state
    assert tracked_resource["connected"] is True
